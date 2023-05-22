"""Permet l'utilisation d'un dossier csv"""
import csv

class Dcp:
    """Classe DCP"""
    def __init__(self, ref = "", titre = "", date_arrivee = "", labo = "", distrib = "", num = ""):
        """Initialisation"""
        self.ref = ref
        self.titre = titre
        self.date_arrivee = date_arrivee
        self.labo = labo
        self.distrib = distrib
        self.num = num

    def write(self):
        """Ecriture dans le csv"""
        with open('test.csv', 'a', encoding='utf-8') as test_csv:

            writer = csv.writer(test_csv, delimiter=',')
            ligne = [self.ref, self.titre, self.date_arrivee, self.labo, self.distrib, self.num]

            writer.writerow(ligne)

    def convert(self, from_csv):
        """Conversion d'une ligne du fichier csv vers un objet Dcp"""
        self.ref = from_csv[0]
        self.titre = from_csv[1]
        self.date_arrivee = from_csv[2]
        self.labo = from_csv[3]
        self.distrib = from_csv[4]
        self.num = from_csv[5]

    def get_dcp(self):
        """Obtient un objet Dcp a partir de la console"""
        self.ref = input("ID : ")
        self.titre = input("titre : ")
        self.date_arrivee = input("date : ")
        self.labo = input("labo : ")
        self.distrib = input("distrib : ")

    def search_num(self):
        """Verifie si le num du distrib existe dans le fichier distrib.csv"""
        print("Recherche le num  dans la base de donnée... ")

        with open('distribs.csv', 'r', encoding='utf-8') as distribs_csv:

            reader = csv.reader(distribs_csv, delimiter=",")
            search_state = 0
            distrib = []

            for ligne in reader:
                if ligne[0] == self.distrib:
                    distrib = ligne
                    print("Numéro correspondant a", distrib[0], "trouvé :", distrib[1])
                    search_state = 1
                    self.num = distrib[1]
                    break

        with open('distribs.csv', 'a', encoding='utf-8') as distribs_csv:

            if search_state == 0:
                self.num = input("Aucune correspondance, entrez un numero de telephone : ")
                nouveau = [self.distrib, self. num]
                writer = csv.writer(distribs_csv, delimiter=',')
                writer.writerow(nouveau)



    def display(self):
        """Affiche le contenu d'un objet Dcp dans la console"""
        print("------------------------")
        print("Titre : ", self.titre)
        print("date d'entree : ", self.date_arrivee)
        print("Labo : ", self.labo)
        print("Distrib : ", self.distrib)
        print("Num distrib : ", self.num)
        print("------------------------")


def search_in_csv():
    """Recherche a partir d'un item mentionne dans le fichier .csv"""
    search_item = input("item a rechercher : ")
    search_state = 0
    found = []
    with open('test.csv', 'r', encoding='utf-8') as test_csv:

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

def read(data):
    """Lit la liste en argument en la convertissant en objet Dcp et l'affichant dans la console"""
    for csv_item in data:
        dcp = Dcp()
        dcp.convert(csv_item)
        dcp.display()

def read_all():
    """Lit la totalite du fichier csv et l'affiche dans la console"""
    with open('test.csv', 'r', encoding='utf-8') as test_csv:

        reader = csv.reader(test_csv, delimiter=',')
        read(reader)

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
            data = search_in_csv()
            read(data)
        case _:
            print("Saisie invalide")

app()
    