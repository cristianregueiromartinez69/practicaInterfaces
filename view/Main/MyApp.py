import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QLabel)
from view.loginAplicacion.LoginView import layoutLogin

class Aplicacion(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RENTACAR")
        self.setFixedSize(800,600)
        container = QWidget()
        container.setLayout(layoutLogin())
        self.setCentralWidget(container)

if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = Aplicacion()
    ventana.show()
    aplicacion.exec()