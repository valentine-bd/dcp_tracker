"""Importation des modules"""
import tkinter as tk
from tkinter import messagebox

from dcp_tracker.dcp import Dcp

class Input():
    """Widget d'entree de variable"""
    def __init__(self, root, text_label):
        self.create_gui(root, text_label)

    def create_gui(self, root, text_label):
        """Cree le widget d'entree de variable"""
        frame = tk.Frame(root)
        label = tk.Label(frame, text=text_label)
        self.input = tk.Entry(frame, width=30)
        label.pack(side="left", padx=10)
        self.input.pack(side="right", padx=10)
        frame.pack(fill="both",expand="yes", pady=10)

    def get_input(self):
        """Obtient les valeurs contenues dans les Entry"""
        value = self.input.get()
        return value



class AjoutDcp(tk.LabelFrame, tk.Button):
    """Widjet ajout de Dcp dans la base de donnee"""
    def __init__(self, root):
        super().__init__(root)
        self.create_gui(root)

    def create_gui(self, root):
        """Cree le widget recherche de Dcp"""

        # Ajouter un DCP dans la base de donnee
        ajout_dcp = tk.LabelFrame(root, text="Ajout de dcp dans la base de donnee")
        ajout_dcp.pack(padx=10, pady=10)

        self.titre_input = Input(ajout_dcp, "Titre :")
        self.date_arrivee_input = Input(ajout_dcp, "Date d'arrivee :")
        self.labo_input = Input(ajout_dcp, "Labo :")
        self.distributeur_input = Input(ajout_dcp, "Distributeur :")
        self.num_input = Input(ajout_dcp, "Numero de distributeur :")

        #Bouton d'ajout
        ajout=tk.Button(ajout_dcp, text="Ajouter", command=self.get_full_input)
        ajout.pack(side="bottom", pady=10)

    def get_full_input(self):
        """Fonction liee au bouton ajout de l'interface"""
        dcp = Dcp()
        dcp.titre = self.titre_input.get_input()
        dcp.date_arrivee = self.date_arrivee_input.get_input()
        dcp.labo = self.labo_input.get_input()
        dcp.distrib = self.distributeur_input.get_input()
        dcp.num = self.num_input.get_input()
        yes = messagebox.askyesno("Confirmation d'ajout",
        "Confirmez vous l'ajout de ce DCP à la base de donnée")

        if yes:
            dcp.write()
            print("Ajout de :")
            dcp.console_display()
        else:
            pass
