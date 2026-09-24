
import sys
import json
from pathlib import Path
from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication, Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidget,
    QTableWidgetItem,
    QLineEdit,
    QWidget,
    QVBoxLayout,
)

# json_file = sys.argv[0]
# print(json_file)


#Find json files
path = Path(__file__).parent / "data_small.json"
path_large = Path(__file__).parent / "data_large.json"

with path.open("r", encoding="utf-8") as fichier:
    data_small = json.load(fichier)

with path_large.open("r", encoding="utf-8") as fichier:
    data_large = json.load(fichier)



# def main_window(self):
#     main_window = QMainWindow()
#     self.setGeometry(600, 100, 800, 600)

#Question déterminant quel type de tableau sera affiché 
choice = str(input("What type of data would you like to sort (large or small) ?"))

#region TEST
# try:
#     file = open(json_file)
#     data = json.load(file)
#     print(type(data))
# except:
#     print(f"Could not load data from {json_file}")


# #Récupération de mes données
# for i in data_small:
#     print("Keys\n")
#     for k in i.keys():
#         print(f"        - {k}")
#     print("\n")
#     print("Values\n")
#     for v in i.values():
#         print(f"        - {v}")
#     print("\n")
#     print("Items\n")
#     for e in i.items():
#         print(f"        - {e}")
#     print("\n")
#endregion

##A FAIRE
#json.decoder.JSONDecodeError

#création d'une interface
app = QApplication([])


#Configuration de l'interface du tableau visuel (SMALL)
if choice in ["small", "Small"]:
    tableau = QTableWidget()
    tableau.setRowCount(len(data_small))
    tableau.setColumnCount(6)
    tableau.setHorizontalHeaderLabels(["id", "nom", "categorie", "format", "polygones", "statut"])


    #Affichage des données (SMALL)
    for i in range(len(data_small)):
        item = data_small[i]
        tableau.setItem(i, 0, QTableWidgetItem(item["id"]))
        tableau.setItem(i, 1, QTableWidgetItem(item["nom"]))
        tableau.setItem(i, 2, QTableWidgetItem(item["categorie"]))
        tableau.setItem(i, 3, QTableWidgetItem(item["format"]))
        tableau.setItem(i, 4, QTableWidgetItem(str(item['polygones'])))
        tableau.setItem(i, 5, QTableWidgetItem(item["statut"]))

    #Tri ordre croissant/décroissant
    tableau.setSortingEnabled(True)



#Configuration de l'interface du tableau visuel (LARGE)
if choice in ["large", "Large"]:
    tableau = QTableWidget()
    tableau.setRowCount(len(data_large))
    tableau.setColumnCount(10)
    tableau.setHorizontalHeaderLabels(["id", "nom", "categorie", "format", "polygones", "statut", "auteur", 'date_creation', "prix", "taille_fichier"])

    for e in range(len(data_large)):
        item = data_large[e]
        tableau.setItem(e, 0, QTableWidgetItem(item["id"]))
        tableau.setItem(e, 1, QTableWidgetItem(item["nom"]))
        tableau.setItem(e, 2, QTableWidgetItem(item["categorie"]))
        tableau.setItem(e, 3, QTableWidgetItem(item["format"]))
        tableau.setItem(e, 4, QTableWidgetItem(str(item['polygones'])))
        tableau.setItem(e, 5, QTableWidgetItem(item["statut"]))
        tableau.setItem(e, 6, QTableWidgetItem(item["auteur"]))
        tableau.setItem(e, 7, QTableWidgetItem(str(item['date_creation'])))
        tableau.setItem(e, 8, QTableWidgetItem(str(item["prix"])))
        tableau.setItem(e, 9, QTableWidgetItem(str(item["taille_fichier"])))

    #Tri ordre croissant/décroissant
    tableau.setSortingEnabled(True)


#Search engine
# [QTableWidgetItem] = QTableWidget.findItems(str, Qt.MatchFlags)

# self.query = QLineEdit()
# self.query.setPlaceholderText("Search...")
# self.query.textChanged.connect(self.search)

# def search(self, s):
#         # clear current selection.
#         self.table.setCurrentItem(None)

#         if not s:
#             # Empty string, don't search.
#             return

#         matching_items = self.table.findItems(s, Qt.MatchContains)
#         if matching_items:
#             # we have found something
#             item = matching_items[0]  # take the first
#             self.table.setCurrentItem(item)


####try n2 :(

# searchbar = QLineEdit.textChanged(placeholderText = "Search...")
# ####searchbar.setPlaceholderText ("Search...")
# container = QWidget()
# container_layout = QVBoxLayout()
# container.addWidget(searchbar)


window = QMainWindow();
window.setCentralWidget(tableau)
window.show()
sys.exit(app.exec())

#liens utiles
#https://doc.qt.io/qtforpython-6/tutorials/basictutorial/tablewidget.html
#https://www.pythontutorial.net/pyqt/pyqt-qtablewidget/
#https://www.pythonguis.com/tutorials/pyside6-widget-search-bar/

