import json
from models import DestinoCulinario, Actividad, RutaVisita, Ubicacion, Usuario, Review

def load_data():
    # Aquí cargarías los datos desde los archivos JSON y los convertirías en instancias de las clases definidas en models.py
    # Por ejemplo:
    with open('data/destinos_culinarios.json') as f:
        destinos_culinarios_data = json.load(f)
    destinos_culinarios = [DestinoCulinario(**data) for data in destinos_culinarios_data]

    # Repetir el proceso para las otras categorías de datos (actividades, rutas_visita, usuarios, reviews)

    return destinos_culinarios, actividades, rutas_visita, usuarios, reviews