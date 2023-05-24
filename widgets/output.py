"""Importation des modules"""
import tkinter as tk
from tkinter import ttk
from dcp_tracker.read import read_all

class Output(tk.Frame, tk.Canvas, ttk.Scrollbar):
    """Widget d'affichage"""
    def __init__(self, root):
        super().__init__(root)
        self.create_gui(root)

    def create_gui(self,root):
        """Creer le widget d'affichage"""
        frame_test = tk.Frame(root)
        self.canva = tk.Canvas(frame_test, scrollregion=(0,0,0,1500), bg='white'
        , width=400, height=600)
        self.canva.pack(padx=5, pady=5)
        frame_test.pack(pady=20)

        self.canva.grid(row=0,column=0)

        yscroll=ttk.Scrollbar(frame_test, orient="vertical")
        yscroll.grid(row=0, column=1, sticky=tk.S+tk.N)
        yscroll["command"]=self.canva.yview
        self.canva['yscrollcommand']=yscroll.set

        self.id_text = self.canva.create_text(125,650,text='test')

        btn_modifier = tk.Button(root, text='afficher la bdd complete',command=self.afficher)
        btn_modifier.pack()

    def afficher(self):
        """Fonction liee au bouton d'affichage"""
        output = read_all()
        self.canva.itemconfigure(self.id_text, text=output)
