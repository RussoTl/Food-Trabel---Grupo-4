import json

class Ubicacion:
    def __init__(self, id, direccion, coordenadas):
        self.id = id
        self.direccion = direccion
        self.coordenadas = coordenadas

    def to_json(self):
        coordenadas_json= []
        for coordenada in self.coordenadas:
            coordenadas_json.append(coordenada)

        return {"id": self.id,
                "direccion": self.direccion,
                "coordenadas": coordenadas_json}
    
    @classmethod
    def from_json(cls, json_datos):
        id= json_datos["id"]
        direccion= json_datos["direccion"]
        coordenadas= json_datos["coordenadas"]
        return cls(id, direccion, coordenadas)
    
    @staticmethod
    def guardar_ubiacion_a_json(ubicacion, nombre_archivo= "ubicacion_json"):

        with open(nombre_archivo, "w", encoding='utf-8') as archivo:
         json.dump(ubicacion.to_json(), archivo, indent=4, ensure_ascii=False)

    @staticmethod
    def cargar_ubicacion_desde_json(nombre_archivo= "ubicacion_json"):

        with open(nombre_archivo, "r", encoding='utf-8') as archivo:
            ubicacion_leida_json= json.load(archivo)
            ubicacion_leida= Ubicacion.from_json(ubicacion_leida_json)
        return ubicacion_leida
    
    @staticmethod
    def mostrar_ubicacion_cargada(ubicacion_leida):
        print("id: ", ubicacion_leida.id)
        print("Dirccion: ", ubicacion_leida.direccion)
        print("Coordenadas: ", ubicacion_leida.coordenadas)

#PRUEBAS
ubi1= Ubicacion(1, "Av. San Martín 4001, Salta", [-24.693685, -65.408140])
#ubi2= Ubicacion(2, "Pje. Zorrilla 1, A4400 Salta", [-24.788253, -65.402364])
#ubi3= Ubicacion(3, "Caseros 221, A4400 DME, Salta", [-24.790140, -65.405945])

Ubicacion.guardar_ubiacion_a_json(ubi1, "ubicacion_json")

ubicacion_leida= Ubicacion.cargar_ubicacion_desde_json("ubicacion_json")

Ubicacion.mostrar_ubicacion_cargada(ubicacion_leida)