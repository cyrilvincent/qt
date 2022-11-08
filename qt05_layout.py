import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class Fenetre(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # creation du premier bouton
        self.bouton1 = QPushButton("OK 1")
        # creation du deuxieme bouton
        self.bouton2 = QPushButton("OK 2")

        # creation du gestionnaire de mise en forme
        layout = QVBoxLayout()
        # ajout du premier bouton au gestionnaire de mise en forme
        layout.addWidget(self.bouton1)
        # ajout du deuxieme bouton au gestionnaire de mise en forme
        layout.addWidget(self.bouton2)
        # on fixe le gestionnaire de mise en forme de la fenetre
        self.setLayout(layout)

        self.setWindowTitle("Ma fenetre")


app = QApplication.instance()
if not app:
    app = QApplication(sys.argv)

fen = Fenetre()
fen.show()

app.exec_()