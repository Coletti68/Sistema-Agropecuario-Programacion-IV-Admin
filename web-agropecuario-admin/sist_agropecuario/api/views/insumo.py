from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from ..models import Insumo, Proveedor
from django.db.models import F

# Listar insumos
# insumo.py -> listar_insumos
def listar_insumos(request):
    insumos = Insumo.objects.all()
    hay_critico = any(insumo.stock <= insumo.stock_minimo for insumo in insumos)
    for insumo in insumos:
        insumo.critico = insumo.stock <= insumo.stock_minimo
    return render(request, 'insumos/listar.html', {'insumos': insumos, 'hay_critico': hay_critico})


# Crear insumo
def crear_insumo(request):
    proveedores = Proveedor.objects.filter(activo=True)
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        proveedor_id = request.POST.get('proveedor_id')
        stock = request.POST.get('stock') or 0
        stock_minimo = request.POST.get('stock_minimo') or 0

        if not nombre or not precio:
            messages.error(request, "Nombre y precio son obligatorios")
            return render(request, 'insumos/crear.html', {'proveedores': proveedores})

        Insumo.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            proveedor_id=proveedor_id,
            stock=stock,
            stock_minimo=stock_minimo,
            activo=True
        )
        messages.success(request, "Insumo creado correctamente")
        return redirect('listar_insumos')

    return render(request, 'insumos/crear.html', {'proveedores': proveedores})

# Editar insumo
def editar_insumo(request, pk):
    insumo = get_object_or_404(Insumo, pk=pk)
    proveedores = Proveedor.objects.filter(activo=True)
    if request.method == 'POST':
        insumo.nombre = request.POST.get('nombre') or insumo.nombre
        insumo.descripcion = request.POST.get('descripcion') or insumo.descripcion
        insumo.precio = request.POST.get('precio') or insumo.precio
        insumo.proveedor_id = request.POST.get('proveedor_id') or insumo.proveedor_id
        insumo.stock = request.POST.get('stock') or insumo.stock
        insumo.stock_minimo = request.POST.get('stock_minimo') or insumo.stock_minimo
        insumo.save()
        messages.success(request, "Insumo actualizado correctamente")
        return redirect('listar_insumos')

    return render(request, 'insumos/editar.html', {'insumo': insumo, 'proveedores': proveedores})

# Desactivar insumo
def desactivar_insumo(request, pk):
    insumo = get_object_or_404(Insumo, pk=pk)
    insumo.activo = False
    insumo.save()
    messages.success(request, f"Insumo '{insumo.nombre}' desactivado")
    return redirect('listar_insumos')

# Activar insumo
def activar_insumo(request, pk):
    insumo = get_object_or_404(Insumo, pk=pk)
    insumo.activo = True
    insumo.save()
    messages.success(request, f"Insumo '{insumo.nombre}' activado")
    return redirect('listar_insumos')

# Insumos con stock crítico
def insumos_stock_critico(request):
    insumos = Insumo.objects.filter(activo=True, stock__lt=F('stock_minimo'))
    return render(request, 'insumos/stock_critico.html', {'insumos': insumos})
