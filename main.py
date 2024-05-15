import sys
import json
from PyQt6.QtWidgets import (QApplication, QMainWindow, QGridLayout,
                             QWidget, QLabel, QTextEdit, QLineEdit,
                             QPushButton)
from PyQt6.QtCore import Qt
from config import *


class MainWindow(QMainWindow):
    """
    Define a custom main window class that inherits from QMainWindow.
    """

    def __init__(self):
        """
        Initialize the main window.

        Sets up the window title, stylesheets, and initializes necessary widgets.
        """

        super().__init__()
        self.setWindowTitle("WordWise Dictionary")

        self.setStyleSheet(APP_STYLESHEET)

        self.definitions = self.load_data()

        # Create a grid layout
        layout = QGridLayout()

        title = QLabel("WordWise")
        title.setStyleSheet(TITLE_STYLESHEET)

        self.text_input = QLineEdit()
        self.text_input.returnPressed.connect(self.define_word)

        button1 = QPushButton("Define")
        button1.setStyleSheet(BUTTON1_STYLESHEET)
        button1.clicked.connect(self.define_word)

        button2 = QPushButton("Clear")
        button2.setStyleSheet(BUTTON2_STYLESHEET)
        button2.clicked.connect(self.clear_all)

        self.text_output = QTextEdit()
        self.text_output.setReadOnly(True)

        signature = QLabel("© 2024 E>")
        signature.setStyleSheet(SIGNATURE_STYLESHEET)

        # Add widgets to the layout
        layout.addWidget(title, 0, 0, 1, 3,
                         alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.text_input, 1, 0)
        layout.addWidget(button1, 1, 1)
        layout.addWidget(button2, 1, 2)
        layout.addWidget(self.text_output, 2, 0, 1, 3)  # Spans three columns
        layout.addWidget(signature, 3, 2)

        # Create a main widget and set the layout
        main_widget = QWidget()
        main_widget.setLayout(layout)

        self.setCentralWidget(main_widget)  # Set the main widget as central

        self.show()

    def load_data(self):
        """
        Load data from the definitions file.

        Attempts to open the definitions file and load its contents using JSON format.
        Returns the loaded data.

        Raises:
            Exception: If an error occurs while loading the data from the file.
        """

        try:
            with open(DEFINITIONS_FILE) as file:
                data = json.load(file)
                return data
        except Exception as err:
            raise err

    def define_word(self):
        """
        Define a word based on the input text.

        Retrieves the input text from the text input field and looks up its definition in the loaded data.
        If the word is found, displays its definition in the text output field. If not found, displays a message indicating it's not available.
        If no input is provided, displays a message indicating no input for definition search.
        """

        word = self.text_input.text()
        if word:
            results = self.definitions.get(word, None)

            if results is None:
                output_msg = "This term is not available in this dictionary."
            else:
                output_msg = ""
                for result in results:
                    output_msg += f"- {result}\n\n"
        else:
            output_msg = "No input for definition search."

        self.text_output.setText(output_msg)

    def clear_all(self):
        """
        Clear all input and output fields.

        Clears the text input field and the text output field.
        """

        self.text_input.clear()
        self.text_output.clear()


def main():
    """
    Entry point for the application.

    Initializes the QApplication, creates the main window, and starts the application event loop.
    """

    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
