# my_cli_tool/cli.py

import argparse
import sys
from my_cli_tool.file_manager import FileManager
from my_cli_tool.config_manager import ConfigManager

def main():
    parser = argparse.ArgumentParser(description='CLI tool for file and config management')
    parser.add_argument('--read', '-r', type=str, help='Read a file')
    parser.add_argument('--write-json', '-w', type=str, help='Write JSON to a file')
    parser.add_argument('--config', '-c', type=str, help='Update config file')
    parser.add_argument('--change-dir', '-cd', type=str, help='Change directory')
    args = parser.parse_args()

    file_manager = FileManager()
    config_manager = ConfigManager()

    if args.read:
        content = file_manager.read_file(args.read)
        print(content)

    if args.write_json:
        data = {"example": "data"}
        file_manager.write_json(args.write_json, data)
        print(f'JSON data written to {args.write_json}')

    if args.config:
        config = config_manager.read_config()
        config['new_setting'] = args.config
        config_manager.write_config(config)
        print(f'Config updated: {config}')

    if args.change_dir:
        new_dir = file_manager.change_directory(args.change_dir)
        print(f'Changed directory to {new_dir}')

if __name__ == '__main__':
    main()
