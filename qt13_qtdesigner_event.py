from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QDialog): # QDialog vient de widget.class dans .ui
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('ui/form.ui', self) # Load the .ui file
        self.show() # Show the GUI
        self.textEdit.setText("Hello")
        self.pushButton.clicked.connect(self.button_clicked)

    def button_clicked(self):
        self.textEdit.setText("Clicked")



app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()


