from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from ..models import HistorialEstadoSolicitud, Solicitud, Usuario, EstadoSolicitud

# GET /historial-estados (admin)
def listar_historial_estados(request):
    historial = HistorialEstadoSolicitud.objects.select_related('solicitud', 'estadosolicitud', 'usuario').all()
    data = [{
        'id': h.pk,
        'solicitud': h.solicitud.pk,
        'estado': h.estadosolicitud.nombre,
        'usuario': h.usuario.nombre if h.usuario else None,
        'fecha': h.fecha
    } for h in historial]
    return JsonResponse(data, safe=False)

# GET /historial-estados/solicitud/:solicitudId
def historial_por_solicitud(request, solicitudId):
    solicitud = get_object_or_404(Solicitud, pk=solicitudId)
    historial = HistorialEstadoSolicitud.objects.filter(solicitud=solicitud).select_related('estadosolicitud', 'usuario')
    data = [{
        'id': h.pk,
        'estado': h.estadosolicitud.nombre,
        'usuario': h.usuario.nombre if h.usuario else None,
        'fecha': h.fecha
    } for h in historial]
    return JsonResponse({'solicitud': solicitud.pk, 'historial': data})

# GET /historial-estados/usuario/:usuarioId
def historial_por_usuario(request, usuarioId):
    usuario = get_object_or_404(Usuario, pk=usuarioId)
    historial = HistorialEstadoSolicitud.objects.filter(usuario=usuario).select_related('solicitud', 'estadosolicitud')
    data = [{
        'id': h.pk,
        'solicitud': h.solicitud.pk,
        'estado': h.estadosolicitud.nombre,
        'fecha': h.fecha
    } for h in historial]
    return JsonResponse({'usuario': usuario.nombre, 'historial': data})

# GET /historial-estados/estado/:estadoId
def historial_por_estado(request, estadoId):
    estado = get_object_or_404(EstadoSolicitud, pk=estadoId)
    historial = HistorialEstadoSolicitud.objects.filter(estadosolicitud=estado).select_related('solicitud', 'usuario')
    data = [{
        'id': h.pk,
        'solicitud': h.solicitud.pk,
        'usuario': h.usuario.nombre if h.usuario else None,
        'fecha': h.fecha
    } for h in historial]
    return JsonResponse({'estado': estado.nombre, 'historial': data})

