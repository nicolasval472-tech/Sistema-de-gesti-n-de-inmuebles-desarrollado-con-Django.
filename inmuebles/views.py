from django.shortcuts import render, redirect, get_object_or_404
from .models import Inmueble
from .forms import InmuebleForm


# LISTAR
def lista_inmuebles(request):
    inmuebles = Inmueble.objects.all()
    return render(request, 'inmuebles/lista.html', {
        'inmuebles': inmuebles
    })


# CREAR
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


# EDITAR
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


# ELIMINAR
def eliminar_inmueble(request, id):
    inmueble = get_object_or_404(Inmueble, id=id)

    if request.method == 'POST':
        inmueble.delete()
        return redirect('lista_inmuebles')

    return render(request, 'inmuebles/confirmar_eliminar.html', {
        'inmueble': inmueble
    })