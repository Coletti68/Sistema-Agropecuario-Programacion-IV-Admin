from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from ..models import Usuario, Rol

# GET /usuarios
def listar_usuarios(request):
    usuarios = Usuario.objects.filter(activo=True).select_related('rol')
    return render(request, 'usuarios/listar.html', {'usuarios': usuarios})

# GET /usuarios/:id
def obtener_usuario_por_id(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk, activo=True)
    return JsonResponse({
        'id': usuario.pk,
        'nombre': usuario.nombre,
        'email': usuario.email,
        'telefono': usuario.telefono,
        'dni': usuario.dni,
        'direccion': usuario.direccion,
        'rol': usuario.rol.nombre
    })

# GET /usuarios?rol=productor
def obtener_usuarios_por_rol(request):
    rol_nombre = request.GET.get('rol')
    if not rol_nombre:
        return JsonResponse({'error': 'Falta parámetro rol'}, status=400)
    try:
        rol = Rol.objects.get(nombre=rol_nombre, activo=True)
    except Rol.DoesNotExist:
        return JsonResponse({'error': 'Rol no encontrado'}, status=404)
    usuarios = Usuario.objects.filter(rol=rol, activo=True)
    data = [{
        'id': u.pk,
        'nombre': u.nombre,
        'email': u.email
    } for u in usuarios]
    return JsonResponse(data, safe=False)

# POST /usuarios
def crear_usuario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        dni = request.POST.get('dni')
        direccion = request.POST.get('direccion')
        password = request.POST.get('password')
        rol_id = request.POST.get('rolid')

        if not nombre or not email or not password or not rol_id:
            return JsonResponse({'error': 'Campos obligatorios faltantes'}, status=400)

        Usuario.objects.create(
            nombre=nombre,
            email=email,
            telefono=telefono,
            dni=dni,
            direccion=direccion,
            passwordhash=make_password(password),
            rol_id=rol_id,
            activo=True
        )
        return JsonResponse({'mensaje': 'Usuario creado correctamente'})
    return render(request, 'usuarios/crear.html')

# PUT /usuarios/:id
def editar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.nombre = request.POST.get('nombre') or usuario.nombre
        usuario.email = request.POST.get('email') or usuario.email
        usuario.telefono = request.POST.get('telefono') or usuario.telefono
        usuario.dni = request.POST.get('dni') or usuario.dni
        usuario.direccion = request.POST.get('direccion') or usuario.direccion
        rol_id = request.POST.get('rolid')
        if rol_id:
            usuario.rol_id = rol_id
        if request.POST.get('password'):
            usuario.passwordhash = make_password(request.POST.get('password'))
        usuario.save()
        return JsonResponse({'mensaje': 'Usuario actualizado'})
    return render(request, 'usuarios/editar.html', {'usuario': usuario})

# PUT /usuarios/:id/desactivar
def desactivar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    usuario.activo = False
    usuario.save()
    return JsonResponse({'mensaje': 'Usuario desactivado'})

# PUT /usuarios/:id/activar
def activar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    usuario.activo = True
    usuario.save()
    return JsonResponse({'mensaje': 'Usuario activado'})

