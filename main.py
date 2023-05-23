"""Importation des modules"""
import tkinter as tk
from widgets.ajout_dcp import AjoutDcp

window = tk.Tk()
window.geometry("1280x720")
window.title("Application test")
AjoutDcp(window)

window.mainloop()
