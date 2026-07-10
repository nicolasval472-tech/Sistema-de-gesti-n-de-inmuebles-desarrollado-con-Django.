from django.db import models

class Inmueble(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=12, decimal_places=2)
    ciudad = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    estado = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo