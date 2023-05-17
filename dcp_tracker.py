"""Permet l'utilisation d'un dossier csv"""
import csv

class Dcp:
    """Classe DCP"""
    def __init__(self, id = "", titre = "", dateArrivee = "", labo = "", distrib = "", num = ""):
        """Initialisation"""
        self.id = id
        self.titre = titre
        self.dateArrivee = dateArrivee
        self.labo = labo
        self.distrib = distrib
        self.num = num

    def write(self):
        """Ecriture dans le csv"""
        with open('test.csv', 'a') as test_csv:

            writer = csv.writer(test_csv, delimiter=',')
            ligne = [self.id, self.titre, self.dateArrivee, self.labo, self.distrib, self.num]

            writer.writerow(ligne)

    def convert(self, fromCsv):
        """Conversion du csv a un objet Dcp"""
        self.id = fromCsv[0]
        self.titre = fromCsv[1]
        self.dateArrivee = fromCsv[2]
        self.labo = fromCsv[3]
        self.distrib = fromCsv[4]
        self.num = fromCsv[5]

    def get_dcp(self):
        """Obtient un objet Dcp a partir de la console"""
        self.id = input("ID : ")
        self.titre = input("titre : ")
        self.dateArrivee = input("date : ")
        self.labo = input("labo : ")
        self.distrib = input("distrib : ")

    def search_num(self):
        """Verifie si le num du distrib existe dans le fichier distrib.csv"""
        print("Recherche le num  dans la base de donnée... ")

        with open('distribs.csv', '+a') as distribs_csv:

            reader = csv.reader(distribs_csv, delimiter=",")
            searchState = 0
            distrib = []

            for ligne in reader:
                if ligne[0] == self.distrib:
                    distrib = ligne
                    print("Numéro correspondant a", distrib[0], "trouvé :", distrib[1])
                    searchState = 1
                    self.num = distrib[1]

            if searchState == 0:
                self.num = input("Aucune correspondance, entrez un numero de telephone : ")
                nouveau = [self.distrib, self. num]
                writer = csv.writer(distribs_csv, delimiter=',')
                writer.writerow(nouveau)



    def display(self):
        """Affiche le contenu d'un objet Dcp"""
        print("------------------------")
        print("Titre : ", self.titre)
        print("date d'entree : ", self.dateArrivee)
        print("Labo : ", self.labo)
        print("Distrib : ", self.distrib)
        print("Num distrib : ", self.num)
        print("------------------------")


def search_in_csv():
    """Recherche a partir d'un item"""
    searchItem = input("item a rechercher : ")
    searchState = 0
    found = []
    with open('test.csv') as test_csv:

        reader = csv.reader(test_csv, delimiter=',')

        for ligne in reader:
            for item in ligne:
                if item == searchItem:
                    found.append(ligne)
                    searchState = 1
                else:
                    continue

    if searchState == 0:
        print("Aucune correspondance trouvée")

    return found

def read(list):
    """Lit la liste en argument en la convertissant en objet Dcp"""
    for csvItem in list:
        dcp = Dcp()
        dcp.convert(csvItem)
        dcp.display()

def read_all():
    """Lit la totalite du fichier csv"""
    with open('test.csv') as test_csv:

        reader = csv.reader(test_csv, delimiter=',')

        for ligne in reader:
            print(ligne)

def app():
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
            list = search_in_csv()
            read(list)
        case _:
            print("Saisie invalide")

app()
    