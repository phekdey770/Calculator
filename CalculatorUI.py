import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit, QMessageBox)
from PyQt5.QtCore import Qt


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setGeometry(100, 100, 320, 450)
        self.setStyleSheet("background-color: #2E2E2E; border-radius: 10px;")
        self.createUI()
        self.history = []  # To store calculation history

    def createUI(self):
        # Layout
        mainLayout = QVBoxLayout()

        # Display Screen
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setFixedHeight(60)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setStyleSheet("""
            QLineEdit {
                background-color: #1E1E1E;
                color: #FFFFFF;
                font-size: 28px;
                border: 2px solid #4CAF50;
                border-radius: 10px;
                padding: 10px;
            }
        """)

        # Buttons Layout
        buttonsLayout = QGridLayout()

        buttons = {
            '7': (0, 0), '8': (0, 1), '9': (0, 2), '/': (0, 3),
            '4': (1, 0), '5': (1, 1), '6': (1, 2), '*': (1, 3),
            '1': (2, 0), '2': (2, 1), '3': (2, 2), '-': (2, 3),
            '0': (3, 0), '+': (3, 1), '=': (3, 2), '.': (3, 3),
            '+/-': (4, 0), 'C': (4, 1), '←': (4, 2), 'Info': (4, 3)  # Added new buttons
        }

        for btnText, pos in buttons.items():
            button = QPushButton(btnText)
            button.setFixedSize(70, 70)
            
            # Define button styles based on text
            if btnText == 'C':
                style = """
                    QPushButton {
                        background-color: #FF0000; /* Red */
                        color: #FFFFFF; /* White */
                        font-size: 22px;
                        border-radius: 35px;
                    }
                    QPushButton:hover {
                        background-color: #CC0000;
                    }
                    QPushButton:pressed {
                        background-color: #990000;
                    }
                """
            elif btnText in ['/', '*', '-', '+']:
                style = """
                    QPushButton {
                        background-color: #FFA500; /* Orange */
                        color: #FFFFFF; /* White */
                        font-size: 22px;
                        border-radius: 35px;
                    }
                    QPushButton:hover {
                        background-color: #FF8C00;
                    }
                    QPushButton:pressed {
                        background-color: #CC7000;
                    }
                """
            elif btnText == '=':
                style = """
                    QPushButton {
                        background-color: #008000; /* Green */
                        color: #FFFFFF; /* White */
                        font-size: 22px;
                        border-radius: 35px;
                    }
                    QPushButton:hover {
                        background-color: #006400;
                    }
                    QPushButton:pressed {
                        background-color: #004d00;
                    }
                """
            elif btnText == '.':
                style = """
                    QPushButton {
                        background-color: #4CAF50; /* Default green */
                        color: #FFFFFF; /* White */
                        font-size: 22px;
                        border-radius: 35px;
                    }
                    QPushButton:hover {
                        background-color: #45a049;
                    }
                    QPushButton:pressed {
                        background-color: #388E3C;
                    }
                """
            elif btnText == '+/-':
                style = """
                    QPushButton {
                        background-color: #2196F3; /* Blue */
                        color: #FFFFFF; /* White */
                        font-size: 22px;
                        border-radius: 35px;
                    }
                    QPushButton:hover {
                        background-color: #1976D2;
                    }
                    QPushButton:pressed {
                        background-color: #1565C0;
                    }
                """
            elif btnText == '←':
                style = """
                    QPushButton {
                        background-color: #FFC107; /* Amber */
                        color: #FFFFFF; /* White */
                        font-size: 22px;
                        border-radius: 35px;
                    }
                    QPushButton:hover {
                        background-color: #FFA000;
                    }
                    QPushButton:pressed {
                        background-color: #FF6F00;
                    }
                """
            elif btnText == 'Info':
                style = """
                    QPushButton {
                        background-color: #9E9E9E; /* Grey */
                        color: #FFFFFF; /* White */
                        font-size: 22px;
                        border-radius: 35px;
                    }
                    QPushButton:hover {
                        background-color: #757575;
                    }
                    QPushButton:pressed {
                        background-color: #616161;
                    }
                """
            else:
                style = """
                    QPushButton {
                        background-color: #4CAF50; /* Default green */
                        color: #FFFFFF; /* White */
                        font-size: 22px;
                        border-radius: 35px;
                    }
                    QPushButton:hover {
                        background-color: #45a049;
                    }
                    QPushButton:pressed {
                        background-color: #388E3C;
                    }
                """
            
            button.setStyleSheet(style)
            button.clicked.connect(self.onButtonClick)
            buttonsLayout.addWidget(button, pos[0], pos[1])

        mainLayout.addWidget(self.display)
        mainLayout.addLayout(buttonsLayout)

        self.setLayout(mainLayout)

    def onButtonClick(self):
        button = self.sender()
        text = button.text()

        if text == 'C':
            self.display.clear()
            # self.history.clear()  # Clear history on 'C'
        elif text == '=':
            try:
                result = eval(self.display.text())
                self.history.append(self.display.text() + ' = ' + str(result))
                self.display.setText(str(result))
            except Exception as e:
                self.display.setText('Error')
        elif text == '+/-':
            current_text = self.display.text()
            if current_text and current_text[0] in '-0123456789':
                if current_text[0] == '-':
                    self.display.setText(current_text[1:])
                else:
                    self.display.setText('-' + current_text)
        elif text == '←':
            current_text = self.display.text()
            self.display.setText(current_text[:-1])
        elif text == 'Info':
            self.showHistory()
        else:
            current_text = self.display.text()
            new_text = current_text + text
            self.display.setText(new_text)

    def showHistory(self):
        if self.history:
            history_text = '\n'.join(self.history)
        else:
            history_text = 'No history available.'

        QMessageBox.information(self, 'Calculation History', history_text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
