import sys
import json
from PyQt6.QtWidgets import (QApplication, QMainWindow, QGridLayout,
                             QWidget, QLabel, QTextEdit, QLineEdit, 
                             QPushButton)
from PyQt6.QtCore import Qt
from config import DEFINITIONS_FILE, APP_STYLE_SHEET, BUTTON_1_STYLE_SHEET


# Define a custom main window class that inherits from QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Word Definition")        

        self.setStyleSheet(APP_STYLE_SHEET)

        self.definitions = self.load_data()

        # Create a grid layout
        layout = QGridLayout()

        self.text_input = QLineEdit()
        self.text_input.returnPressed.connect(self.define_word)


        button = QPushButton("Define")
        button.setToolTip("Define")
        button.setFixedWidth(100)
        button.setStyleSheet(BUTTON_1_STYLE_SHEET)
        button.clicked.connect(self.define_word)

        self.text_output = QTextEdit()
        self.text_output.setReadOnly(True)

        # Add widgets to the layout
        layout.addWidget(self.text_input, 0, 0)
        layout.addWidget(button, 0, 1)
        layout.addWidget(self.text_output, 1, 0, 1, 2)  # Spans two columns

        # Create a main widget and set the layout
        main_widget = QWidget()
        main_widget.setLayout(layout)

        self.setCentralWidget(main_widget)  # Set the main widget as central

        self.show()


    def load_data(self):
        try:
            with open(DEFINITIONS_FILE) as file:
                data = json.load(file)
                return data
        except Exception as err:
            raise err


    def define_word(self):
        word = self.text_input.text()
        if word:
            results = self.definitions.get(word, None)

            if results is None:
                print("This term is not available in this dictionary.")
            else:
                for result in results:
                    print(result)
        


# Main function to create and run the application
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    # window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
