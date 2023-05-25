"""Importation des modules"""
import tkinter as tk

from widgets.ajout_dcp import AjoutDcp
from widgets.output import Output

window = tk.Tk()
#window.geometry("1280x720")
window.title("Dcp Tracker")

AjoutDcp(window)
Output(window)

window.mainloop()
