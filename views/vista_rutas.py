from tkinter import *

class VistaRutas(Frame):
    def __init__(self, master=None, controlador=None):
        super().__init__(master)
        self.master = master
        self.controlador = controlador
        self.config(bg="Orangered")
        self.titulo = Label(self, text="Rutas", font=("Comic Sans MS", 24, "bold"), bg="Orangered")
        self.titulo.grid(pady=10)
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.boton_inicio = Button(self, text="Inicio", command=self.controlador.regresar_inicio, bg="SpringGreen4", font=("Comic Sans MS", 12 ,"bold"), fg= "gray7")
        self.boton_inicio.grid(padx= 10, pady=10, sticky="nsew")
        self.boton_inicio.place()
"""
def mostrar_rutas():
    ventana_rutas = tk.Toplevel()
    ventana_rutas.title("Rutas de Visita")
    ventana_rutas.geometry("400x300")

    etiqueta_rutas = tk.Label(ventana_rutas, text="Selecciona una Opcion:")
    etiqueta_rutas.pack(pady=10)

    
    boton_escribirReview = tk.Button(boton_reviewsCalif, text="Escribe una reseña y califica", command=mostrar_rutas, bg="SpringGreen4", font=("Comic Sans MS", 12 ,"bold"), fg= "gray7")
    boton_escribirReview.pack(pady=10)

    boton_verReview = tk.Button(boton_reviewsCalif, text="Ver Reviews", command=mostrar_rutas, bg="SpringGreen4", font=("Comic Sans MS", 12 ,"bold"), fg= "gray7")
    boton_verReview.pack(pady=10)
    """