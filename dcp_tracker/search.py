"""Permet l'utilisation d'un dossier csv"""
import csv

def search_in_csv():
    """Recherche a partir d'un item mentionne dans le fichier .csv"""
    search_item = input("item a rechercher : ")
    search_state = 0
    found = []
    with open('csv/test.csv', 'r', encoding='utf-8') as test_csv:

        reader = csv.reader(test_csv, delimiter=',')

        for ligne in reader:
            for item in ligne:
                if item == search_item:
                    found.append(ligne)
                    search_state = 1
                    break
                else:
                    continue

    if search_state == 0:
        print("Aucune correspondance trouvée")

    return found
