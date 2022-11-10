from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QStandardItemModel, QStandardItem

import media
import sys
import settings

class Ui(QtWidgets.QMainWindow):



    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('ui/main.ui', self) # Load the .ui file
        self.show() # Show the GUI
        self.parserButton.clicked.connect(self.parser_clicked)
        self.parser = media.BookCsvParser(settings.book_path)

    def parser_clicked(self):
        books = self.parser.parse()
        model = QStandardItemModel()
        self.listView.setModel(model)
        for b in books:
            item = QStandardItem(b.title)
            model.appendRow(item)




app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()