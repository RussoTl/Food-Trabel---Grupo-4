import tkinter as tk
from tkinter import Tk, Label, Entry, Frame, ttk, PhotoImage, StringVar, Button
from models.Usuarios import usuario
from tkinter import messagebox as MessageBox
from PIL import Image, ImageTk

root = Tk()



nombreUsuario = StringVar()
passUsuario = StringVar()
usuarios = []


def createGUI():

    """ROOT (VENTANA PRINCIPAL)"""
    
    root.title("LogIn")
    #MainFrame
    mainFrame = Frame(root)
    mainFrame.pack()
    mainFrame.config(width=400, height=320, bg="Orangered")

    """TITULOS""" 
    titulo = Label(mainFrame, text="Foodie Tour", font=("Comic Sans MS", 18, "bold"), bg="Orangered", underline=6)
    titulo.grid(column=0, row=0, padx=10, pady=10, columnspan=2)
 
    nombreLabel = Label(mainFrame, text="Usuario:",bg="Orangered", font=("Comic Sans MS", 14, "bold"), fg="gray7") #DarkGreen
    nombreLabel.grid(column=0, row=1)
    passlLabel = Label(mainFrame, text="Contraseña:",bg="Orangered", font=("Comic Sans MS", 14, "bold"), fg="gray7")
    passlLabel.grid(column=0, row=2)


    """ENTRADAS DE TEXTO"""
    
    nombreUsuario.set("")
    nombreEntry = Entry(mainFrame, textvariable=nombreUsuario)
    nombreEntry.grid(column=1, row=1)

    passUsuario.set("")
    passEntry = Entry(mainFrame, textvariable=passUsuario, show="*")
    passEntry.grid(column=1, row=2)

    """BOTONES DE REGISTRO DE USER E INICIO DE SESION"""
    inicioSesion = Button(mainFrame, text="Iniciar Sesion", command=iniciarSesion, bg= "SpringGreen4", font=("Comic Sans MS", 12 ,"bold"), fg ="gray7")
    inicioSesion.grid(column=1, row=3, ipadx=5, ipady=5, padx=10, pady=10)

    registro = Button(mainFrame, text="Registrar", command=registrarUsuario, bg= "SpringGreen4", font=("Comic Sans MS",12, "bold"), fg ="gray7")
    registro.grid(column=0, row=3, ipadx=5, ipady=5, padx=10, pady=10)

    root.mainloop()

"""INICIO DE SESION"""
def iniciarSesion():
    for user in usuarios:
        if user.nombre == nombreUsuario.get():
            test = user.conectar(passUsuario.get())
            if test:
                MessageBox.showinfo("Conectado", f"Se inicio sesion en [{user.nombre}] correctamente.")
            else:
                MessageBox.showerror("Error", "Contraseña incorrecta.")
            break 
    else:
        MessageBox.showerror("Error", "No existen usuarios con ese nombre.")
""" REGISTRO DE USER """
def registrarUsuario():
    name =  nombreUsuario.get()
    passwd = passUsuario.get()
    newUser = usuario(name,passwd)
    usuarios.append(newUser)
    MessageBox.showinfo("Registro Exitoso",f"Se registro el usuario {name} con Exito")
    nombreUsuario.set("")
    passUsuario.set("")


if __name__== "__main__":
    #user1 = usuario(input("Ingrese un Usuario: "), input("Ingrese una contraseña: "))
    createGUI()

