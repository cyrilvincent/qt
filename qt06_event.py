import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class Fenetre(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # creation du bouton
        self.bouton = QPushButton("OK")

        # on connecte le signal "clicked" a la methode appui_bouton
        self.bouton.clicked.connect(self.appui_bouton)

        # creation du gestionnaire de mise en forme
        layout = QVBoxLayout()
        layout.addWidget(self.bouton)
        self.setLayout(layout)

        self.setWindowTitle("Ma fenetre")

    def appui_bouton(self):
        print("Appui sur le bouton")


app = QApplication.instance()
if not app:
    app = QApplication(sys.argv)

fen = Fenetre()
fen.show()

app.exec_()