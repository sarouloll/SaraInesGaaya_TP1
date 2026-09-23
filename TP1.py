import sys
import json
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidget,
    QTableWidgetItem
)

json_file = sys.argv[1]
print(json_file)

try:
    file = open(json_file)
    data = json.load(file)
    print(type(data))
except:
    print(f"Could not load data from {json_file}")

#Récupération de mes données
for i in data:
    print("Keys\n")
    for k in i.keys():
        print(f"        - {k}")
    print("\n")
    print("Values\n")
    for v in i.values():
        print(f"        - {v}")
    print("\n")
    print("Items\n")
    for e in i.items():
        print(f"        - {e}")
    print("\n")



#création d'une interface
app = QApplication([])

#Configuration de l'interface du tableau visuel
tableau = QTableWidget()
tableau.setRowCount(len(data))
tableau.setColumnCount(6)
tableau.setHorizontalHeaderLabels(["id", "nom", "categorie", "format", "polygones", "statut"])


#Affichage des données
for i in range(len(data)):
    item = data[i]
    tableau.setItem(i, 0, QTableWidgetItem(item["id"]))
    tableau.setItem(i, 1, QTableWidgetItem(item["nom"]))
    tableau.setItem(i, 2, QTableWidgetItem(item["categorie"]))
    tableau.setItem(i, 3, QTableWidgetItem(item["format"]))
    tableau.setItem(i, 4, QTableWidgetItem(item['polygones']))
    tableau.setItem(i, 5, QTableWidgetItem(item["statut"]))


window = QMainWindow();
window.setCentralWidget(tableau)
window.show()
sys.exit(app.exec())
