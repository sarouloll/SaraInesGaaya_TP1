# Correction
import sys
import json
from pathlib import Path
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidget,
    QTableWidgetItem,
    QLineEdit,
    QWidget,
    QVBoxLayout,
    QFileDialog
)

app = QApplication([])

#Ouverture de l'explorateur de fichier permettant de sélectionner un JSON
json_path, _ = QFileDialog.getOpenFileName(None, "Selectionner le fichier JSON", 
                                           "","Fichiers JSON (*.json)")

path = Path(json_path)

# Message d'erreur si utilisateur annule la sélection
if not json_path:
    print("Aucun fichier selectionné.")
    sys.exit()

# Messgae d'erreur si le chemin est incorrect/inexistant
if not path.exists():
    print("Erreur, fichier inexistant.")
    sys.exit()

# Ouverture et lecture du fichier 
# Interprétation du fichier
try:
    with path.open("r", encoding="utf-8") as fichier:
        data = json.load(fichier)

# Erreur si incapable de lire le fichier
except json.JSONDecodeError:
    print("Erreur, ceci n'est pas un JSON fonctionnel.")
    sys.exit()

# Message d'erreur pour tout autre problème 
except Exception as j:
    print(f"Erreur, ouverture du fichier {j} impossible")
    sys.exit()

# Va chercher le nom du fichier
# Convertis tout les lettres en minuscules
filename = path.stem.lower()

# Vérifie/cherche le mot "small" dans le fichier
if "small" in filename:
    choice = "small"

# Sinon, vérifie/cherche avec le mot "large"
elif "large" in filename:
    choice = "large"

# Message d'erreur
else:
    print("Erreur, le fichier doit contenir 'large' ou 'small' pour poursuivre")
    sys.exit()

#Création de l'interface principale
window = QMainWindow();
window.setWindowTitle("Visualisation données")
window.resize(1050, 600)

# Création d'un container pour mettre mes éléments (tableau, barre de recherche)
container = QWidget()
# Met les éléments dans une interface verticale
layout = QVBoxLayout(container)

#Affichage de la barre de recherche
searchbar = QLineEdit()
searchbar.setPlaceholderText("Search...")
layout.addWidget(searchbar)


#Configuration de l'interface du tableau visuel (SMALL)
if choice == "small":
    tableau = QTableWidget()
    tableau.setRowCount(len(data))
    tableau.setColumnCount(6)
    # Titres des en-têtes
    tableau.setHorizontalHeaderLabels([
        "id", 
        "nom", 
        "categorie", 
        "format", 
        "polygones", 
        "statut"
    ])

    # Affichage des données (SMALL)
    for i in range(len(data)):
        item = data[i]
        tableau.setItem(i, 0, QTableWidgetItem(item["id"]))
        tableau.setItem(i, 1, QTableWidgetItem(item["nom"]))
        tableau.setItem(i, 2, QTableWidgetItem(item["categorie"]))
        tableau.setItem(i, 3, QTableWidgetItem(item["format"]))
        tableau.setItem(i, 4, QTableWidgetItem(str(item['polygones'])))
        tableau.setItem(i, 5, QTableWidgetItem(item["statut"]))

    # Tri ordre croissant/décroissant
    tableau.setSortingEnabled(True)


# Configuration de l'interface du tableau visuel (LARGE)
elif choice == "large":
    tableau = QTableWidget()
    tableau.setRowCount(len(data))
    tableau.setColumnCount(10)
    # Titres des en-têtes
    tableau.setHorizontalHeaderLabels([
        "id", 
        "nom", 
        "categorie", 
        "format", 
        "polygones", 
        "statut", 
        "auteur", 
        'date_creation', 
        "prix", 
        "taille_fichier"
    ])

    # Affichage des données (LARGE)
    for e in range(len(data)):
        item = data[e]
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

    # Tri ordre croissant/décroissant
    tableau.setSortingEnabled(True)


# Permet de rechercher mes valeurs dans tout les colonnes et rangées du tableau de données
def update_display(text):
    search = text.strip().casefold()

    # Cherche dans les rangées et ensuite dans les colonnes
    for row in range(tableau.rowCount()):
        found = False

        for column in range(tableau.columnCount()):
            item = tableau.item(row, column)

            # Permet de rechercher le texte peu importe son emplacement et les majuscules/minuscules
            if item is not None and search in item.text().casefold():
                found = True
                break

        # Cache les valeurs qui ne sont pas recherchées
        tableau.setRowHidden(row, not found)


# Met à jour l'affichage quand un charactère est inscrit dans la barre de recherche
searchbar.textChanged.connect(update_display)

layout.addWidget(tableau)
window.setCentralWidget(container)
window.show()
sys.exit(app.exec())    
