from tkinter import *
from tkintermapview import TkinterMapView
from models.ubicacion import Ubicacion
from models.destino_culinario import DestinoCulinario
from PIL import Image, ImageTk


class VistaDestinos(Frame):
    def __init__(self, master=None, controlador=None, seleccionar_destino_callback=None, seleccionar_ubicacion_callback=None):
        super().__init__(master)
        self.master = master
        self.controladorDestino = controlador
        self.seleccionar_destino_callback = seleccionar_destino_callback
        self.seleccionar_ubicacion_callback = seleccionar_ubicacion_callback
        self.config(bg="Orangered")
        
        self.destinos = DestinoCulinario.cargar_destinos_desde_json(r"data\destinos_json")
        self.ubicaciones = Ubicacion.cargar_ubicaciones_desde_json(r"data\ubicaciones_json")
        self.marcadores =[]
        self.imagenes = []
        
        
        # Frame para los destinos
        self.frame_destinos = Frame(self, width=200, height=500, bg="Orangered")
        self.frame_destinos.pack(side='left', fill='both', expand=True)
        
        #ListBox para los destinos
        self.lista_destinos = Listbox(self.frame_destinos, bg="Orangered", fg="gray7", font=("Comic Sans",8,"bold"))
        self.lista_destinos.bind('<<ListboxSelect>>', self.on_select_destino)
        self.lista_destinos.pack(fill='both', expand=True)
        
          
        self.titulo = Label(self, text="Destinos Culinarios", bg="Orangered",font=("Comic Sans MS", 24, "bold")) 
        self.titulo.pack()
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.boton_inicio = Button(self, text="Inicio", command=self.controladorDestino.regresar_inicio, bg="SpringGreen4",  fg= "gray7", font=("Comic Sans MS", 12 ,"bold"))
        self.boton_inicio.pack(side="bottom", anchor="sw")
        self.boton_inicio.place()
        
        
        
        """MAPA"""
        self.frame_mapa= Frame(self, width=0, height=600)
        self.frame_mapa.pack(side='right', fill='both', expand=True)
        
        
        
        #Placeholder para el mapa
        self.mapa = TkinterMapView(self, width=400, height=600, corner_radius=0)
        self.mapa.set_position(-24.7930070, -65.4117382)
        self.mapa.set_zoom(14)
        self.mapa.pack(side='right')
        
        # Carga los destinos, imágenes y marcadores después de crear el mapa
        self.cargar_imagenes()
        self.cargar_marcadores()
        self.cargar_destinos()
        self.cargar_marcadores()
        
    def cargar_destinos(self):
        for destino in self.destinos:
            self.lista_destinos.insert(END, destino.nombre)  # Agregar los destinos a la lista_destinos


    def agregar_destino(self, destino):
        nombre = destino.nombre
        self.lista_destinos.insert(END, nombre)

    def agregar_marcador_mapa(self, latitud, longitud, texto, imagen=None, destino=None):
        if self.seleccionar_ubicacion_callback is not None:
            return self.mapa.set_marker(latitud, longitud, text=texto, image=imagen, command=lambda event: self.seleccionar_ubicacion(event, destino))
        else:
            # Si self.seleccionar_ubicacion_callback es None, solo se creará el marcador sin comando.
            return self.mapa.set_marker(latitud, longitud, text=texto, image=imagen)

    def cargar_marcadores(self):
        for ubicacion, destino in zip(self.ubicaciones, self.destinos):
            imagen = self.imagenes[ubicacion.id - 1]
            marcador = self.agregar_marcador_mapa(ubicacion.coordenadas[0], ubicacion.coordenadas[1], destino.nombre, imagen, destino)
            marcador.hide_image(True)
            self.marcadores.append(marcador)
        

    def cargar_imagenes(self):
        for destino in self.destinos:
            ruta_img = "assets/" + destino.imagen
            imagen = ImageTk.PhotoImage(Image.open(ruta_img).resize((200, 200)))
            self.imagenes.append(imagen)
    
    def agregar_marcador_mapa(self, latitud, longitud, texto, imagen=None, destino=None):
        if self.seleccionar_ubicacion_callback is not None:
            return self.mapa.set_marker(latitud, longitud, text=texto, image=imagen, command=lambda event: self.seleccionar_ubicacion(event, destino))
        else:
            # Si self.seleccionar_ubicacion_callback es None, solo se creará el marcador sin comando.
            return self.mapa.set_marker(latitud, longitud, text=texto, image=imagen)

            
    
    def on_select_destino(self, event):
        # Obtener el índice del elemento seleccionado
        indice_seleccionado = self.lista_destinos.curselection()
        if indice_seleccionado:
            # Obtener el destino seleccionado
            nombre_destino = self.lista_destinos.get(indice_seleccionado)
            self.seleccionar_destino(nombre_destino)
    
    def seleccionar_destino(self, nombre_destino):
        destino_seleccionado = self.controladorDestino.buscar_destino_por_id(nombre_destino)
        ubicacion_seleccionada = None

        print("Destino seleccionado:", destino_seleccionado.nombre)
        # Buscar la ubicación correspondiente al destino seleccionado
        for ubicacion in self.ubicaciones:
            if ubicacion.id == destino_seleccionado.id_ubicacion:
                ubicacion_seleccionada = ubicacion
                break

        if ubicacion_seleccionada:
            # Centrar el mapa en la ubicación seleccionada
            self.mapa.set_position(ubicacion_seleccionada.coordenadas[0], ubicacion_seleccionada.coordenadas[1])


    
    def seleccionar_ubicacion(self, event, destino):
        if self.seleccionar_ubicacion_callback is not None:
            if destino is not None:
                print("Destino seleccionado:", destino.nombre)
                # Aquí puedes mostrar la imagen o realizar cualquier acción adicional que necesites.
     