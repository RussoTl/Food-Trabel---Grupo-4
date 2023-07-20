#Este va a ser el archivo PRINCIPAL
#Aqui vamos a crear la ventana principal.
#def o class necesarias para cargar los datos, mostrar las vistas y gestionar las interacciones del usuario.
class DestinoCulinario:
    def __init__(self, id, nombre, tipo_cocina, ingredientes, precio_minimo, precio_maximo, popularidad, disponibilidad, id_ubicacion, imagen):
        self.id = id
        self.nombre = nombre
        self.tipo_cocina = tipo_cocina
        self.ingredientes = ingredientes
        self.precio_minimo = precio_minimo
        self.precio_maximo = precio_maximo
        self.popularidad = popularidad
        self.disponibilidad = disponibilidad
        self.id_ubicacion = id_ubicacion
        self.imagen = imagen

class Actividad:
    def __init__(self, id, nombre, destino_id, hora_inicio):
        self.id = id
        self.nombre = nombre
        self.destino_id = destino_id
        self.hora_inicio = hora_inicio

class RutaVisita:
    def __init__(self, id, nombre, destinos):
        self.id = id
        self.nombre = nombre
        self.destinos = destinos

class Ubicacion:
    def __init__(self, id, direccion, coordenadas):
        self.id = id
        self.direccion = direccion
        self.coordenadas = coordenadas

class Usuario:
    def __init__(self, id, nombre, apellido, historial_rutas):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.historial_rutas = historial_rutas

class Review:
    def __init__(self, id, id_destino, id_usuario, calificacion, comentario, animo):
        self.id = id
        self.id_destino = id_destino
        self.id_usuario = id_usuario
        self.calificacion = calificacion
        self.comentario = comentario
        self.animo = animo
