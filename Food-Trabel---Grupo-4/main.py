import json
from models.destino_culinario import DestinoCulinario
from models.actividad import Actividad
from models.review import Review
from models.ruta_visita import RutaVisita
from models.ubicacion import Ubicacion
from models.usuario import Usuario

# PROGRAMA
destino1 = DestinoCulinario(
    id=1,
    nombre="Destino Mediterraneo",
    tipo_cocina="Mediterránea 🍝",
    ingredientes=["aceite de oliva",
                  "tomates 🍅", "ajo 🧄", "pescado 🐟"],
    precio_minimo=30.0,
    precio_maximo=50.0,
    popularidad=8.7,
    disponibilidad=True,
    id_ubicacion=123,
    imagen="https://ejemplo.com/imagen_del_destino1.jpg"
)
destino2 = DestinoCulinario(
    id=2,
    nombre="Sushi Go",
    tipo_cocina="Japonesa 🍣",
    ingredientes=["arroz 🍚", "pescado fresco 🐟",
                  "alga nori 🌿", "salsa de soja 🍱"],
    precio_minimo=25.0,
    precio_maximo=60.0,
    popularidad=9.2,
    disponibilidad=True,
    id_ubicacion=456,
    imagen="https://ejemplo.com/imagen_destino2.jpg"
)

destino3 = DestinoCulinario(
    id=3,
    nombre="Tacolandia",
    tipo_cocina="Mexicana 🌮",
    ingredientes=["tortillas de maíz 🌽",
                  "carne de res 🥩", "frijoles 🍛", "guacamole 🥑"],
    precio_minimo=20.0,
    precio_maximo=40.0,
    popularidad=8.5,
    disponibilidad=True,
    id_ubicacion=789,
    imagen="https://ejemplo.com/imagen_destino3.jpg"
)

destino4 = DestinoCulinario(
    id=4,
    nombre="Pizzini",
    tipo_cocina="Italiana 🍕",
    ingredientes=["harina de trigo 🍞",
                  "salsa de tomate 🍅", "mozzarella 🧀", "albahaca 🌿"],
    precio_minimo=25.0,
    precio_maximo=45.0,
    popularidad=9.0,
    disponibilidad=True,
    id_ubicacion=101,
    imagen="https://ejemplo.com/imagen_destino4.jpg"
)

destino5 = DestinoCulinario(
    id=5,
    nombre="Agni Food",
    tipo_cocina="India 🍛",
    ingredientes=["arroz basmati 🍚", "pollo tikka masala 🍗",
                  "especias 🌶️", "lentejas 🍲"],
    precio_minimo=35.0,
    precio_maximo=55.0,
    popularidad=8.8,
    disponibilidad=True,
    id_ubicacion=202,
    imagen="https://ejemplo.com/imagen_destino5.jpg"
)

destino6 = DestinoCulinario(
    id=6,
    nombre="Messie",
    tipo_cocina="Francesa 🥐",
    ingredientes=["mantequilla 🧈", "harina de trigo 🍞",
                  "queso brie 🧀", "baguette 🥖"],
    precio_minimo=40.0,
    precio_maximo=70.0,
    popularidad=9.5,
    disponibilidad=True,
    id_ubicacion=303,
    imagen="https://ejemplo.com/imagen_destino6.jpg"
)

destinos = [destino1, destino2, destino3, destino4, destino5, destino6]

# Guardar destinos en un archivo JSON
DestinoCulinario.guardar_destinos_a_json(destinos, "data/destinos_json")

# Cargar destinos desde el archivo JSON
destinos_leidos = DestinoCulinario.cargar_destinos_desde_json(
    "data/destinos_json")

# Mostrar los datos recuperados
DestinoCulinario.mostrar_destinos(destinos_leidos)
