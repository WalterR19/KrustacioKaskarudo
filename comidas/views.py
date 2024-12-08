from django.shortcuts import render, get_object_or_404, redirect
from .models import Comida
from .forms import ComidaForm

def index(request):
    """
    Vista para mostrar el listado de comidas.
    """
    comidas = Comida.objects.all()
    return render(request, 'index.html', {'comidas': comidas})

def create_comida(request):
    """
    Vista para crear una nueva comida.
    """
    if request.method == 'POST':
        form = ComidaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comidas:index')
    else:
        form = ComidaForm()
    return render(request, 'create.html', {'form': form})

def detail_comida(request, pk):
    """
    Vista para ver los detalles de una comida.
    """
    comida = get_object_or_404(Comida, pk=pk)
    return render(request, 'detail.html', {'comida': comida})

def update_comida(request, pk):
    """
    Vista para actualizar una comida existente.
    """
    comida = get_object_or_404(Comida, pk=pk)
    if request.method == 'POST':
        form = ComidaForm(request.POST, instance=comida)
        if form.is_valid():
            form.save()
            return redirect('comidas:index')
    else:
        form = ComidaForm(instance=comida)
    return render(request, 'update.html', {'form': form})

def delete_comida(request, pk):
    """
    Vista para eliminar una comida existente.
    """
    comida = get_object_or_404(Comida, pk=pk)
    if request.method == 'POST':
        comida.delete()
        return redirect('comidas:index')
    return render(request, 'delete.html', {'comida': comida})
