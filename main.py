import sys
import json
from PyQt6.QtWidgets import (QApplication, QMainWindow, QGridLayout,
                             QWidget, QLabel, QTextEdit, QLineEdit, 
                             QPushButton)
from PyQt6.QtCore import Qt
from config import DEFINITIONS_FILE, APP_STYLESHEET, BUTTON1_STYLESHEET, BUTTON2_STYLESHEET, TITLE_STYLESHEET


# Define a custom main window class that inherits from QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WordWise")        

        self.setStyleSheet(APP_STYLESHEET)

        self.definitions = self.load_data()

        # Create a grid layout
        layout = QGridLayout()

        title = QLabel("WordWise")
        title.setStyleSheet(TITLE_STYLESHEET)

        self.text_input = QLineEdit()
        self.text_input.returnPressed.connect(self.define_word)


        button1 = QPushButton("Define")
        button1.setToolTip("Define")
        # button1.setFixedWidth(100)
        button1.setStyleSheet(BUTTON1_STYLESHEET)
        button1.clicked.connect(self.define_word)

        button2 = QPushButton("Clear")
        button2.setToolTip("Clear")
        # button2.setFixedWidth(100)
        button2.setStyleSheet(BUTTON2_STYLESHEET)
        button2.clicked.connect(self.clear_all)

        self.text_output = QTextEdit()
        self.text_output.setReadOnly(True)

        signature = QLabel("© 2024 E>")

        # Add widgets to the layout
        layout.addWidget(title, 0, 0, 1, 3, alignment=Qt.AlignmentFlag.AlignCenter)
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
        else:
            print("No input for definition search.")

    def clear_all(self):
        self.text_input.clear()
        self.text_output.clear()
        


# Main function to create and run the application
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    # window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
