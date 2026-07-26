# Importación del panel de administración de Django
from django.contrib import admin

# Importación de las funciones para definir e incluir rutas
from django.urls import path, include


# Rutas principales del proyecto
urlpatterns = [

    # Ruta para acceder al panel de administración
    path('admin/', admin.site.urls),

    # Incluye las rutas de la aplicación de inmuebles
    path('', include('inmuebles.urls')),
]