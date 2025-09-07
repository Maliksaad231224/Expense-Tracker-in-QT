# -*- coding: utf-8 -*-
import sys
from dotenv import load_dotenv
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QHeaderView
import os
from ui_form import Ui_MainWindow


load_dotenv()
print(repr(os.getenv("myname")))
print(repr(os.getenv("password")))
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Use setPlaceholderText for modern placeholder style
        self.ui.pendingpaymentstable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.pendingpaymentstable.verticalHeader().setVisible(False)
        self.ui.expectedpaymentstable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.expectedpaymentstable.verticalHeader().setVisible(False)
        self.ui.username_field.setPlaceholderText("Enter your username...")
        self.ui.password_field.setPlaceholderText("Enter your password...")
        self.ui.stackedWidget.setCurrentIndex(2)
        # Mask password input

        self.theme = "light"

        # Load credentials from .env
        self.username = os.getenv("myname")
        self.password = os.getenv("password")

        # Connect login button
        self.ui.invert_color.clicked.connect(self.invert_color)
        self.ui.login_button.clicked.connect(self.login)

    def invert_color(self):
        print(self.theme)
            # List of all your frames
        if self.theme == "light":
            self.ui.frame.setStyleSheet("background-color: #111827; color: black;")
            self.ui.frame_4.setStyleSheet("background-color: #111827; color: black;")
            self.ui.frame_9.setStyleSheet("background-color: #111827; color: black;")
            self.ui.frame_5.setStyleSheet("background-color: #111827; color: black;")
            self.ui.frame_10.setStyleSheet("background-color: #111827; color: black;")
            self.ui.frame_7.setStyleSheet("background-color: #111827; color: black;")
            self.ui.frame_6.setStyleSheet("background-color: #111827; color: black;")
            self.ui.frame_8.setStyleSheet("background-color: #111827; color: black;")
            self.ui.frame_3.setStyleSheet("background-color: #111827; color: black;")
            self.ui.frame_4.setStyleSheet("background-color: #111827; color: black;")
            self.ui.frame_11.setStyleSheet("background-color: #111827; color: black;")

            self.ui.label_15.setStyleSheet(" color: white;")
            self.ui.label_16.setStyleSheet(" color: white;")
            self.ui.label_17.setStyleSheet(" color: white;")
            self.ui.label_7.setStyleSheet(" color: white;")
            self.ui.label_9.setStyleSheet(" color: white;")
            self.ui.label_18.setStyleSheet(" color: white;")
            self.ui.user.setStyleSheet(" color: white;")
            self.theme = "dark"  # toggle

        else:
            self.ui.frame.setStyleSheet("background-color: white; color: black;")
            self.ui.frame_4.setStyleSheet("background-color: white; color: black;")
            self.ui.frame_9.setStyleSheet("background-color: white; color: black;")
            self.ui.frame_11.setStyleSheet("background-color: white; color: black;")
            self.ui.frame_5.setStyleSheet("background-color: white; color: black;")
            self.ui.frame_3.setStyleSheet("background-color: white; color: black;")
            self.ui.frame_4.setStyleSheet("background-color: white; color: black;")
            self.ui.frame_10.setStyleSheet("background-color: white; color: black;")
            self.ui.frame_8.setStyleSheet("background-color: white; color: black;")
            self.ui.frame_7.setStyleSheet("background-color: white; color: black;")
            self.ui.frame_6.setStyleSheet("background-color: white; color: black;")

            self.ui.user.setStyleSheet(" color: black;")
            self.ui.label_7.setStyleSheet(" color: black;")
            self.ui.label_9.setStyleSheet(" color: black;")
            self.ui.label_15.setStyleSheet(" color: black;")
            self.ui.label_16.setStyleSheet(" color: black;")
            self.ui.label_17.setStyleSheet(" color: black;")
            self.ui.label_18.setStyleSheet(" color: black;")

            self.theme = "light"  # toggle


    def maindashboard(self):

        self.ui.stackedWidget.setCurrentIndex(1)
    def login(self):
        username_input = self.ui.username_field.toPlainText()  # QLineEdit uses .text()
        password_input = self.ui.password_field.toPlainText()
        print(self.username, self.password, username_input, password_input)

        if username_input == self.username and password_input == self.password:
            self.maindashboard()
        else:
            print("Login failed")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
