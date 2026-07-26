# Importación de funciones necesarias de Django
from django.shortcuts import render, redirect, get_object_or_404

# Importación del modelo Inmueble
from .models import Inmueble

# Importación del formulario de inmuebles
from .forms import InmuebleForm


# Vista para listar todos los inmuebles registrados
def lista_inmuebles(request):
    inmuebles = Inmueble.objects.all()
    return render(request, 'inmuebles/lista.html', {
        'inmuebles': inmuebles
    })


# Vista para registrar un nuevo inmueble
def crear_inmueble(request):
    if request.method == 'POST':
        formulario = InmuebleForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect('lista_inmuebles')
    else:
        formulario = InmuebleForm()

    return render(request, 'inmuebles/formulario.html', {
        'formulario': formulario
    })


# Vista para editar la información de un inmueble
def editar_inmueble(request, id):
    inmueble = get_object_or_404(Inmueble, id=id)

    if request.method == 'POST':
        formulario = InmuebleForm(request.POST, instance=inmueble)

        if formulario.is_valid():
            formulario.save()
            return redirect('lista_inmuebles')
    else:
        formulario = InmuebleForm(instance=inmueble)

    return render(request, 'inmuebles/formulario.html', {
        'formulario': formulario
    })


# Vista para eliminar un inmueble del sistema
def eliminar_inmueble(request, id):
    inmueble = get_object_or_404(Inmueble, id=id)

    if request.method == 'POST':
        inmueble.delete()
        return redirect('lista_inmuebles')

    return render(request, 'inmuebles/confirmar_eliminar.html', {
        'inmueble': inmueble
    })