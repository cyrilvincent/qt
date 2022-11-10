# pip install pyqt5-tools
# Python 3.10 non supporté
# C:\Users\conta\AppData\Local\Programs\Python\Python39\Lib\site-packages\qt5_applications\Qt\bin
# Egalement dans Qt/bin
# Sinon download : https://www.qt.io/download-qt-installer
# 2 solutions :
# Créer le .py
# Créer le .ui
from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QDialog): # QDialog vient de widget.class dans .ui
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('ui/form.ui', self) # Load the .ui file
        self.show() # Show the GUI

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()


