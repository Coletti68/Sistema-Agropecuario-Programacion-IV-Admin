from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from ..models import UsuarioCultivo, Usuario, Cultivo
from django.http import JsonResponse
# ==========================
# Panel de asignaciones
# ==========================

def panel_usuarios_cultivos(request):
    cultivo_id = request.GET.get('cultivoid')
    usuario_id = request.GET.get('usuarioid')

    asignaciones = UsuarioCultivo.objects.select_related('usuarioid', 'cultivoid')

    if cultivo_id:
        asignaciones = asignaciones.filter(cultivoid_id=cultivo_id)
    if usuario_id:
        asignaciones = asignaciones.filter(usuarioid_id=usuario_id)

    usuarios = Usuario.objects.filter(activo=True)
    cultivos = Cultivo.objects.filter(activo=True)

    return render(request, 'usuario_cultivo/usuario_panel.html', {
        'asignaciones': asignaciones,
        'usuarios': usuarios,
        'cultivos': cultivos,
    })


# ==========================
# Crear asignación
# ==========================
def crear_usuariocultivo(request):
    if request.method == 'POST':
        usuario_id = request.POST.get('usuarioid')
        cultivo_id = request.POST.get('cultivoid')
        latitud = request.POST.get('latitud')
        longitud = request.POST.get('longitud')
        fechasiembra = request.POST.get('fechasiembra')

        if not usuario_id or not cultivo_id:
            messages.error(request, "Debe seleccionar un usuario y un cultivo.")
            return redirect('panel_usuarios_cultivos')

        UsuarioCultivo.objects.create(
            usuarioid_id=usuario_id,
            cultivoid_id=cultivo_id,
            latitud=latitud,
            longitud=longitud,
            fechasiembra=fechasiembra
        )
        messages.success(request, "Asignación creada correctamente.")
        return redirect('panel_usuarios_cultivos')

    usuarios = Usuario.objects.filter(activo=True)
    cultivos = Cultivo.objects.filter(activo=True)
    return render(request, 'usuario_cultivo/crear.html', {
        'usuarios': usuarios,
        'cultivos': cultivos
    })


# ==========================
# Editar asignación
# ==========================
def editar_usuariocultivo(request, pk):
    asignacion = get_object_or_404(UsuarioCultivo, pk=pk)

    if request.method == 'POST':
        asignacion.usuarioid_id = request.POST.get('usuarioid') or asignacion.usuarioid_id
        asignacion.cultivoid_id = request.POST.get('cultivoid') or asignacion.cultivoid_id
        asignacion.latitud = request.POST.get('latitud') or asignacion.latitud
        asignacion.longitud = request.POST.get('longitud') or asignacion.longitud
        asignacion.fechasiembra = request.POST.get('fechasiembra') or asignacion.fechasiembra
        asignacion.save()
        messages.success(request, "Asignación actualizada correctamente.")
        return redirect('panel_usuarios_cultivos')

    usuarios = Usuario.objects.filter(activo=True)
    cultivos = Cultivo.objects.filter(activo=True)
    return render(request, 'usuario_cultivo/editar.html', {
        'asignacion': asignacion,
        'usuarios': usuarios,
        'cultivos': cultivos
    })


# ==========================
# Desactivar asignación
# ==========================
def desactivar_usuariocultivo(request, pk):
    asignacion = get_object_or_404(UsuarioCultivo, pk=pk)
    asignacion.activo = False
    asignacion.save()
    messages.success(request, "Asignación desactivada.")
    return redirect('panel_usuarios_cultivos')


# ==========================
# Activar asignación
# ==========================
def activar_usuariocultivo(request, pk):
    asignacion = get_object_or_404(UsuarioCultivo, pk=pk)
    asignacion.activo = True
    asignacion.save()
    messages.success(request, "Asignación activada.")
    return redirect('panel_usuarios_cultivos')


# GET /usuariocultivos/usuario/:usuarioId
def cultivos_por_usuario(request, usuarioId):
    usuario = get_object_or_404(Usuario, pk=usuarioId)
    asignaciones = UsuarioCultivo.objects.filter(usuarioid=usuario, activo=True).select_related('cultivoid')
    data = [{
        'id': a.usuariocultivoid,
        'cultivo': a.cultivoid.nombre,
        'latitud': a.latitud,
        'longitud': a.longitud,
        'fechasiembra': a.fechasiembra
    } for a in asignaciones]
    print("JSON asignaciones:", data)  # debug
    return JsonResponse(data, safe=False)
# GET /usuariocultivos/cultivo/:cultivoId
def usuarios_por_cultivo(request, cultivoId):
    cultivo = get_object_or_404(Cultivo, pk=cultivoId)
    asignaciones = UsuarioCultivo.objects.filter(cultivoid=cultivo)
    data = [{
        'id': a.usuariocultivoid,
        'usuario': a.usuarioid.nombre,
        'latitud': a.latitud,
        'longitud': a.longitud,
        'fechasiembra': a.fechasiembra
    } for a in asignaciones]
    return JsonResponse(data, safe=False)
