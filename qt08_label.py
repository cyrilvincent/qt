import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel


class Fenetre(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.n = 0  # attribut pour compter le nombre d'appui sur le bouton

        # création du bouton
        self.bouton = QPushButton("mon bouton avec une gestion d'appui")
        # on connecte le signal "clicked" à la méthode "appui_bouton"
        self.bouton.clicked.connect(self.appui_bouton)

        # création de l'étiquette
        self.label = QLabel("appui n = " + str(self.n))

        # mise en place du gestionnaire de mise en forme
        layout = QVBoxLayout()
        layout.addWidget(self.bouton)
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.setWindowTitle("Ma fenetre")

    # on définit une méthode à connecter au signal envoyé
    def appui_bouton(self):
        # on incrémente l'attribut "n" de 1
        self.n = self.n + 1
        # on utilise la méthode "setText" de QLabel pour fixer le texte
        self.label.setText("appui n = " + str(self.n))


app = QApplication.instance()
if not app:
    app = QApplication(sys.argv)

fen = Fenetre()
fen.show()

app.exec_()