import json


class DestinoCulinario:
    def __init__(self, id, nombre, tipo_cocina, ingredientes, precio_minimo, precio_maximo, popularidad,
                 disponibilidad, id_ubicacion, imagen):
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

    def __str__(self):
        disponibilidad_str = 'Disponible' if self.disponibilidad else 'No disponible'
        return f"""\
            ID: {self.id}
            Nombre: {self.nombre}
            Tipo de cocina: {self.tipo_cocina}
            Ingredientes: {', '.join(self.ingredientes)}
            Precio mínimo: 💲{self.precio_minimo}
            Precio máximo: 💲{self.precio_maximo}
            Popularidad: ⭐️{self.popularidad}
            Disponibilidad: {disponibilidad_str}
            ID de ubicación: {self.id_ubicacion}
            Imagen: {self.imagen}
        """

    def to_json(self):
        ingredientes_json = []
        for ingrediente in self.ingredientes:
            ingredientes_json.append(ingrediente)
        return {
            "id": self.id,
            "nombre": self.nombre,
            "tipo_cocina": self.tipo_cocina,
            "ingredientes": ingredientes_json,
            "precio_minimo": self.precio_minimo,
            "precio_maximo": self.precio_maximo,
            "popularidad": self.popularidad,
            "disponibilidad": self.disponibilidad,
            "id_ubicacion": self.id_ubicacion,
            "imagen": self.imagen
        }

    @classmethod
    def from_json(cls, json_datos):
        id = json_datos["id"]
        nombre = json_datos["nombre"]
        tipo_cocina = json_datos["tipo_cocina"]
        ingredientes = json_datos["ingredientes"]
        precio_minimo = json_datos["precio_minimo"]
        precio_maximo = json_datos["precio_maximo"]
        popularidad = json_datos["popularidad"]
        disponibilidad = json_datos["disponibilidad"]
        id_ubicacion = json_datos["id_ubicacion"]
        imagen = json_datos["imagen"]
        return cls(id, nombre, tipo_cocina, ingredientes, precio_minimo, precio_maximo, popularidad, disponibilidad,
                   id_ubicacion, imagen)

    @staticmethod
    def guardar_destinos_a_json(destinos, nombre_archivo="data/destinos_json"):
        # Método estático para guardar destinos en un archivo JSON
        destinos_json = []
        for destino in destinos:
            destinos_json.append(destino.to_json())

        with open(nombre_archivo, "w", encoding='utf-8') as archivo:
            json.dump(destinos_json, archivo, indent=4, ensure_ascii=False)

    @staticmethod
    def cargar_destinos_desde_json(nombre_archivo="data/destinos_json"):
        # Método estático para cargar destinos desde un archivo JSON
        with open(nombre_archivo, "r", encoding='utf-8') as archivo:
            destinos_leidos_json = json.load(archivo)
        destinos_leidos = []
        for destino_json in destinos_leidos_json:
            destino_leido = DestinoCulinario.from_json(destino_json)
            destinos_leidos.append(destino_leido)
        return destinos_leidos

    @staticmethod
    def mostrar_destinos(destinos_cargados):
        # Muestra de datos recuperados de un archivo JSON
        for destino_leido in destinos_cargados:
            print("ID: ", destino_leido.id)
            print("Nombre: ", destino_leido.nombre)
            print("Tipo de cocina: ", destino_leido.tipo_cocina)
            print("Ingredientes: ", destino_leido.ingredientes)
            print("Precio mínimo: ", destino_leido.precio_minimo)
            print("Precio máximo: ", destino_leido.precio_maximo)
            print("Popularidad: ", destino_leido.popularidad)
            print("Disponibilidad: ", destino_leido.disponibilidad)
            print("ID de ubicación: ", destino_leido.id_ubicacion)
            print("Imagen: ", destino_leido.imagen)
            print("--------------------")
