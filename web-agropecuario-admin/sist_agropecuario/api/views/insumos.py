from django.shortcuts import render, redirect, get_object_or_404
from ..models import Insumo

def listar_insumos(request):
    insumos = Insumo.objects.filter(estado=True)
    return render(request, 'insumos/listar.html', {'insumos': insumos})

def crear_insumo(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        Insumo.objects.create(nombre=nombre, precio=precio, estado=True)
        return redirect('listar_insumos')
    return render(request, 'insumos/crear.html')
