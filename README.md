# Summary

This project setup provides a basic CLI tool with the capabilities to read files, write JSON, manage configuration, and change directories, all while being modularized into different Python files and classes. You can extend this as needed for more functionality.

# Setup:

1. Create a venv using the following command:

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

2. Install the dependencies using the command: `pip install -r requirements.txt`

Your development environment is now ready.

# Creating a binary using pyinstaller

Using the command `pyinstaller --onefile -n mycli my_cli_tool/cli.py` you get the `./mycli.spec` file which can be used to generate a binsary.

Run the following command to get started: `pyinstaller mycli.spec`

You will find a new directory called `dist/mycli` within you will find the binary `my-cli`

## What is the mycli.spec File?
The mycli.spec file is a specification file that PyInstaller uses to define how your Python application should be packaged into an executable. This file includes detailed instructions on what to include in the final package, such as scripts, modules, data files, and any additional settings.

Here's a breakdown of the key components of a typical .spec file:

block_cipher: This variable is used to specify an optional cipher for encrypting Python bytecode. It is often set to None.

Analysis: This class collects information about your application. It examines your script and determines all the dependencies (modules, data files, etc.) needed to run it.

PYZ: This class packages the collected Python files into a single .pyz archive, which is a zipped archive of all Python code.

EXE: This class creates the executable file from the .pyz archive and the bootloader, which is responsible for starting your Python code.

COLLECT: This class gathers all the necessary files (executables, libraries, data files) into a single directory.

## What Does pyinstaller mycli.spec Do?
When you run the command pyinstaller mycli.spec, PyInstaller uses the instructions in the .spec file to build your application into an executable. Here's a step-by-step breakdown of what happens:

Reading the Spec File: PyInstaller reads the mycli.spec file to understand how to package your application.

Analysis: PyInstaller analyzes the cli.py script to determine all the dependencies (imported modules, data files, etc.) that are required to run your application.

Collecting Files: It collects all the necessary Python files, modules, and data files as specified in the Analysis part of the .spec file.

Creating a PYZ Archive: It packages the collected Python files into a .pyz archive. This archive contains all the bytecode for your application.

Creating the Executable: PyInstaller creates an executable using the EXE class. This step combines the Python interpreter, the .pyz archive, and a bootloader into a single executable file.

Collecting Everything: Finally, the COLLECT step gathers the executable, any additional binaries, data files, and other required files into a single directory. This directory will be the output directory (e.g., dist/mycli).

# Test the Program

``` bash
./mycli --help
./mycli --read example.txt
./mycli --write-json example.json
./mycli --config new_value
./mycli --change-dir /path/to/directory
```