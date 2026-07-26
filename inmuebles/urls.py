# Importación de la función para definir las rutas
from django.urls import path

# Importación de las vistas de la aplicación
from . import views


# Rutas de la aplicación de gestión de inmuebles
urlpatterns = [

    # Página principal que muestra la lista de inmuebles
    path('', views.lista_inmuebles, name='lista_inmuebles'),

    # Ruta para registrar un nuevo inmueble
    path('nuevo/', views.crear_inmueble, name='crear_inmueble'),

    # Ruta para editar un inmueble existente
    path('editar/<int:id>/', views.editar_inmueble, name='editar_inmueble'),

    # Ruta para eliminar un inmueble
    path('eliminar/<int:id>/', views.eliminar_inmueble, name='eliminar_inmueble'),
]