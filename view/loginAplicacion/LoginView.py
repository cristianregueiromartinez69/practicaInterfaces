from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QLabel, QGridLayout)
from view.presentacionView.TituloApp import tituloApp,descricionApp
from view.loginAplicacion.emailView import get_email_label, get_email_text
from view.loginAplicacion.PasswordView import get_password_label, get_password_text


def layoutLogin():
    layout = QVBoxLayout()
    layout.addWidget(tituloApp())
    layout.addWidget(descricionApp())
    layout.addWidget(get_email_label())
    layout.addWidget(get_email_text())
    layout.addWidget(get_password_label())
    layout.addWidget(get_password_text())
    return layout
