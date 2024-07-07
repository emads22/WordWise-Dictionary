# WordWise Dictionary

![WordWise_Dictionary_logo](./assets/images/WordWise_Dictionary_logo.png)

## Overview
WordWise Dictionary is an offline user-friendly desktop GUI application built with PyQt6 that provides a convenient way to look up definitions of words. Whether you're a student, professional, or language enthusiast, WordWise Dictionary helps you quickly find the meanings of unfamiliar words, enhancing your vocabulary and comprehension.

## Features
- **Search Definitions**: Users can enter a word in the text input field and press the "Define" button to search for its definition.
- **Clear Functionality**: Users can clear both the input and output fields by pressing the "Clear" button.

## Technologies Used
- **PyQt6**: A set of Python bindings for the Qt application framework.
- **pyinstaller**: A library for bundling Python applications into standalone executables.

## Setup
1. Clone the repository.
2. Ensure Python 3.x is installed.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Users can expand the dictionary by adding more definitions to the `data.json` file as needed.
5. Locate the executable file in the `executable` folder.
6. No additional setup is necessary.

## Usage
1. Run the script using `python wordwise.py`.
2. Enter a word in the input field and press the "Define" button to search for its definition.
3. Press the "Clear" button to clear both the input and output fields.

## Creating the Executable File
Follow these steps to generate an executable file for WordWise Dictionary using PyInstaller:

1. **Navigate to Project Directory**: Open a terminal or command prompt and change directory to the location where your WordWise Dictionary project is saved.

2. **Navigate to Executable Folder**: If you haven't already, create an "executable" folder in the project directory.

3. **Run PyInstaller Command**: Execute the following command in the terminal to create the executable file. Ensure PyInstaller is installed (it will be automatically installed if you run `pip install -r requirements.txt` earlier):
   ```sh
   pyinstaller --onefile --windowed --noconsole --add-data "../assets;assets" --icon="../assets/icon/wordwise.ico" "../wordwise.py"
   ```

4. **Locate the Executable File**: Once the command finishes, locate the generated executable file in the "dist" folder.

5. **Move Executable File**: Move the executable file (`wordwise.exe`) from the "dist" folder to the "executable" folder in the project directory. You can then delete the "build" and "dist" folders along with their contents, as well as the "wordwise.spec" file.

6. **Run the WordWise Application**: Double-click the `wordwise.exe` file to launch the WordWise Dictionary application. It will have the WordWise icon associated with it.

## Contributing
Contributions are welcome! Here are some ways you can contribute to the project:
- Report bugs and issues
- Suggest new features or improvements
- Submit pull requests with bug fixes or enhancements

## Author
- Emad &nbsp; E>
  
  [<img src="https://img.shields.io/badge/GitHub-Profile-blue?logo=github" width="150">](https://github.com/emads22)

## License
This project is licensed under the MIT License, which grants permission for free use, modification, distribution, and sublicense of the code, provided that the copyright notice (attributed to [emads22](https://github.com/emads22)) and permission notice are included in all copies or substantial portions of the software. This license is permissive and allows users to utilize the code for both commercial and non-commercial purposes.

Please see the [LICENSE](LICENSE) file for more details.