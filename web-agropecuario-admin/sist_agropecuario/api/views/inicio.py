from django.shortcuts import render, redirect
from django.db.models import F
from api.models import Usuario, Cultivo, Solicitud, Proveedor, Insumo

def inicio(request):
    usuarioid = request.session.get('usuarioid')
    nombre = request.session.get('nombre')

    if not usuarioid:
        return redirect('login_custom')

    # Obtener estadísticas para el dashboard
    total_usuarios = Usuario.objects.filter(activo=True).count()
    total_cultivos = Cultivo.objects.filter(activo=True).count()
    total_solicitudes = Solicitud.objects.filter(activo=True).count()
    total_proveedores = Proveedor.objects.filter(activo=True).count()
    total_insumos = Insumo.objects.filter(activo=True).count()
    
    # Solicitudes pendientes (estado 1 = pendiente, ajustar según tu DB)
    solicitudes_pendientes = Solicitud.objects.filter(activo=True, estadosolicitudid=1).count()
    
    # Insumos con stock bajo
    insumos_stock_bajo = Insumo.objects.filter(activo=True, stock__lte=F('stock_minimo')).count()

    context = {
        'nombre': nombre,
        'total_usuarios': total_usuarios,
        'total_cultivos': total_cultivos,
        'total_solicitudes': total_solicitudes,
        'total_proveedores': total_proveedores,
        'total_insumos': total_insumos,
        'solicitudes_pendientes': solicitudes_pendientes,
        'insumos_stock_bajo': insumos_stock_bajo,
    }

    return render(request, 'inicio.html', context)

