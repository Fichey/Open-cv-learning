import sys
from PyQt6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        
        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignmentFlag.AlignCenter,
                                     font=QtGui.QFont('Consola', 10))
        
        #making font height and with identical seems to be harder than i thought...
        
        self.layout = QtWidgets.QVBoxLayout(self)
        
        self.layout.addWidget(self.text)

