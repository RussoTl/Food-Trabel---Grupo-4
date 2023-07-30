from tkinter import *

class VistaInicio(Frame):
    def __init__(self, master=None, controlador=None):
        super().__init__(master)
        self.master = master
        self.controlador = controlador
        self.config(bg="Orangered")
        self.titulo = Label(self, text="Foodie Tour", font=("Comic Sans MS", 24, "bold"), bg="Orangered")
        self.titulo.grid(row=0, column=0, pady=5)
        
        
        def salir(self):
            self.destroy()
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        
        
        
        self.boton_destinos = Button(self, text="Explorar Destinos Culinarios", command=self.controlador.mostrar_destinos, bg="SpringGreen4", font=("Comic Sans MS", 12 ,"bold"), fg= "gray7")
        self.boton_destinos.grid(padx= 10, pady=10, sticky="nsew")

        self.boton_busquedaFiltro = Button(self, text="Búsqueda y Filtro", command=self.controlador.mostrar_busqueda_filtro, bg="SpringGreen4", font=("Comic Sans MS", 12 ,"bold"), fg= "gray7")
        self.boton_busquedaFiltro.grid(padx= 10, pady=10, sticky="nsew")

        self.boton_planificarVisitas = Button(self, text="Planificar Visitas", command=self.controlador.mostrar_rutas, bg="SpringGreen4", font=("Comic Sans MS", 12 ,"bold"), fg= "gray7")
        self.boton_planificarVisitas.grid(padx= 10, pady=10, sticky="nsew")

        self.boton_reviewsCalif = Button(self, text="Reviews y Calificaciones", command=self.controlador.mostrar_reviews, bg="SpringGreen4", font=("Comic Sans MS", 12 ,"bold"), fg= "gray7")
        self.boton_reviewsCalif.grid(padx= 10, pady=10, sticky="nsew")

        self.boton_salir = Button(self, text="Salir", command= lambda: salir(master), bg="SpringGreen4", font=("Comic Sans MS", 12 ,"bold"), fg= "gray7")
        self.boton_salir.grid(padx= 10, pady=10, sticky="nsew")
        self.boton_salir.place()
