"""Importation des modules"""
import tkinter as tk

from dcp_tracker.dcp import Dcp

def get_dcp_entry():
    """Fonction liee au bouton ajout de l'interface"""
    dcp.titre = titre_input.get()
    dcp.date_arrivee = date_arrivee_input.get()
    dcp.labo = labo_input.get()
    dcp.distrib = distributeur_input.get()
    dcp.num = num_input.get()
    dcp.write()

dcp = Dcp()
window = tk.Tk()
#window.geometry("1280x720")
window.title("Application test")

# Ajouter un DCP dans la base de donnee
ajout_dcp = tk.LabelFrame(window, text="Ajout de dcp dans la base de donnee")
ajout_dcp.pack(padx=10, pady=10)

#Titre
frame1 = tk.Frame(ajout_dcp)
titre_label = tk.Label(frame1, text="Titre :")
titre_input = tk.Entry(frame1, width=30)
titre_label.pack(side="left", padx=10)
titre_input.pack(side="right", padx=10)
frame1.pack(fill="both",expand="yes", pady=10)

#Date
frame2 = tk.Frame(ajout_dcp)
date_arrivee_label = tk.Label(frame2, text="Date d'arrivee :")
date_arrivee_input = tk.Entry(frame2, width=30)
date_arrivee_label.pack(side="left", padx=10)
date_arrivee_input.pack(side="right", padx=10)
frame2.pack(fill="both",expand="yes", pady=10)

#Labo
frame3 = tk.Frame(ajout_dcp)
labo_label = tk.Label(frame3, text="Labo :")
labo_input = tk.Entry(frame3, width=30)
labo_label.pack(side="left", padx=10)
labo_input.pack(side="right", padx=10)
frame3.pack(fill="both",expand="yes", pady=10)

#Distributeur
frame4 = tk.Frame(ajout_dcp)
distributeur_label = tk.Label(frame4, text="Distributeur :")
distributeur_input = tk.Entry(frame4, width=30)
distributeur_label.pack(side="left", padx=10)
distributeur_input.pack(side="right", padx=10)
frame4.pack(fill="both",expand="yes", pady=10)

#numero distributeur
frame5 = tk.Frame(ajout_dcp)
num_label = tk.Label(frame5, text="Numero du distributeur :")
num_input = tk.Entry(frame5, width=30)
num_label.pack(side="left", padx=10)
num_input.pack(side="right", padx=10)
frame5.pack(fill="both",expand="yes",pady=10)

#Bouton d'ajout
ajout=tk.Button(ajout_dcp, text="Ajouter", command=get_dcp_entry)
ajout.pack(side="bottom", pady=10)

window.mainloop()
