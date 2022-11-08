import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QCheckBox


class Fenetre(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # création de la case à cocher
        self.case = QCheckBox("Voici ma premiere case a cocher")

        # on connecte le signal "stateChanged" à la méthode "etat_change"
        self.case.stateChanged.connect(self.etat_change)

        # création du gestionnaire de mise en forme
        layout = QVBoxLayout()
        # ajout de la case à cocher au gestionnaire de mise en forme
        layout.addWidget(self.case)
        # on fixe le gestionnaire de mise en forme de la fenêtre
        self.setLayout(layout)

        self.setWindowTitle("Ma fenetre")

    # on définit une méthode à connecter au signal envoyé
    def etat_change(self):
        print("action sur la case")
        if self.case.checkState() == Qt.Checked:
            print("coche")
        else:
            print("decoche")


app = QApplication.instance()
if not app:
    app = QApplication(sys.argv)

fen = Fenetre()
fen.show()

app.exec_()