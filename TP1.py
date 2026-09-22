import sys
import json
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidget
)
print ("Hello world")

#Récupération de mes données




#création d'une interface
app = QApplication([])

#Configuration de l'interface du tableau visuel
tableau = QTableWidget()
tableau.setRowCount(len(data))
tableau.setColumnCount(3)
tableau.setHorizontalHeaderLabels(["Nom", "Taille", "Quantité d'éléments"])

#Affichage des données
for i in range(len(data)):
    item = data[i]
    tableau.setItem(i, 0, QTableWidgetItem(item["Nom"]))
    tableau.setItem(i, 1, QTableWidgetItem(item["Taille"]))
    tableau.setItem(i, 2, QTableWidgetItem(item["Quantité d'éléments"]))


#
window = QMainWindow();
window.setCentralWidget(tableau)
window.show()
sys.exit(app.exec())
