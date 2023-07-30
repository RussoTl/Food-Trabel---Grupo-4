import tkinter as tk
from views.vista_rutas import VistaRutas
from views.vista_destinos import VistaDestinos
from views.vista_busqueda_filtros import VistaBusquedaFiltro
from views.vista_inicio import VistaInicio
from views.vista_reviews import VistaReviews
from controladores.controlador_inicio import ControladorInicio
from controladores.controlador_busqueda_filtro import ControladorBusquedaFiltro
from controladores.controlador_destinos import ControladorDestinos
from controladores.controlador_rutas import ControladorRutas
from controladores.controlador_reviews import ControladorReviews


"""VENTANA PRINCIPAL"""
class Aplicacion(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Foodie Tour")
        self.geometry("400x400")
        self.resizable(False, False)
        self.config(bg="Orangered")
        self.iniciar()
        self.cambiar_frame(self.vista_inicio)
        
    def iniciar(self):
        controlador_inicio= ControladorInicio(self)
        controlador_actividades= ControladorBusquedaFiltro(self)
        controlador_destinos= ControladorDestinos(self)
        controlador_rutas=ControladorRutas(self)
        controlador_reviews= ControladorReviews(self)
        
        self.vista_inicio= VistaInicio(self, controlador_inicio)
        self.vista_actividades= VistaBusquedaFiltro(self, controlador_actividades)
        self.vista_destinos= VistaDestinos(self, controlador_destinos)
        self.vista_rutas= VistaRutas(self, controlador_rutas)
        self.vista_reviews= VistaReviews(self, controlador_reviews)

        self.ajustar_frame(self.vista_inicio)
        self.ajustar_frame(self.vista_actividades)
        self.ajustar_frame(self.vista_destinos)
        self.ajustar_frame(self.vista_rutas)
        self.ajustar_frame(self.vista_reviews)
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
    def ajustar_frame(self, frame):
        frame.grid(row=0, column= 0, sticky="nsew")
    
    def cambiar_frame(self, frame_destino):
        frame_destino.tkraise()
        

if __name__== "__main__":
    app = Aplicacion()
    app.mainloop()