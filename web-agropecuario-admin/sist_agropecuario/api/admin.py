from django.contrib import admin
from .models import (
    Rol, Usuario, Cultivo, UsuarioCultivo, HistorialCultivo,
    Proveedor, Insumo, Solicitud, SolicitudDetalle, Pago,
    EstadoSolicitud, HistorialEstadoSolicitud, ComprobanteEntrega
)

class RecargarAdmin(admin.ModelAdmin):
    class Media:
        js = ('admin/js/admin_notificaciones.js',)

admin.site.register(Rol, RecargarAdmin)
admin.site.register(Usuario, RecargarAdmin)
admin.site.register(Cultivo, RecargarAdmin)
admin.site.register(UsuarioCultivo, RecargarAdmin)
admin.site.register(HistorialCultivo, RecargarAdmin)
admin.site.register(Proveedor, RecargarAdmin)
admin.site.register(Insumo, RecargarAdmin)
admin.site.register(Solicitud, RecargarAdmin)
admin.site.register(SolicitudDetalle, RecargarAdmin)
admin.site.register(Pago, RecargarAdmin)
admin.site.register(EstadoSolicitud, RecargarAdmin)
admin.site.register(HistorialEstadoSolicitud, RecargarAdmin)
admin.site.register(ComprobanteEntrega, RecargarAdmin)
