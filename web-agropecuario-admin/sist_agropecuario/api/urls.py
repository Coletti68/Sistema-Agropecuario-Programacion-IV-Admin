from django.urls import path
from . import views
from .views import auth, inicio

# Importar correctamente las vistas de solicitudes
from .views.solicitudes import (
    listar_solicitudes,
    detalle_solicitud,
    procesar_solicitud,
    listar_comprobantes,
    ver_comprobante,
    historial_solicitud,
    cambiar_estado_solicitud
)


urlpatterns = [
    # Inicio y login
    path('', inicio.inicio, name='inicio'),
    path('login/', auth.login_custom, name='login_custom'),
    path('logout/', auth.logout_custom, name='logout_custom'),

    # Usuarios
    # Usuarios
path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
path('usuarios/nuevo/', views.crear_usuario, name='crear_usuario'),
path('usuarios/<int:pk>/editar/', views.editar_usuario, name='editar_usuario'),
path('usuarios/<int:pk>/desactivar/', views.desactivar_usuario, name='desactivar_usuario'),
path('usuarios/<int:pk>/activar/', views.activar_usuario, name='activar_usuario'),

path('cultivos/asignados/usuario/<int:usuarioId>/', 
     views.ver_cultivos_asignados, name='ver_cultivos_asignados'),


   path('usuariocultivos/panel/', views.panel_usuarios_cultivos, name='panel_usuarios_cultivos'),
    path('usuariocultivos/nuevo/', views.crear_usuariocultivo, name='crear_usuariocultivo'),
    path('usuariocultivos/<int:pk>/editar/', views.editar_usuariocultivo, name='editar_usuariocultivo'),
    path('usuariocultivos/usuario/<int:usuarioId>/', views.cultivos_por_usuario, name='cultivos_por_usuario'),
    path('usuariocultivos/cultivo/<int:cultivoId>/', views.usuarios_por_cultivo, name='usuarios_por_cultivo'),


    

    # Cultivos
    path('cultivos/', views.listar_cultivos, name='listar_cultivos'),
    path('cultivos/nuevo/', views.crear_cultivo, name='crear_cultivo'),
    path('cultivos/<int:pk>/editar/', views.editar_cultivo, name='editar_cultivo'),
    path('cultivos/<int:pk>/desactivar/', views.desactivar_cultivo, name='desactivar_cultivo'),
    path('cultivos/<int:pk>/activar/', views.activar_cultivo, name='activar_cultivo'),
    path('cultivos/usuario/<int:usuarioId>/', views.cultivos_por_usuario, name='cultivos_por_usuario'),


    # Proveedores
    path('proveedores/', views.listar_proveedores, name='listar_proveedores'),
    path('proveedores/nuevo/', views.crear_proveedor, name='crear_proveedor'),
    path('proveedores/<int:pk>/editar/', views.editar_proveedor, name='editar_proveedor'),
    path('proveedores/<int:pk>/desactivar/', views.desactivar_proveedor, name='desactivar_proveedor'),
    path('proveedores/<int:pk>/activar/', views.activar_proveedor, name='activar_proveedor'),
    path('proveedores/<int:pk>/insumos/', views.listar_insumos_por_proveedor, name='listar_insumos_por_proveedor'),


path('usuariocultivos/panel/', views.panel_usuarios_cultivos, name='panel_usuarios_cultivos'),
path('usuariocultivos/nuevo/', views.crear_usuariocultivo, name='crear_usuariocultivo'),
path('usuariocultivos/<int:pk>/editar/', views.editar_usuariocultivo, name='editar_usuariocultivo'),
path('usuariocultivos/<int:pk>/desactivar/', views.desactivar_usuariocultivo, name='desactivar_usuariocultivo'),
path('usuariocultivos/<int:pk>/activar/', views.activar_usuariocultivo, name='activar_usuariocultivo'),
    # Insumos
    path('insumos/', views.listar_insumos, name='listar_insumos'),
    path('insumos/nuevo/', views.crear_insumo, name='crear_insumo'),
    path('insumos/<int:pk>/editar/', views.editar_insumo, name='editar_insumo'),
    path('insumos/<int:pk>/desactivar/', views.desactivar_insumo, name='desactivar_insumo'),
    path('insumos/<int:pk>/activar/', views.activar_insumo, name='activar_insumo'),
    path('insumos/stock-critico/', views.insumos_stock_critico, name='insumos_stock_critico'),

    # Solicitudes
    path('solicitudes/', listar_solicitudes, name='listar_solicitudes'),
    path('solicitudes/<int:pk>/', detalle_solicitud, name='detalle_solicitud'),
    path('solicitudes/<int:pk>/procesar/', procesar_solicitud, name='procesar_solicitud'),

    path('comprobantes/', listar_comprobantes, name='listar_comprobantes'),
    path('comprobantes/<int:comprobante_id>/', ver_comprobante, name='ver_comprobante'),
    path('solicitudes/<int:pk>/historial/', historial_solicitud, name='historial_solicitud'),

    # Solicitudes
path('solicitudes/<int:pk>/cambiar-estado/', cambiar_estado_solicitud, name='cambiar_estado_solicitud'),

]
