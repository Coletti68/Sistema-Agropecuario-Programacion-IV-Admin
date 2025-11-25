from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from decimal import Decimal

from ..models import (
    Solicitud,
    SolicitudDetalle,
    EstadoSolicitud,
    HistorialEstadoSolicitud,
    ComprobanteEntrega
)


# -----------------------------
# LISTAR SOLICITUDES
# -----------------------------
def listar_solicitudes(request):
    estado_id = request.GET.get("estadoid")
    solicitudes = Solicitud.objects.select_related("usuario", "estadosolicitudid")

    if estado_id:
        solicitudes = solicitudes.filter(estadosolicitudid_id=estado_id)

    estados = EstadoSolicitud.objects.all()

    return render(request, "solicitudes/listar.html", {
        "solicitudes": solicitudes,
        "estados": estados,
        "estado_seleccionado": int(estado_id) if estado_id else None,
        "nombre": "Administrador",  # Ajustar según tu autenticación
    })
def cambiar_estado_solicitud(request, pk):
    solicitud = get_object_or_404(Solicitud, pk=pk)
    if request.method == "POST":
        estado_id = request.POST.get("estadoid")
        nuevo_estado = get_object_or_404(EstadoSolicitud, pk=estado_id)
        solicitud.estadosolicitudid = nuevo_estado
        solicitud.save()

        # Guardar historial
        HistorialEstadoSolicitud.objects.create(
            solicitud=solicitud,
            estadosolicitud=nuevo_estado,
            usuario=request.user if request.user.is_authenticated else None
        )

    return redirect("listar_solicitudes")


# -----------------------------
# DETALLE DE SOLICITUD
# -----------------------------
def detalle_solicitud(request, pk):
    solicitud = get_object_or_404(Solicitud, pk=pk)
    detalles = SolicitudDetalle.objects.filter(solicitud=solicitud)
    
    detalles_list = []
    total_general = 0
    for item in detalles:
        item.subtotal = item.cantidad * item.preciounitario  # calculamos subtotal
        total_general += item.subtotal
        detalles_list.append(item)

    return render(request, "solicitudes/detalle.html", {
        "solicitud": solicitud,
        "detalles": detalles_list,
        "total_general": total_general,
    })


# -----------------------------
# PROCESAR SOLICITUD
# -----------------------------
def procesar_solicitud(request, pk):
    solicitud = get_object_or_404(Solicitud, pk=pk)

    # Obtener o crear estado "ENTREGADA"
    estado_entregado, _ = EstadoSolicitud.objects.get_or_create(nombre="ENTREGADA")

    # Verificar si ya está procesada
    if solicitud.estadosolicitudid == estado_entregado:
        messages.warning(request, "Esta solicitud ya fue procesada.")
        return redirect("listar_solicitudes")

    detalles = solicitud.solicituddetalle_set.filter(activo=True)

    # Verificar stock
    for item in detalles:
        if item.cantidad > item.insumo.stock:
            messages.error(request, f"Stock insuficiente para el insumo {item.insumo.nombre}.")
            return redirect("listar_solicitudes")

    # Descontar stock
    for item in detalles:
        item.insumo.stock -= item.cantidad
        item.insumo.save()

    # Cambiar estado de la solicitud
    solicitud.estadosolicitudid = estado_entregado
    solicitud.save()

    # Registrar historial del estado
    HistorialEstadoSolicitud.objects.create(
        solicitud=solicitud,
        estadosolicitud=estado_entregado,
        usuario=request.user if request.user.is_authenticated else None
    )

    # Calcular total
    total = sum(item.cantidad * item.preciounitario for item in detalles)

    # Crear comprobante
    ComprobanteEntrega.objects.create(
        solicitud=solicitud,
        total=total,
        entregadopor="Administrador del sistema",
        recibidopor=solicitud.usuario.nombre
    )

    messages.success(request, "Solicitud procesada y comprobante generado.")
    return redirect("listar_solicitudes")


# -----------------------------
# LISTAR COMPROBANTES
# -----------------------------
def listar_comprobantes(request):
    comprobantes = ComprobanteEntrega.objects.select_related("solicitud").all()
    return render(request, "comprobantes/listar.html", {"comprobantes": comprobantes})


# -----------------------------
# VER COMPROBANTE
# -----------------------------
def ver_comprobante(request, comprobante_id):
    comprobante = get_object_or_404(ComprobanteEntrega, pk=comprobante_id)
    return render(request, "comprobantes/ver.html", {"comprobante": comprobante})

def historial_solicitud(request, pk):
    solicitud = get_object_or_404(Solicitud, pk=pk)
    historial = HistorialEstadoSolicitud.objects.filter(
        solicitud_id=pk
    ).select_related("estadosolicitud", "usuario")

    return render(request, "solicitudes/historial.html", {
        "solicitud": solicitud,
        "historial": historial
    })
