from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QLabel, QGridLayout)


def tituloApp():
    titulo = QLabel("RENTACAR")
    return titulo

def descricionApp():
    descripcion = QLabel("¡Alquile nuestros vehículos al mejor precio!")
    return descripcion