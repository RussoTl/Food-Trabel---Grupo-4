from tkinter import *
class VistaDestinos(Frame):
    def __init__(self, master=None, controlador=None):
        super().__init__(master)
        self.master = master
        self.controlador = controlador
        self.config(bg="Orangered")
        self.titulo = Label(self, text="Destinos Culinarios", font=("Comic Sans MS", 24, "bold"), bg="Orangered")
        self.titulo.grid(pady=10)
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.boton_inicio = Button(self, text="Inicio", command=self.controlador.regresar_inicio, bg="SpringGreen4", font=("Comic Sans MS", 12 ,"bold"), fg= "gray7")
        self.boton_inicio.grid(padx= 10, pady=10, sticky="nsew")
        self.boton_inicio.place()
