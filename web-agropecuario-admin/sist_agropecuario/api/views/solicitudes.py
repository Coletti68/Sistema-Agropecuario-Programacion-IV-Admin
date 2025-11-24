from django.shortcuts import render, redirect, get_object_or_404
from ..models import Solicitud, SolicitudDetalle, EstadoSolicitud, HistorialEstadoSolicitud

# LISTAR SOLICITUDES
def listar_solicitudes(request):
    solicitudes = Solicitud.objects.select_related("usuario", "estadosolicitudid")
    estados = EstadoSolicitud.objects.all()

    return render(request, "solicitudes/listar.html", {
        "solicitudes": solicitudes,
        "estados": estados,
        "nombre": "Administrador"
    })


# DETALLE DE UNA SOLICITUD
def detalle_solicitud(request, pk):
    solicitud = get_object_or_404(Solicitud, pk=pk)
    detalles = SolicitudDetalle.objects.filter(solicitud=solicitud)

    return render(request, "solicitudes/detalle.html", {
        "solicitud": solicitud,
        "detalles": detalles
    })


# HISTORIAL DE CAMBIOS DE ESTADO
def historial_solicitud(request, pk):
    solicitud = get_object_or_404(Solicitud, pk=pk)
    historial = HistorialEstadoSolicitud.objects.filter(solicitud_id=pk).select_related(
        "estadosolicitud", "usuario"
    )

    return render(request, "solicitudes/historial.html", {
        "solicitud": solicitud,
        "historial": historial
    })


# CAMBIAR ESTADO (POST tradicional)
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
# LISTAR SOLICITUDES con filtro por estado
def listar_solicitudes(request):
    estado_id = request.GET.get('estadoid')  # obtener el parámetro GET ?estadoid=
    
    # Traer todas las solicitudes y usar select_related para optimizar queries
    solicitudes = Solicitud.objects.select_related("usuario", "estadosolicitudid").all()
    
    # Aplicar filtro por estado si se recibió
    if estado_id:
        solicitudes = solicitudes.filter(estadosolicitudid_id=estado_id)
    
    # Traer todos los estados para el dropdown de filtrado
    estados = EstadoSolicitud.objects.all()

    return render(request, "solicitudes/listar.html", {
        "solicitudes": solicitudes,
        "estados": estados,
        "estado_seleccionado": int(estado_id) if estado_id else None,
        "nombre": "Administrador"
    })