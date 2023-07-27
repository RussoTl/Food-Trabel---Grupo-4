from customtkinter import *

class menu():
    root = CTk()
    root.title("Menu")
    root.geometry("300x300")
    root.config(bg="DarkOrange2")


    destinoCulinario = CTkButton(root, text="Destinos Culinarios",fg_color="SpringGreen4", font=("Comic Sans MS", 12 ,"bold"), text_color="gray7")
    destinoCulinario.grid(column=0, row=0, ipadx=5, ipady=5, padx=10, pady=10)
    destinoCulinario.place(relx=0.5, rely=0.2, anchor="c")

    busquedaFiltro = CTkButton(root, text="Búsqueda y Filtro",fg_color="SpringGreen4", font=("Comic Sans MS", 12 ,"bold"), text_color="gray7")
    busquedaFiltro.grid(column=0, row=1, ipadx=5, ipady=5, padx=10, pady=10)
    busquedaFiltro.place(relx=0.5, rely=0.4, anchor="c")

    planificarVisitas = CTkButton(root, text="Planificar Visitas",fg_color= "SpringGreen4", font=("Comic Sans MS", 12 ,"bold"), text_color="gray7")
    planificarVisitas.grid(column=0, row=2, ipadx=5, ipady=5, padx=10, pady=10)
    planificarVisitas.place(relx=0.5, rely=0.6, anchor="c")

    reviewsCalificaciones = CTkButton(root, text="Reviews y Calificaciones",fg_color= "SpringGreen4", font=("Comic Sans MS", 12 ,"bold"), text_color="gray7")
    reviewsCalificaciones.grid(column=0, row=3, ipadx=5, ipady=5, padx=10, pady=10)
    reviewsCalificaciones.place(relx=0.5, rely=0.8, anchor="c")


    root.mainloop()