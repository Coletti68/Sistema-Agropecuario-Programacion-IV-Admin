from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from ..models import ComprobanteEntrega, Solicitud, Usuario

# GET /comprobantes (admin)
def listar_comprobantes(request):
    comprobantes = ComprobanteEntrega.objects.select_related('solicitud', 'usuario').all()
    return render(request, 'comprobantes/listar.html', {'comprobantes': comprobantes})

# POST /comprobantes (generar entrega)
def generar_comprobante(request):
    if request.method == 'POST':
        solicitud_id = request.POST.get('solicitudid')
        usuario_id = request.POST.get('usuarioid')
        observaciones = request.POST.get('observaciones')

        if not solicitud_id or not usuario_id:
            return JsonResponse({'error': 'Campos obligatorios faltantes'}, status=400)

        solicitud = get_object_or_404(Solicitud, pk=solicitud_id)
        usuario = get_object_or_404(Usuario, pk=usuario_id)

        comprobante = ComprobanteEntrega.objects.create(
            solicitud=solicitud,
            usuario=usuario,
            observaciones=observaciones
        )
        return JsonResponse({'mensaje': 'Comprobante generado', 'id': comprobante.pk})
    return JsonResponse({'error': 'Método inválido'}, status=405)

# GET /comprobantes/:id (admin)
def ver_comprobante(request, pk):
    comprobante = get_object_or_404(ComprobanteEntrega.objects.select_related('solicitud', 'usuario'), pk=pk)
    data = {
        'id': comprobante.pk,
        'solicitud': comprobante.solicitud.pk,
        'usuario': comprobante.usuario.nombre,
        'fecha': comprobante.fecha,
        'observaciones': comprobante.observaciones
    }
    return JsonResponse(data)
