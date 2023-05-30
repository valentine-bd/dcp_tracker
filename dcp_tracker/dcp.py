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
        with open('csv/test.csv', 'a', encoding='utf-8') as test_csv:

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

        with open('csv/distribs.csv', 'r', encoding='utf-8') as distribs_csv:

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

        with open('csv/distribs.csv', 'a', encoding='utf-8') as distribs_csv:

            if search_state == 0:
                self.num = input("Aucune correspondance, entrez un numero de telephone : ")
                nouveau = [self.distrib, self. num]
                writer = csv.writer(distribs_csv, delimiter=',')
                writer.writerow(nouveau)

    def console_display(self):
        """Affiche le contenu d'un objet Dcp dans la console"""
        print("------------------------")
        print("Titre : ", self.titre)
        print("date d'entree : ", self.date_arrivee)
        print("Labo : ", self.labo)
        print("Distrib : ", self.distrib)
        print("Num distrib : ", self.num)
        print("------------------------")

    def window_display(self):
        """Retourne une chaine de caractere permettant l'affichage sur fenetre"""
        output = "Titre : " + self.titre + " \nDate d'entree : " + self.date_arrivee + " \nLabo : " + self.labo + " \nDistributeur : " + self.distrib + " \nNumero du distributeur : " + self.num
        return output
