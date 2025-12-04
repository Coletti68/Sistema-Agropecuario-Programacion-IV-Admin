from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from ..models import Usuario, Rol


def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, "usuarios/listar.html", {"usuarios": usuarios})


def crear_usuario(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        telefono = request.POST.get("telefono")
        dni = request.POST.get("dni")
        direccion = request.POST.get("direccion")
        password = request.POST.get("password")
        rolid = request.POST.get("rolid")

        if Usuario.objects.filter(email=email).exists():
            return JsonResponse({'success': False, 'message': 'El correo electrónico ya está registrado.'})
        
        if dni and Usuario.objects.filter(dni=dni).exists():
             return JsonResponse({'success': False, 'message': 'El DNI ya está registrado.'})

        try:
            Usuario.objects.create(
                nombre=nombre,
                email=email,
                telefono=telefono,
                dni=dni,
                direccion=direccion,
                passwordhash=make_password(password),
                rol_id=rolid,
                activo=True
            )
            return JsonResponse({'success': True, 'message': 'Usuario creado exitosamente.'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': f'Error al crear usuario: {str(e)}'})

    roles = Rol.objects.filter(activo=True)
    return render(request, "usuarios/crear.html", {"roles": roles})


def editar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)

    if request.method == "POST":
        usuario.nombre = request.POST.get("nombre")
        usuario.email = request.POST.get("email")
        usuario.telefono = request.POST.get("telefono")
        usuario.dni = request.POST.get("dni")
        usuario.direccion = request.POST.get("direccion")

        rolid = request.POST.get("rolid")
        if rolid:
            usuario.rol_id = rolid

        if request.POST.get("password"):
            usuario.passwordhash = make_password(request.POST.get("password"))

        usuario.save()
        return redirect("listar_usuarios")

    roles = Rol.objects.filter(activo=True)
    return render(request, "usuarios/editar.html", {"usuario": usuario, "roles": roles})


def desactivar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    usuario.activo = False
    usuario.save()
    return redirect("listar_usuarios")


def activar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    usuario.activo = True
    usuario.save()
    return redirect("listar_usuarios")
