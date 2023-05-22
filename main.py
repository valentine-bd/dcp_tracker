"""Importation des modules"""
from dcp_tracker.dcp import Dcp
from dcp_tracker.search import search_in_csv
from dcp_tracker.read import read, read_all

def main():
    """Choix des operations"""
    print("===MENU===")
    print("Lire le fichier entier : tapez 1")

    print("Ajouter un dcp : tapez 2")
    print("Rechercher un dcp : tapez 3")

    choix = input("Votre choix :")

    match choix:
        case "1":
            read_all()
        case "2":
            dcp = Dcp()
            dcp.get_dcp()
            dcp.search_num()
            dcp.write()
        case "3":
            data = search_in_csv()
            read(data)
        case _:
            print("Saisie invalide")

if __name__ == "__main__":
    main()
