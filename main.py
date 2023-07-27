from customtkinter import *
from tkinter import *
from models.Usuario import usuario
from tkinter import messagebox as MessageBox
from PIL import Image, ImageTk
from controladores.vista_1 import controlador_inicio

root = CTk()


nombreUsuario = StringVar()
passUsuario = StringVar()
usuarios = []


def createGUI():

    """ROOT (VENTANA PRINCIPAL)"""
    
    root.title("LogIn")
    """MAIN FRAME"""
    mainFrame = Frame(root)
    mainFrame.pack()
    mainFrame.config(width=400, height=320, bg="Orangered")

    """LABELS""" 
    titulo = Label(mainFrame, text="Foodie Tour", font=("Comic Sans MS", 18, "bold"), bg="Orangered", underline=6)
    titulo.grid(column=0, row=0, padx=10, pady=10, columnspan=2)
    

    nombreLabel = Label(mainFrame, text="Usuario:",bg="Orangered", font=("Comic Sans MS", 14, "bold"), fg="gray7") #DarkGreen
    nombreLabel.grid(column=0, row=1)
    

    passlLabel = Label(mainFrame, text="Contraseña:",bg="Orangered", font=("Comic Sans MS", 14, "bold"), fg="gray7")
    passlLabel.grid(column=0, row=2)


    """ENTRADAS DE TEXTO"""
    
    nombreUsuario.set("")
    nombreEntry = CTkEntry(mainFrame, textvariable=nombreUsuario)
    nombreEntry.grid(column=1, row=1)

    passUsuario.set("")
    passEntry = CTkEntry(mainFrame, textvariable=passUsuario, show="*")
    passEntry.grid(column=1, row=2)

    """BOTONES DE REGISTRO DE USER E INICIO DE SESION"""
    inicioSesion = CTkButton(mainFrame, text="Iniciar Sesion", command=iniciarSesion, fg_color= "SpringGreen4", font=("Comic Sans MS", 12 ,"bold"), text_color ="gray7")
    inicioSesion.grid(column=1, row=3, ipadx=5, ipady=5, padx=10, pady=10)

    registro = CTkButton(mainFrame, text="Registrar", command=registrarUsuario, fg_color= "SpringGreen4", font=("Comic Sans MS",12, "bold"), text_color="gray7")
    registro.grid(column=0, row=3, ipadx=5, ipady=5, padx=10, pady=10)

    root.mainloop()

"""INICIO DE SESION"""
def iniciarSesion():
    for user in usuarios:
        if user.nombre == nombreUsuario.get():
            test = user.conectar(passUsuario.get())
            if test:
                
                MessageBox.showinfo("Conectado", f"Se inicio sesion en [{user.nombre}] correctamente.")
                
            #else:
                #MessageBox.showerror("Error", "Contraseña incorrecta.")
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

def cambiar_frame(frame_destino):
        frame_destino.tkraise()
        
if __name__== "__main__":
    #user1 = usuario(input("Ingrese un Usuario: "), input("Ingrese una contraseña: "))
    createGUI()
    