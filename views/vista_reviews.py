from tkinter import *

class VistaReviews(Frame):
    def __init__(self, master=None, controlador=None):
        super().__init__(master)
        self.master = master
        self.controlador = controlador
        self.config(bg="Orangered")
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        
        """ESCRIBE UNA REVIEW"""
        self.review=Label(self, text="Escribe una Review", font=("Comic Sans MS", 24, "bold"), bg="Orangered")
        self.review.grid()
        self.escribirReview = Text(self, height=5, width=40)
        self.escribirReview.grid(padx=1, pady=1)
        
        self.boton_review= Button(self, text="Enviar Review", bg="SpringGreen4", font=("Comic Sans MS", 12 ,"bold"), fg= "gray7")
        self.boton_review.grid()
        
        """VER REVIEWS"""
        self.busqueda = Label(self, text="Reviews", font=("Comic Sans MS", 24, "bold"), bg="Orangered")
        self.busqueda.grid(padx=0, pady=0)
        self.verReviews= Listbox(self, selectmode=SINGLE, font=("OpenSans"), bg="Orange", height=5, width=10)
        elementos=["Review 1", "Review 2", "Review 2", "Review 3", "Review 4"]
        for elemento in elementos:
            self.verReviews.insert(END, f"{elemento}")
        self.verReviews.grid()
        
        #self.grid_rowconfigure(0, weight=1)
        #self.grid_columnconfigure(0, weight=1)
        
        self.boton_inicio = Button(self, text="Inicio", command=self.controlador.regresar_inicio, bg="SpringGreen4", font=("Comic Sans MS", 12 ,"bold"), fg= "gray7")
        self.boton_inicio.grid(padx= 10, pady=10, sticky="nsew")
        self.boton_inicio.place()
