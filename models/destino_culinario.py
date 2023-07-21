class DestinoCulinario:
    def __init__(self, id, tipo_cocina, ingredientes, precio_minimo, precio_maximo, popularidad, disponibilidad, id_ubicacion, imagen):
        self. id = id
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
            Tipo de cocina: {self.tipo_cocina}
            Ingredientes: {', '.join(self.ingredientes)}
            Precio mínimo: 💲{self.precio_minimo}
            Precio máximo: 💲{self.precio_maximo}
            Popularidad: ⭐️{self.popularidad}
            Disponibilidad: {disponibilidad_str}
            ID de ubicación: {self.id_ubicacion}
            Imagen: {self.imagen}
        """