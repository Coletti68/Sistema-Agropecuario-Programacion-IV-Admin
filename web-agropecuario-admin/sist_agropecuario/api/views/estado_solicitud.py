from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from ..models import Solicitud, EstadoSolicitud, HistorialEstadoSolicitud

# GET /solicitudes/:id/estados
def ver_historial_estados(request, id):
    solicitud = get_object_or_404(Solicitud, pk=id)
    historial = HistorialEstadoSolicitud.objects.filter(solicitud=solicitud).select_related('estadosolicitud', 'usuario')
    data = [{
        'estado': h.estadosolicitud.nombre,
        'usuario': h.usuario.nombre if h.usuario else None,
        'fecha': h.fecha
    } for h in historial]
    return JsonResponse({'solicitud': solicitud.pk, 'historial': data})

# POST /solicitudes/:id/estados (admin)
def cambiar_estado(request, id):
    solicitud = get_object_or_404(Solicitud, pk=id)
    if request.method == 'POST':
        estado_id = request.POST.get('estadoid')
        if not estado_id:
            return JsonResponse({'error': 'Falta estadoid'}, status=400)
        try:
            estado = EstadoSolicitud.objects.get(pk=estado_id)
        except EstadoSolicitud.DoesNotExist:
            return JsonResponse({'error': 'Estado no encontrado'}, status=404)

        solicitud.estadosolicitudid = estado   # usar el nombre real del campo
        solicitud.save()

        HistorialEstadoSolicitud.objects.create(
            solicitud=solicitud,
            estadosolicitud=estado,
            usuario=request.user if request.user.is_authenticated else None
        )
        return JsonResponse({'mensaje': 'Estado actualizado'})
    return JsonResponse({'error': 'Método inválido'}, status=405)

