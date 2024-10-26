from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QLabel, QGridLayout,
                             QLineEdit)
from view.presentacionView.TituloApp import tituloApp,descricionApp

def get_email_label():
    emailLabel = QLabel("email")
    return emailLabel

def get_email_text():
    email_text = QLineEdit()
    email_text.setPlaceholderText("Email aqui...")
    return email_text