import json


class Usuario:
    def __init__(self, id, nombre, apellido, historial_rutas=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        if historial_rutas is None:
            self.historial_rutas = []
        else:
            self.historial_rutas = historial_rutas

    def to_json(self):
        historial_rutas_json = []
        for historial in self.historial_rutas:
            historial_rutas_json.append(historial)
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "historial_rutas": historial_rutas_json
        }

    def __str__(self):
        return f"""\
            ID: {self.id}
            Nombre: {self.nombre}
            Apellido: {self.apellido}
            Historial de rutas: {', '.join(self.historial_rutas)}
        """

    @classmethod
    def from_json(cls, json_datos):
        id = json_datos["id"]
        nombre = json_datos["nombre"]
        apellido = json_datos["apellido"]
        historial_rutas = json_datos["historial_rutas"]
        return cls(id, nombre, apellido, historial_rutas)

    @staticmethod
    def guardar_usuarios_a_json(usuarios, nombre_archivo="data/usuarios_json"):
        usuarios_json = []
        for usuario in usuarios:
            usuarios_json.append(usuario.to_json())

        with open(nombre_archivo, "w", encoding='utf-8') as archivo:
            json.dump(usuarios_json, archivo, indent=4, ensure_ascii=False)

    @staticmethod
    def cargar_usuarios_desde_json(nombre_archivo="data/usuarios_json"):
        with open(nombre_archivo, "r", encoding='utf-8') as archivo:
            usuarios_leidos_json = json.load(archivo)
        usuarios_leidos = []
        for usuario_json in usuarios_leidos_json:
            usuario_leido = Usuario.from_json(usuario_json)
            usuarios_leidos.append(usuario_leido)
        return usuarios_leidos

    @staticmethod
    def mostrar_usuarios_cargados(usuarios_cargados):
        for usuario_cargado in usuarios_cargados:
            print("ID: ", usuario_cargado.id)
            print("Nombre: ", usuario_cargado.nombre)
            print("Apellido: ", usuario_cargado.apellido)
            print("Historial de Rutas:", usuario_cargado.historial_rutas)
            print("--------------------")


# PRUEBAS JSON
usuario1 = Usuario(1, "Javi", "Acosta", [1, 2, 5])
usuario2 = Usuario(2, "Agustin", "Acosta", [1, 4, 5])
usuario3 = Usuario(3, "Mateo", "Fileni", [1, 3, 4])
usuario4 = Usuario(4, "Nacho", "Saravia", [4, 5, 6])
usuario5 = Usuario(5, "Andres", "Sarmiento", [4, 5])
usuario6 = Usuario(6, "David", "Romero", [6])

usuarios = [usuario1, usuario2, usuario3, usuario4, usuario5, usuario6]

# Guardar usuarios en un archivo JSON
Usuario.guardar_usuarios_a_json(usuarios, "data/usuarios_json")

# Cargar usuarios desde el archivo JSON
usuarios_leidos = Usuario.cargar_usuarios_desde_json("data/usuarios_json")

# Mostrar los usuarios recuperados
Usuario.mostrar_usuarios_cargados(usuarios_leidos)
