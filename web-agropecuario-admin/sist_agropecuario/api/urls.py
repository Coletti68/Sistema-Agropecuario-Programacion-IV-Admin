# api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Usuarios
    path('usuarios/', views.usuarios.listar_usuarios, name='listar_usuarios'),
    path('usuarios/nuevo/', views.usuarios.crear_usuario, name='crear_usuario'),
    path('usuarios/<int:pk>/editar/', views.usuarios.editar_usuario, name='editar_usuario'),
    path('usuarios/<int:pk>/desactivar/', views.usuarios.desactivar_usuario, name='desactivar_usuario'),

    # Cultivos
    path('cultivos/', views.cultivos.listar_cultivos, name='listar_cultivos'),
    path('cultivos/nuevo/', views.cultivos.crear_cultivo, name='crear_cultivo'),
    path('cultivos/<int:pk>/editar/', views.cultivos.editar_cultivo, name='editar_cultivo'),

    # Proveedores
    path('proveedores/', views.proveedores.listar_proveedores, name='listar_proveedores'),
    path('proveedores/nuevo/', views.proveedores.crear_proveedor, name='crear_proveedor'),

    # Insumos
    path('insumos/', views.insumos.listar_insumos, name='listar_insumos'),
    path('insumos/nuevo/', views.insumos.crear_insumo, name='crear_insumo'),
    path('insumos/<int:pk>/editar/', views.insumos.editar_insumo, name='editar_insumo'),
    path('insumos/<int:pk>/desactivar/', views.insumos.desactivar_insumo, name='desactivar_insumo'),

    # Solicitudes
    path('solicitudes/', views.solicitudes.listar_solicitudes, name='listar_solicitudes'),
    path('solicitudes/<int:pk>/detalle/', views.solicitudes.ver_detalle, name='ver_detalle'),
    path('solicitudes/<int:pk>/estado/', views.solicitudes.cambiar_estado, name='cambiar_estado'),

    # Pagos
    path('pagos/', views.pagos.listar_pagos, name='listar_pagos'),
    path('pagos/nuevo/', views.pagos.registrar_pago, name='registrar_pago'),

    # Comprobantes
    path('comprobantes/', views.comprobantes.listar_comprobantes, name='listar_comprobantes'),
    path('comprobantes/<int:pk>/generar/', views.comprobantes.generar_comprobante, name='generar_comprobante'),

    # Informes
    path('informes/stock/', views.informes.informe_stock_critico, name='informe_stock_critico'),
    path('informes/insumos-periodo/', views.informes.informe_insumos_por_periodo, name='informe_insumos_por_periodo'),
    path('informes/costos-productor/', views.informes.informe_costos_por_productor, name='informe_costos_por_productor'),
]
