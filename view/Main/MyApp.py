import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QLabel)

class Aplicacion(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RENTACAR")
        self.setFixedSize(800,600)

if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = Aplicacion()
    ventana.show()
    aplicacion.exec()