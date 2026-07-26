# Importación del módulo de formularios de Django
from django import forms

# Importación del modelo Inmueble
from .models import Inmueble


# Formulario para registrar y editar inmuebles
class InmuebleForm(forms.ModelForm):

    # Configuración del formulario basada en el modelo Inmueble
    class Meta:
        model = Inmueble

        # Campos que se mostrarán en el formulario
        fields = [
            'titulo',
            'descripcion',
            'precio',
            'ciudad',
            'direccion',
            'estado',
        ]