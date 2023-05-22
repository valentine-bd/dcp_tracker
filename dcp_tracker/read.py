"""Permet l'utilisation d'un dossier csv et la classe Dcp"""
import csv
from dcp_tracker.dcp import Dcp

def read(data):
    """Lit la liste en argument en la convertissant en objet Dcp et l'affichant dans la console"""
    for csv_item in data:
        dcp = Dcp()
        dcp.convert(csv_item)
        dcp.display()

def read_all():
    """Lit la totalite du fichier csv et l'affiche dans la console"""
    with open('csv/test.csv', 'r', encoding='utf-8') as test_csv:

        reader = csv.reader(test_csv, delimiter=',')
        read(reader)
