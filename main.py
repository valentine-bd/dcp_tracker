"""Importation des modules"""
from widgets.main_window import MainWindow

class App():
    """Classe correspondant à l'application"""
    def main(self):
        """Fonction principale"""     
        MainWindow()

if __name__ == '__main__':
    App().main()
