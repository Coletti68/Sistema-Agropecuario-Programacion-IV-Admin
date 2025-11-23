from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from ..models import Pago, Usuario

# GET /pagos (admin)
def listar_pagos(request):
    pagos = Pago.objects.select_related('usuario').all()
    return render(request, 'pagos/listar.html', {'pagos': pagos})

# POST /pagos (registrar pago)
def registrar_pago(request):
    if request.method == 'POST':
        usuario_id = request.POST.get('usuarioid')
        monto = request.POST.get('monto')
        estado = request.POST.get('estado')  # ahora es texto

        if not usuario_id or not monto or not estado:
            return JsonResponse({'error': 'Campos obligatorios faltantes'}, status=400)

        usuario = get_object_or_404(Usuario, pk=usuario_id)

        Pago.objects.create(
            usuario=usuario,
            monto=monto,
            estado_pago=estado  # asignación directa al CharField
        )
        return JsonResponse({'mensaje': 'Pago registrado correctamente'})
    return JsonResponse({'error': 'Método inválido'}, status=405)

# PUT /pagos/:id (admin)
def actualizar_estado_pago(request, pk):
    pago = get_object_or_404(Pago, pk=pk)
    if request.method == 'POST':
        estado = request.POST.get('estado')  # texto
        if not estado:
            return JsonResponse({'error': 'Falta estado'}, status=400)
        pago.estado_pago = estado
        pago.save()
        return JsonResponse({'mensaje': 'Estado de pago actualizado'})
    return JsonResponse({'error': 'Método inválido'}, status=405)

# GET /pagos/usuario/:usuarioId (admin)
def listar_pagos_por_usuario(request, usuarioId):
    usuario = get_object_or_404(Usuario, pk=usuarioId)
    pagos = Pago.objects.filter(usuario=usuario)
    data = [{
        'id': p.pk,
        'monto': p.monto,
        'fecha': p.fecha_pago,   # coincide con el modelo
        'estado': p.estado_pago  # texto directo
    } for p in pagos]
    return JsonResponse({'usuario': usuario.nombre, 'pagos': data})