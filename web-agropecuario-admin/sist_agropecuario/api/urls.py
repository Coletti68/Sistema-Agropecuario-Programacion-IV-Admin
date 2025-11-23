# api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Usuarios
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('usuarios/nuevo/', views.crear_usuario, name='crear_usuario'),
    path('usuarios/<int:pk>/editar/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/<int:pk>/desactivar/', views.desactivar_usuario, name='desactivar_usuario'),
    path('usuarios/<int:pk>/activar/', views.activar_usuario, name='activar_usuario'),

    # Cultivos
    path('cultivos/', views.listar_cultivos, name='listar_cultivos'),
    path('cultivos/nuevo/', views.crear_cultivo, name='crear_cultivo'),
    path('cultivos/<int:pk>/editar/', views.editar_cultivo, name='editar_cultivo'),
    path('cultivos/<int:pk>/desactivar/', views.desactivar_cultivo, name='desactivar_cultivo'),
    path('cultivos/<int:pk>/activar/', views.activar_cultivo, name='activar_cultivo'),
    path('cultivos/usuario/<int:usuarioId>/', views.cultivos_por_usuario, name='cultivos_por_usuario'),
    path('cultivos/asignados/', views.ver_cultivos_asignados, name='ver_cultivos_asignados'),

    # Proveedores
    path('proveedores/', views.listar_proveedores, name='listar_proveedores'),
    path('proveedores/nuevo/', views.crear_proveedor, name='crear_proveedor'),
    path('proveedores/<int:pk>/editar/', views.editar_proveedor, name='editar_proveedor'),
    path('proveedores/<int:pk>/desactivar/', views.desactivar_proveedor, name='desactivar_proveedor'),
    path('proveedores/<int:pk>/activar/', views.activar_proveedor, name='activar_proveedor'),
    path('proveedores/<int:pk>/insumos/', views.listar_insumos_por_proveedor, name='listar_insumos_por_proveedor'),

    # Insumos
    path('insumos/', views.listar_insumos, name='listar_insumos'),
    path('insumos/nuevo/', views.crear_insumo, name='crear_insumo'),
    path('insumos/<int:pk>/editar/', views.editar_insumo, name='editar_insumo'),
    path('insumos/<int:pk>/desactivar/', views.desactivar_insumo, name='desactivar_insumo'),
    path('insumos/stock-critico/', views.insumos_stock_critico, name='insumos_stock_critico'),

    # Solicitudes
    path('solicitudes/', views.listar_solicitudes, name='listar_solicitudes'),
    path('solicitudes/detalles/', views.listar_solicitudes_con_detalles, name='listar_solicitudes_con_detalles'),
    path('solicitudes/<int:pk>/', views.obtener_solicitud_por_id, name='obtener_solicitud_por_id'),
    path('solicitudes/<int:pk>/estado/', views.cambiar_estado_solicitud, name='cambiar_estado_solicitud'),
    path('solicitudes/estado/<int:estadoId>/', views.filtrar_solicitudes_por_estado, name='filtrar_solicitudes_por_estado'),
    path('solicitudes/usuario/<int:usuarioId>/', views.solicitudes_por_usuario, name='solicitudes_por_usuario'),
    path('solicitudes/<int:pk>/historial/', views.historial_solicitud, name='historial_solicitud'),

    # Solicitud Detalle
    path('solicitudes/<int:id>/detalle/', views.ver_detalles_solicitud, name='ver_detalles_solicitud'),
    path('solicitudes/<int:id>/detalle/nuevo/', views.agregar_item_solicitud, name='agregar_item_solicitud'),
    path('solicitudes/<int:id>/detalle/<int:detalleid>/editar/', views.editar_item_solicitud, name='editar_item_solicitud'),
    path('solicitudes/<int:id>/detalle/<int:detalleid>/eliminar/', views.eliminar_item_solicitud, name='eliminar_item_solicitud'),

    # Pagos
    path('pagos/', views.listar_pagos, name='listar_pagos'),
    path('pagos/nuevo/', views.registrar_pago, name='registrar_pago'),
    path('pagos/<int:pk>/estado/', views.actualizar_estado_pago, name='actualizar_estado_pago'),
    path('pagos/usuario/<int:usuarioId>/', views.listar_pagos_por_usuario, name='listar_pagos_por_usuario'),

    # Comprobantes
    path('comprobantes/', views.listar_comprobantes, name='listar_comprobantes'),
    path('comprobantes/nuevo/', views.generar_comprobante, name='generar_comprobante'),
    path('comprobantes/<int:pk>/', views.ver_comprobante, name='ver_comprobante'),

    # Historial Estado Solicitud
    path('historial-estados/', views.listar_historial_estados, name='listar_historial_estados'),
    path('historial-estados/solicitud/<int:solicitudId>/', views.historial_por_solicitud, name='historial_por_solicitud'),
    path('historial-estados/usuario/<int:usuarioId>/', views.historial_por_usuario, name='historial_por_usuario'),
    path('historial-estados/estado/<int:estadoId>/', views.historial_por_estado, name='historial_por_estado'),

    # Historial Cultivo
    path('historial-cultivo/', views.listar_historial, name='listar_historial'),
    path('historial-cultivo/usuario/<int:usuarioId>/', views.historial_por_usuario, name='historial_cultivo_por_usuario'),
    path('historial-cultivo/asignacion/<int:asignacionId>/', views.historial_por_asignacion, name='historial_por_asignacion'),
    path('historial-cultivo/<int:pk>/detalles/', views.historial_detalles, name='historial_detalles'),

    # Usuario Cultivo
    path('usuario-cultivos/', views.listar_usuariocultivos, name='listar_usuariocultivos'),
    path('usuario-cultivos/usuario/<int:usuarioId>/', views.cultivos_por_usuario, name='cultivos_por_usuario'),
    path('usuario-cultivos/cultivo/<int:cultivoId>/', views.usuarios_por_cultivo, name='usuarios_por_cultivo'),
]

