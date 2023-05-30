"""Permet l'utilisation d'un dossier csv"""
import csv
from dcp_tracker.read import read

def copy_csv(origin_file, copy_file):
    with open(origin_file, 'r', encoding='utf-8') as origin:
        reader = csv.reader(origin, delimiter=',')
        with open(copy_file, 'w', encoding='utf-8') as copy:
            writer = csv.writer(copy, delimiter=',')
            for ligne in reader:
                writer.writerow(ligne)

def search_in_csv(search_item):
    """Recherche a partir d'un item mentionne dans le fichier .csv"""
    exist = False
    found = []
    with open('csv/test.csv', 'r', encoding='utf-8') as test_csv:

        reader = csv.reader(test_csv, delimiter=',')

        for ligne in reader:
            for item in ligne:
                if item == search_item:
                    found.append(ligne)
                    exist = True
                    break
                else:
                    continue

    if exist == False:
        print("Aucune correspondance trouvée")

    return found

def delete_in_csv(search_item):
    """Supprime une ligne du fichier csv a partir d'un item"""
    exist = False
    with open('csv/test.csv', "r", encoding='utf-8') as read_csv:
        reader = csv.reader(read_csv, delimiter=',')
        with open('csv/test_new.csv', "w", encoding='utf-8') as write_csv:
            writer = csv.writer(write_csv, delimiter=',')
            for ligne in reader:
                search_state = 0
                for item in ligne:
                    if item == search_item:
                        search_state = 1
                        exist = True
                        break
                if search_state == 0:
                    writer.writerow(ligne)

    copy_csv('csv/test_new.csv', 'csv/test.csv')
    if exist == False:
        print("Aucune correspondance trouvée")

