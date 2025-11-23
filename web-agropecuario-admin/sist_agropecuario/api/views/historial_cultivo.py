from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from ..models import HistorialCultivo, UsuarioCultivo, Usuario

# GET /historial (admin)  
def listar_historial(request):
    historial = HistorialCultivo.objects.select_related('usuariocultivo', 'usuariocultivo__usuario').all()
    data = [{
        'id': h.pk,
        'usuario': h.usuariocultivo.usuario.nombre,
        'cultivo': h.usuariocultivo.cultivo.nombre,
        'fecha': h.fecha,
        'observaciones': h.observaciones
    } for h in historial]
    return JsonResponse(data, safe=False)

# GET /historial/usuario/:usuarioId (admin) todo el historial de un productor, sin importar qué cultivo.
def historial_por_usuario(request, usuarioId):
    usuario = get_object_or_404(Usuario, pk=usuarioId)
    historial = HistorialCultivo.objects.filter(usuariocultivo__usuario=usuario)
    data = [{
        'id': h.pk,
        'cultivo': h.usuariocultivo.cultivo.nombre,
        'fecha': h.fecha,
        'observaciones': h.observaciones
    } for h in historial]
    return JsonResponse({'usuario': usuario.nombre, 'historial': data})

# GET /historial/asignacion/:usuarioCultivoId (admin) historial de un cultivo específico asignado a un productor.
def historial_por_asignacion(request, usuarioCultivoId):
    asignacion = get_object_or_404(UsuarioCultivo, pk=usuarioCultivoId)
    historial = HistorialCultivo.objects.filter(usuariocultivo=asignacion)
    data = [{
        'id': h.pk,
        'fecha': h.fecha,
        'observaciones': h.observaciones
    } for h in historial]
    return JsonResponse({'cultivo': asignacion.cultivo.nombre, 'historial': data})

# GET /historial/detalles/:usuarioCultivoId (admin) lo mismo que asignación, pero con datos extra (usuario, cultivo, coordenadas).
def historial_detalles(request, usuarioCultivoId):
    asignacion = get_object_or_404(UsuarioCultivo.objects.select_related('usuario', 'cultivo'), pk=usuarioCultivoId)
    historial = HistorialCultivo.objects.filter(usuariocultivo=asignacion)
    data = [{
        'id': h.pk,
        'fecha': h.fecha,
        'observaciones': h.observaciones,
        'usuario': asignacion.usuario.nombre,
        'cultivo': asignacion.cultivo.nombre,
        'latitud': asignacion.latitud,
        'longitud': asignacion.longitud
    } for h in historial]
    return JsonResponse({'cultivo': asignacion.cultivo.nombre, 'usuario': asignacion.usuario.nombre, 'historial': data})
