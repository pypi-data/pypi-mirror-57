from pydantic import BaseModel
from typing import List, Union
from datetime import datetime
from pathlib import Path
import shutil
import json
import requests


class Config(BaseModel):
    api_base_url: str  # Where the service template API can be found
    update_dir: str  # The root directory of the microservice
    package_file: str  # The ehelply-package.json file which contains version and updating information for the microservice
    access_key: str  # Access key identifies this microservice to the updater service
    secret_key: str  # Secret key gives a secret passkey to the updater service to validate that this is a valid service


class FileMeta(BaseModel):
    uuid: str
    name: str
    path: str


class FileMetas(BaseModel):
    files: List[FileMeta]


class File(FileMeta):
    content: str


class Update(BaseModel):
    version: str
    changelog: List[str]


class Updates(BaseModel):
    updates: List[Update]


class Updater:
    def __init__(self, config: Config) -> None:
        self.config: Config = config
        self.package: dict = {}
        self.headers: dict = {
            "X-AccessKey": config.access_key,
            "X-SecretKey": config.secret_key,
        }
        self.setup()

    def setup(self):
        """
        Setup the updater utility
        :return:
        """
        with open(self.config.package_file, 'r') as file:
            self.package.update(json.load(file))

    def save_updated_package(self, update_information: Updates):
        self.package['template_version'] = update_information.updates[0].version

        with open(self.config.package_file, 'w') as file:
            json.dump(self.package, file)

    def is_update_required(self) -> bool:
        """
        Check with the service template service for whether an update exists

        Expected Response:
        {
            "required": bool
        }
        :return:
        """
        response = requests.post(self.config.api_base_url + "/update", json={"package": self.package}, headers=self.headers)

        if response.status_code == 200:
            return response.json()['required']

        raise Exception("Unable to determine whether an update is required")

    def get_update_information(self) -> Updates:
        """
        Gets information about the update from the server
        :return:
        """
        response = requests.post(self.config.api_base_url + "/update/details", json={"package": self.package}, headers=self.headers)

        if response.status_code == 200:
            return Updates(**response.json())

        raise Exception("Unable to get update information")

        # return Updates(updates=[
        #     Update(version="2.0.0", changelog=["Added a thing", "Removed a thing"]),
        #     Update(version="1.9.0", changelog=["Did a cool thing", "Did a different cool thing"]),
        # ])

    def get_file_list(self) -> FileMetas:
        """
        Returns a list of files that need to be updated
        :return:
        """

        response = requests.post(self.config.api_base_url + "/update/files", json={"package": self.package}, headers=self.headers)

        if response.status_code == 200:
            return FileMetas(**response.json())

        raise Exception("Unable to retrieve an update file list")

        # return FileMetas(files=[
        #     FileMeta(uuid="test", name="my_backup_test.txt", path="tests"),
        #     FileMeta(uuid="test", name="another_test.txt", path="tests/nested")
        # ])

    def get_updated_file(self, file: FileMeta) -> File:
        """
        Retrieves the contents of an updated file from the server
        :return:
        """
        response = requests.post(self.config.api_base_url + "/update/file", json={"file_meta": file.dict()}, headers=self.headers)

        if response.status_code == 200:
            return File(**response.json())

        raise Exception("Unable to retrieve updated file")

        # return File(
        #     name="my_update_test.txt",
        #     path="tests/service",
        #     uuid="test",
        #     content="I am the new epic content of this file"
        # )

    def save_updated_file(self, file: File):
        """
        Updates the file in the microservice
        :return:
        """
        file_path = Path(self.config.update_dir).resolve().joinpath(file.path).joinpath(file.name)
        with open(str(file_path), 'w') as io_file:
            io_file.write(file.content)

    def backup(self, location, file: FileMeta):
        """
        Backup the microserivces current service template files
        :return:
        """
        original = Path(self.config.update_dir).resolve().joinpath(file.path).joinpath(file.name)
        backup = Path(location).joinpath(file.path)
        backup.mkdir(parents=True, exist_ok=True)
        backup = backup.joinpath(file.name)
        shutil.copy(original, backup)

    def create_backup_readme(self, location, update_information: Updates):
        update_information_str: str = ""
        for update in update_information.updates:
            update_information_str += """* {version}
""".format(version=update.version)
            for changelog_item in update.changelog:
                update_information_str += """   * {item}
""".format(item=changelog_item)

        readme: str = """# Service Template Backup
This is a backup which was autogenerated by updating the service template.
You are free to remove this backup if it is of no use to you. 

## Update Information
{update_information}""".format(update_information=update_information_str)

        with open(str(location.joinpath("readme.md")), 'w') as file:
            file.write(readme)

    def preview(self) -> Union[bool, Updates]:
        """
        Determine whether an update is required and get information about it
        :return:
        """
        if self.is_update_required():
            return self.get_update_information()
        else:
            return False

    def update(self) -> Union[bool, Updates]:
        """
        Preform an update on the microservice with the given configuration
        :return:
        """
        if self.is_update_required():
            # Get update information
            update_information: Updates = self.get_update_information()

            # Setup backup location
            backup_location = Path(self.config.update_dir).resolve().joinpath(
                datetime.utcnow().strftime("%Y%m%d-%H%M%S-utc.service-template.bak/"))
            backup_location.mkdir()

            self.create_backup_readme(backup_location, update_information)

            for file_meta in self.get_file_list().files:
                # Get typing information
                file_meta: FileMeta = file_meta

                # Backup original version
                self.backup(location=backup_location, file=file_meta)

                # Retrieve updated file from the server
                file: File = self.get_updated_file(file_meta)

                # Save the updated file
                self.save_updated_file(file)

            self.save_updated_package(update_information)

            # Return with update information
            return update_information
        else:
            return False
