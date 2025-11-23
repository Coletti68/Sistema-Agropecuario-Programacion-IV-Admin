from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from ..models import Insumo
from django.db.models import F

# GET /insumos
def listar_insumos(request):
    insumos = Insumo.objects.filter(activo=True)
    return render(request, 'insumos/listar.html', {'insumos': insumos})

# POST /insumos
def crear_insumo(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        proveedor_id = request.POST.get('proveedorid')
        stock = request.POST.get('stock') or 0
        stock_minimo = request.POST.get('stock_minimo') or 0

        if not nombre or not precio:
            return JsonResponse({'error': 'Nombre y precio son obligatorios'}, status=400)

        Insumo.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            proveedor_id=proveedor_id,
            stock=stock,
            stock_minimo=stock_minimo,
            activo=True
        )
        return JsonResponse({'mensaje': 'Insumo creado correctamente'})
    return render(request, 'insumos/crear.html')

# PUT /insumos/:id
def editar_insumo(request, pk):
    insumo = get_object_or_404(Insumo, pk=pk)
    if request.method == 'POST':
        insumo.nombre = request.POST.get('nombre') or insumo.nombre
        insumo.descripcion = request.POST.get('descripcion') or insumo.descripcion
        insumo.precio = request.POST.get('precio') or insumo.precio
        insumo.proveedor_id = request.POST.get('proveedorid') or insumo.proveedor_id
        insumo.stock = request.POST.get('stock') or insumo.stock
        insumo.stock_minimo = request.POST.get('stock_minimo') or insumo.stock_minimo
        insumo.save()
        return JsonResponse({'mensaje': 'Insumo actualizado'})
    return render(request, 'insumos/editar.html', {'insumo': insumo})

# DELETE /insumos/:id
def desactivar_insumo(request, pk):
    insumo = get_object_or_404(Insumo, pk=pk)
    insumo.activo = False
    insumo.save()
    return JsonResponse({'mensaje': 'Insumo desactivado'})

# PUT /insumos/:id/activar
def activar_insumo(request, pk):
    insumo = get_object_or_404(Insumo, pk=pk)
    insumo.activo = True
    insumo.save()
    return JsonResponse({'mensaje': 'Insumo activado'})


# GET /insumos/stock-critico
def insumos_stock_critico(request):
    insumos = Insumo.objects.filter(activo=True, stock__lt=F('stock_minimo'))
    data = [{
        'id': i.pk,
        'nombre': i.nombre,
        'stock': i.stock,
        'stock_minimo': i.stock_minimo
    } for i in insumos]
    return JsonResponse(data, safe=False)

