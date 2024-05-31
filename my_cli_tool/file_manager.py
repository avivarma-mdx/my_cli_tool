# my_cli_tool/file_manager.py

import json
import os

class FileManager:
    def read_file(self, file_path):
        with open(file_path, 'r') as file:
            return file.read()

    def write_json(self, file_path, data):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def change_directory(self, path):
        os.chdir(path)
        return os.getcwd()
