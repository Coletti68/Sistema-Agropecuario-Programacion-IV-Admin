from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib import messages
from ..models import Proveedor, Insumo

# GET /proveedores
def listar_proveedores(request):
    proveedores = Proveedor.objects.all()  # mostramos todos
    return render(request, 'proveedores/listar.html', {'proveedores': proveedores})

# POST /proveedores
def crear_proveedor(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        contacto = request.POST.get('contacto')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')

        if not nombre:
            return JsonResponse({'success': False, 'message': 'El nombre es obligatorio'})

        if email and Proveedor.objects.filter(email=email).exists():
            return JsonResponse({'success': False, 'message': 'El correo electrónico ya está registrado.'})

        try:
            Proveedor.objects.create(
                nombre=nombre,
                contacto=contacto,
                telefono=telefono,
                email=email,
                activo=True
            )
            return JsonResponse({'success': True, 'message': 'Proveedor creado correctamente'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': f'Error al crear proveedor: {str(e)}'})

    return render(request, 'proveedores/crear.html')


# POST /proveedores/:id
def editar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.nombre = request.POST.get('nombre') or proveedor.nombre
        proveedor.contacto = request.POST.get('contacto') or proveedor.contacto
        proveedor.telefono = request.POST.get('telefono') or proveedor.telefono
        proveedor.email = request.POST.get('email') or proveedor.email
        proveedor.save()
        messages.success(request, "Proveedor actualizado correctamente")
        return redirect('listar_proveedores')

    return render(request, 'proveedores/editar.html', {'proveedor': proveedor})


# GET /proveedores/:id/desactivar
def desactivar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    proveedor.activo = False
    proveedor.save()
    messages.success(request, "Proveedor desactivado correctamente")
    return redirect('listar_proveedores')


# GET /proveedores/:id/activar
def activar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    proveedor.activo = True
    proveedor.save()
    messages.success(request, "Proveedor activado correctamente")
    return redirect('listar_proveedores')


# GET /proveedores/:id/insumos
def listar_insumos_por_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    insumos = Insumo.objects.filter(proveedor=proveedor)
    return render(request, 'insumos/listar_por_proveedor.html', {'proveedor': proveedor, 'insumos': insumos})
