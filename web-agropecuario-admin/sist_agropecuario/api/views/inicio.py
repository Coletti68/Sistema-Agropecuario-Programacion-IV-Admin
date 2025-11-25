from django.shortcuts import render, redirect
from api.models import Usuario, Cultivo, Solicitud, Proveedor, Insumo

def inicio(request):
    usuarioid = request.session.get('usuarioid')
    nombre = request.session.get('nombre')

    if not usuarioid:
        return redirect('login_custom')

    # Obtener contadores para el dashboard
    context = {
        'nombre': nombre,
        'total_usuarios': Usuario.objects.count(),
        'total_cultivos': Cultivo.objects.filter(activo=True).count(),
        'total_solicitudes': Solicitud.objects.filter(activo=True).count(),
        'total_proveedores': Proveedor.objects.filter(activo=True).count(),
        'total_insumos': Insumo.objects.filter(activo=True).count(),
    }

    return render(request, 'inicio.html', context)
