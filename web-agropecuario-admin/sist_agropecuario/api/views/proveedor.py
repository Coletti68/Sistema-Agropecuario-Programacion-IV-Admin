from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from ..models import Proveedor, Insumo

# GET /proveedores
def listar_proveedores(request):
    proveedores = Proveedor.objects.filter(activo=True)
    return render(request, 'proveedores/listar.html', {'proveedores': proveedores})

# POST /proveedores
def crear_proveedor(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        contacto = request.POST.get('contacto')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')

        if not nombre:
            return JsonResponse({'error': 'Nombre obligatorio'}, status=400)

        Proveedor.objects.create(
            nombre=nombre,
            contacto=contacto,
            telefono=telefono,
            email=email,
            activo=True
        )
        return JsonResponse({'mensaje': 'Proveedor creado correctamente'})
    return render(request, 'proveedores/crear.html')

# PUT /proveedores/:id
def editar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.nombre = request.POST.get('nombre') or proveedor.nombre
        proveedor.contacto = request.POST.get('contacto') or proveedor.contacto
        proveedor.telefono = request.POST.get('telefono') or proveedor.telefono
        proveedor.email = request.POST.get('email') or proveedor.email
        proveedor.save()
        return JsonResponse({'mensaje': 'Proveedor actualizado'})
    return render(request, 'proveedores/editar.html', {'proveedor': proveedor})

# DELETE /proveedores/:id
def desactivar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    proveedor.activo = False
    proveedor.save()
    return JsonResponse({'mensaje': 'Proveedor desactivado'})

# PUT /proveedores/:id/activar
def activar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    proveedor.activo = True
    proveedor.save()
    return JsonResponse({'mensaje': 'Proveedor activado'})

# GET /proveedores/:id/insumos
def listar_insumos_por_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk, activo=True)
    insumos = Insumo.objects.filter(proveedor=proveedor, activo=True)
    data = [{
        'id': i.pk,
        'nombre': i.nombre,
        'precio': i.precio,
        'stock': i.stock
    } for i in insumos]
    return JsonResponse({'proveedor': proveedor.nombre, 'insumos': data})
