"""Importation des modules"""
import tkinter as tk

from dcp_tracker.dcp import Dcp

class AjoutDcp(tk.Frame, tk.LabelFrame, tk.Entry, tk.Label, tk.Button, Dcp):
    """Widjet ajout de Dcp dans la base de donnee"""
    def __init__(self, window):
        super().__init__(window)
        self.create_gui(window)

    def create_gui(self, window):
        """Creer le widget recherche de Dcp"""

        # Ajouter un DCP dans la base de donnee
        ajout_dcp = tk.LabelFrame(window, text="Ajout de dcp dans la base de donnee")
        ajout_dcp.pack(padx=10, pady=10)

        #Titre
        frame1 = tk.Frame(ajout_dcp)
        titre_label = tk.Label(frame1, text="Titre :")
        self.titre_input = tk.Entry(frame1, width=30)
        titre_label.pack(side="left", padx=10)
        self.titre_input.pack(side="right", padx=10)
        frame1.pack(fill="both",expand="yes", pady=10)

        #Date
        frame2 = tk.Frame(ajout_dcp)
        date_arrivee_label = tk.Label(frame2, text="Date d'arrivee :")
        self.date_arrivee_input = tk.Entry(frame2, width=30)
        date_arrivee_label.pack(side="left", padx=10)
        self.date_arrivee_input.pack(side="right", padx=10)
        frame2.pack(fill="both",expand="yes", pady=10)

        #Labo
        frame3 = tk.Frame(ajout_dcp)
        labo_label = tk.Label(frame3, text="Labo :")
        self.labo_input = tk.Entry(frame3, width=30)
        labo_label.pack(side="left", padx=10)
        self.labo_input.pack(side="right", padx=10)
        frame3.pack(fill="both",expand="yes", pady=10)

        #Distributeur
        frame4 = tk.Frame(ajout_dcp)
        distributeur_label = tk.Label(frame4, text="Distributeur :")
        self.distributeur_input = tk.Entry(frame4, width=30)
        distributeur_label.pack(side="left", padx=10)
        self.distributeur_input.pack(side="right", padx=10)
        frame4.pack(fill="both",expand="yes", pady=10)

        #numero distributeur
        frame5 = tk.Frame(ajout_dcp)
        num_label = tk.Label(frame5, text="Numero du distributeur :")
        self.num_input = tk.Entry(frame5, width=30)
        num_label.pack(side="left", padx=10)
        self.num_input.pack(side="right", padx=10)
        frame5.pack(fill="both",expand="yes",pady=10)

        #Bouton d'ajout
        ajout=tk.Button(ajout_dcp, text="Ajouter", command=self.get_dcp_entry)
        ajout.pack(side="bottom", pady=10)

    def get_dcp_entry(self):
        """Fonction liee au bouton ajout de l'interface"""
        dcp = Dcp()
        dcp.titre = self.titre_input.get()
        dcp.date_arrivee = self.date_arrivee_input.get()
        dcp.labo = self.labo_input.get()
        dcp.distrib = self.distributeur_input.get()
        dcp.num = self.num_input.get()
        dcp.write()
