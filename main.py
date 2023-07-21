import models.destino_culinario as destino_culinario, models.actividad as actividad, models.ruta_visita as ruta_visita, models.usuario as usuario, models.review as review, models.ubicacion as ubicacion

# PROGRAMA
destino1 = destino_culinario.DestinoCulinario(
    id=1,
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

print(destino1)
