from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_inmuebles, name='lista_inmuebles'),

    path('nuevo/', views.crear_inmueble, name='crear_inmueble'),

    path('editar/<int:id>/', views.editar_inmueble, name='editar_inmueble'),

    path('eliminar/<int:id>/', views.eliminar_inmueble, name='eliminar_inmueble'),
]