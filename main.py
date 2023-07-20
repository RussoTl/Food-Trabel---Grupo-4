#Este va a ser el archivo PRINCIPAL
#Aqui vamos a crear la ventana principal.
import tkinter as tk
from views import MainMenuView
from data import load_data

class FoodieTourApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Foodie Tour")
        self.geometry("800x600")

        # Carga de datos desde archivos JSON
        self.destinos_culinarios, self.actividades, self.rutas_visita, self.usuarios, self.reviews = load_data()

        # Inicialización de la vista principal
        self.main_menu_view = MainMenuView(self, self.destinos_culinarios, self.actividades, self.rutas_visita)

if __name__ == "__main__":
    app = FoodieTourApp()
    app.mainloop()