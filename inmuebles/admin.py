# Importación del panel de administración de Django
from django.contrib import admin

# Importación del modelo Inmueble
from .models import Inmueble


# Registro del modelo Inmueble en el panel de administración
admin.site.register(Inmueble)