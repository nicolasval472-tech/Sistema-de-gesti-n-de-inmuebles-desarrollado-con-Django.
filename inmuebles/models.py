# Importación del módulo de modelos de Django
from django.db import models


# Modelo que representa la información de un inmueble
class Inmueble(models.Model):

    # Título del inmueble
    titulo = models.CharField(max_length=200)

    # Descripción del inmueble
    descripcion = models.TextField()

    # Precio del inmueble
    precio = models.DecimalField(max_digits=12, decimal_places=2)

    # Ciudad donde se encuentra el inmueble
    ciudad = models.CharField(max_length=100)

    # Dirección del inmueble
    direccion = models.CharField(max_length=200)

    # Estado del inmueble (Disponible o No disponible)
    estado = models.BooleanField(default=True)

    # Fecha en la que se registra el inmueble
    fecha_registro = models.DateTimeField(auto_now_add=True)

    # Método que muestra el título del inmueble
    def __str__(self):
        return self.titulo