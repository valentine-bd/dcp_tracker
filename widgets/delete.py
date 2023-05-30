"""Importation des modules"""
import tkinter as tk

from widgets.ajout_dcp import Input
from dcp_tracker.search import delete_in_csv

class Delete():
    """Widget de recherche"""
    def __init__(self, root):
        self.create_gui(root)

    def create_gui(self, root):
        """Creer le widget de suppresion"""
        search_item =tk.LabelFrame(root, text="Supprimer par item")
        search_item.pack()

        self.item = Input(search_item, "Item :")

        search = tk.Button(search_item, text="Supprimer", command=self.delete_research)
        search.pack(side="bottom", pady=10)

    def delete_research(self):
        word = self.item.get_input()
        print(word)
        delete_in_csv(word)