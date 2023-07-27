from tkinter import *

root = Tk()
root.title("Menu")
root.geometry("300x300")
root.config(bg="DarkOrange2")


destinoCulinario = Button(root, text="Destinos Culinarios",bg= "SpringGreen4", font=("Comic Sans MS", 12 ,"bold"), fg ="gray7")
destinoCulinario.grid(column=0, row=0, ipadx=5, ipady=5, padx=10, pady=10)
destinoCulinario.place(relx=0.5, rely=0.2, anchor="c")

busquedaFiltro = Button(root, text="Búsqueda y Filtro",bg= "SpringGreen4", font=("Comic Sans MS", 12 ,"bold"), fg ="gray7")
busquedaFiltro.grid(column=0, row=1, ipadx=5, ipady=5, padx=10, pady=10)
busquedaFiltro.place(relx=0.5, rely=0.4, anchor="c")

planificarVisitas = Button(root, text="Planificar Visitas",bg= "SpringGreen4", font=("Comic Sans MS", 12 ,"bold"), fg ="gray7")
planificarVisitas.grid(column=0, row=2, ipadx=5, ipady=5, padx=10, pady=10)
planificarVisitas.place(relx=0.5, rely=0.6, anchor="c")

reviewsCalificaciones = Button(root, text="Reviews y Calificaciones",bg= "SpringGreen4", font=("Comic Sans MS", 12 ,"bold"), fg ="gray7")
reviewsCalificaciones.grid(column=0, row=3, ipadx=5, ipady=5, padx=10, pady=10)
reviewsCalificaciones.place(relx=0.5, rely=0.8, anchor="c")


root.mainloop()