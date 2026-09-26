
import sys
import json
from pathlib import Path
from PySide6.QtCore import Qt
#from PySide6.QtGui import QGuiApplication, Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidget,
    QTableWidgetItem,
    QLineEdit,
    QWidget,
    QVBoxLayout,
    QCompleter
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
window = QMainWindow();
window.setWindowTitle("Visualisation données")
window.resize(1050, 600)

container = QWidget()
layout = QVBoxLayout(container)


#Affichage de la barre de recherche
searchbar = QLineEdit()
searchbar.setPlaceholderText("Search...")
layout.addWidget(searchbar)





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
elif choice in ["large", "Large"]:
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

else:
    print("Please choose between Small or Large data")


# noms = [(item["nom"]), (item["id"]), (item["categorie"]), (item["format"]), (str(item['polygones'])), (item["statut"]), (item["auteur"]), (str(item['date_creation'])), (str(item["prix"])), (str(item["taille_fichier"]))
noms = [str(item["nom"])
    for item in (data_small if choice.lower() == "small" else data_large)]

completer = QCompleter(searchbar)
completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
searchbar.setCompleter(completer)    

# def update_display(self, text):
#     search = text.strip().casefold()
#     for widget in self.widgets:
#         if widget.name.casefold().startswith(search):
#             widget.show()
#         else:
#                 widget.hide()

def update_display(text):
    search = text.strip().casefold()

    for row in range(tableau.rowCount()):
        item = tableau.item(row, 1)

        if item is not None and search in item.text().casefold():
            tableau.setRowHidden(row, False)
        else:
            tableau.setRowHidden(row, True)

#Met à jour l'affichage quand un charactère est inscrit dans la barre de recherche
searchbar.textChanged.connect(update_display)

layout.addWidget(tableau)
window.setCentralWidget(container)
window.show()
sys.exit(app.exec())    

#liens utiles
#https://doc.qt.io/qtforpython-6/tutorials/basictutorial/tablewidget.html
#https://www.pythontutorial.net/pyqt/pyqt-qtablewidget/
#https://www.pythonguis.com/tutorials/pyside6-widget-search-bar/

