from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QLabel, QGridLayout,
                             QLineEdit)
from view.presentacionView.TituloApp import tituloApp,descricionApp

def get_password_label():
    password_label = QLabel("Contraseña")
    return password_label

def get_password_text():
    password_text = QLineEdit()
    password_text.setPlaceholderText("Passoword aqui...")
    password_text.setEchoMode(QLineEdit.EchoMode.Password)
    return password_text