"""Importation des modules"""
import tkinter as tk

from widgets.ajout_dcp import Input

from dcp_tracker.search import search_in_csv
from dcp_tracker.read import read

class Search():
    """Widget de recherche"""
    def __init__(self, root, output):
        self.create_gui(root)
        self.output = output

    def create_gui(self, root):
        """Creer le widget de recherche"""
        search_item =tk.LabelFrame(root, text="Rechercher par item")
        search_item.pack()

        self.item = Input(search_item, "Rechercher :")

        search = tk.Button(search_item
                           , text="Rechercher", command=self.display_research)
        search.pack(side="bottom", pady=10)

    def display_research(self):
        """Fonction liee au bouton d'affichage"""
        word = self.item.get_input()
        print(word)
        output_text = read(search_in_csv(word))
        self.output.canva.itemconfigure(self.output.id_text, text=output_text)
