from PIL import Image, ImageTk
from models.destino_culinario import DestinoCulinario

class ControladorDestinos:
    def __init__(self, app, destinos):
        self.app = app
        self.destinos = destinos

    def buscar_destino_por_id(self, nombre_destino):
        for destino in self.destinos:
            if destino.nombre == nombre_destino:
                return destino
        raise ValueError(f"No se encontró ningún destino con el nombre '{nombre_destino}'")
    

        
    def regresar_inicio(self):
        self.app.cambiar_frame(self.app.vista_inicio)