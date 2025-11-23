from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from ..models import Solicitud, SolicitudDetalle, Insumo

# GET /solicitudes/:id/detalle
def ver_detalles_solicitud(request, id):
    solicitud = get_object_or_404(Solicitud, pk=id)
    detalles = [{
        'id': d.pk,
        'insumo': d.insumo.nombre,
        'cantidad': d.cantidad,
        'precio_unitario': d.preciounitario
    } for d in solicitud.solicituddetalle_set.filter(activo=True)]
    return JsonResponse(detalles, safe=False)

# POST /solicitudes/:id/detalle
def agregar_item_solicitud(request, id):
    solicitud = get_object_or_404(Solicitud, pk=id)
    if request.method == 'POST':
        insumo_id = request.POST.get('insumoid')
        cantidad = request.POST.get('cantidad')
        precio_unitario = request.POST.get('preciounitario')

        if not insumo_id or not cantidad or not precio_unitario:
            return JsonResponse({'error': 'Campos obligatorios faltantes'}, status=400)

        insumo = get_object_or_404(Insumo, pk=insumo_id)
        detalle = SolicitudDetalle.objects.create(
            solicitud=solicitud,
            insumo=insumo,
            cantidad=cantidad,
            preciounitario=precio_unitario,
            activo=True
        )
        return JsonResponse({'mensaje': 'Ítem agregado', 'id': detalle.pk})
    return JsonResponse({'error': 'Método inválido'}, status=405)

# PUT /solicitudes/:id/detalle/:detalleid
def editar_item_solicitud(request, id, detalleid):
    detalle = get_object_or_404(SolicitudDetalle, pk=detalleid, solicitud_id=id)
    if request.method == 'POST':
        detalle.cantidad = request.POST.get('cantidad') or detalle.cantidad
        detalle.preciounitario = request.POST.get('preciounitario') or detalle.preciounitario
        detalle.save()
        return JsonResponse({'mensaje': 'Ítem actualizado'})
    return JsonResponse({'error': 'Método inválido'}, status=405)

# DELETE /solicitudes/:id/detalle/:detalleid
def eliminar_item_solicitud(request, id, detalleid):
    detalle = get_object_or_404(SolicitudDetalle, pk=detalleid, solicitud_id=id)
    detalle.activo = False
    detalle.save()
    return JsonResponse({'mensaje': 'Ítem eliminado'})
