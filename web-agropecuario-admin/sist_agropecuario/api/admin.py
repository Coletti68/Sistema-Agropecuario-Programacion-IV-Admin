from django.contrib import admin

# Register your models here.

from .models import (
    Rol, Usuario, Cultivo, UsuarioCultivo, HistorialCultivo,
    Proveedor, Insumo, Solicitud, SolicitudDetalle, Pago,
    EstadoSolicitud, HistorialEstadoSolicitud, ComprobanteEntrega
)

admin.site.register([
    Rol, Usuario, Cultivo, UsuarioCultivo, HistorialCultivo,
    Proveedor, Insumo, Solicitud, SolicitudDetalle, Pago,
    EstadoSolicitud, HistorialEstadoSolicitud, ComprobanteEntrega
])
