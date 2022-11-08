import sys
from PyQt5.QtWidgets import QApplication, QWidget

# pip install PyQt5

app = QApplication.instance()
if not app:
    app = QApplication(sys.argv)

fen = QWidget()

# on donne un titre à la fenêtre
fen.setWindowTitle("Premiere fenetre")

# on fixe la taille de la fenêtre
fen.resize(500,250)

# on fixe la position de la fenêtre
fen.move(300,50)

fen.show()

app.exec_()