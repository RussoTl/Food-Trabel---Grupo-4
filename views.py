import tkinter as tk

class MainMenuView(tk.Frame):
    def __init__(self, parent, destinos_culinarios, actividades, rutas_visita):
        super().__init__(parent)
        self.destinos_culinarios = destinos_culinarios
        self.actividades = actividades
        self.rutas_visita = rutas_visita