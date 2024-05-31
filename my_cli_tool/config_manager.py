# my_cli_tool/config_manager.py

import json
import os

class ConfigManager:
    def __init__(self, config_path='config.json'):
        self.config_path = config_path
        if not os.path.exists(self.config_path):
            self.write_config({})

    def read_config(self):
        with open(self.config_path, 'r') as file:
            return json.load(file)

    def write_config(self, config):
        with open(self.config_path, 'w') as file:
            json.dump(config, file, indent=4)
