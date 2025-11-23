from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from ..models import Solicitud, SolicitudDetalle, EstadoSolicitud, HistorialEstadoSolicitud, Usuario

# GET /solicitudes
def listar_solicitudes(request):
    solicitudes = Solicitud.objects.select_related('usuario', 'estadosolicitudid').all()
    return render(request, 'solicitudes/listar.html', {'solicitudes': solicitudes})

# GET /solicitudes/detalles
def listar_solicitudes_con_detalles(request):
    solicitudes = Solicitud.objects.select_related('usuario', 'estadosolicitudid').prefetch_related('solicituddetalle_set')
    data = []
    for s in solicitudes:
        detalles = [{
            'insumo': d.insumo.nombre,
            'cantidad': d.cantidad,
            'precio_unitario': d.preciounitario
        } for d in s.solicituddetalle_set.all()]
        data.append({
            'id': s.pk,
            'usuario': s.usuario.nombre,
            'estado': s.estadosolicitudid.nombre,
            'detalles': detalles
        })
    return JsonResponse(data, safe=False)

# GET /solicitudes/:id
def obtener_solicitud_por_id(request, pk):
    solicitud = get_object_or_404(Solicitud.objects.select_related('usuario', 'estadosolicitudid'), pk=pk)
    detalles = [{
        'insumo': d.insumo.nombre,
        'cantidad': d.cantidad,
        'precio_unitario': d.preciounitario
    } for d in solicitud.solicituddetalle_set.all()]
    return JsonResponse({
        'id': solicitud.pk,
        'usuario': solicitud.usuario.nombre,
        'estado': solicitud.estadosolicitudid.nombre,
        'detalles': detalles
    })

# PUT /solicitudes/:id/estado
def cambiar_estado_solicitud(request, pk):
    solicitud = get_object_or_404(Solicitud, pk=pk)
    if request.method == 'POST':
        estado_id = request.POST.get('estadoid')
        if not estado_id:
            return JsonResponse({'error': 'Falta estadoid'}, status=400)
        try:
            estado = EstadoSolicitud.objects.get(pk=estado_id)
        except EstadoSolicitud.DoesNotExist:
            return JsonResponse({'error': 'Estado no encontrado'}, status=404)
        solicitud.estadosolicitudid = estado
        solicitud.save()
        HistorialEstadoSolicitud.objects.create(
            solicitud=solicitud,
            estadosolicitud=estado,
            usuario=request.user if request.user.is_authenticated else None
        )
        return JsonResponse({'mensaje': 'Estado actualizado'})
    return JsonResponse({'error': 'Método inválido'}, status=405)

# GET /solicitudes/estado/:estadoId
def filtrar_solicitudes_por_estado(request, estadoId):
    solicitudes = Solicitud.objects.filter(estadosolicitudid_id=estadoId).select_related('usuario', 'estadosolicitudid')
    data = [{
        'id': s.pk,
        'usuario': s.usuario.nombre,
        'estado': s.estadosolicitudid.nombre
    } for s in solicitudes]
    return JsonResponse(data, safe=False)

# GET /solicitudes/usuario/:usuarioId
def solicitudes_por_usuario(request, usuarioId):
    solicitudes = Solicitud.objects.filter(usuario_id=usuarioId).select_related('estadosolicitudid')
    data = [{
        'id': s.pk,
        'estado': s.estadosolicitudid.nombre,
        'fecha': s.fechasolicitud
    } for s in solicitudes]
    return JsonResponse(data, safe=False)

# GET /solicitudes/:id/historial
def historial_solicitud(request, pk):
    historial = HistorialEstadoSolicitud.objects.filter(solicitud_id=pk).select_related('estadosolicitud', 'usuario')
    data = [{
        'estado': h.estadosolicitud.nombre,
        'usuario': h.usuario.nombre if h.usuario else None,
        'fecha': h.fecha
    } for h in historial]
    return JsonResponse(data, safe=False)
