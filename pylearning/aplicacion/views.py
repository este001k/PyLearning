from django.shortcuts import render
from . forms import usuarioForm


def inicio(request):
    return render (request, 'inicio.html')

def formulario(request):
    if request.method == 'POST':
        form = usuarioForm(request.POST)
        if form.is_valid():
            form.save()
            # falta agregarlo a la base de datos y quiza una alerta
    else:
        form = usuarioForm()
    return render(request, 'formulario.html', {'form': form})