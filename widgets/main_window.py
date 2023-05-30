"""Importation des modules"""
import tkinter as tk

from widgets.ajout_dcp import AjoutDcp
from widgets.output import Output
from widgets.search import Search
from widgets.delete import Delete

class MainWindow():
    """Classe pilotant l'aspect de la fenetre principale"""
    def __init__(self):
        self.create_window()

    def create_window(self):
        """Gestion de la fenetre"""
        window = tk.Tk()
        window.geometry("1280x720")
        window.title("Dcp Tracker")

        frame2 =tk.Frame(window)
        output = Output(frame2)
        frame2.pack(side=tk.RIGHT)

        frame1 = tk.Frame(window)
        AjoutDcp(frame1)
        Search(frame1, output)
        Delete(frame1)
        frame1.pack(side=tk.LEFT)

        window.mainloop()
        