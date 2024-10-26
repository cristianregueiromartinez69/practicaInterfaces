from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QLabel, QGridLayout)
from view.presentacionView.TituloApp import tituloApp,descricionApp


def layoutLogin():
    layout = QVBoxLayout()
    layout.addWidget(tituloApp())
    layout.addWidget(descricionApp())
    return layout
