import sys
from PyQt5.QtWidgets import QApplication, QPushButton

app = QApplication.instance()
if not app:
    app = QApplication(sys.argv)

bouton = QPushButton("OK")
bouton.show()

app.exec_()