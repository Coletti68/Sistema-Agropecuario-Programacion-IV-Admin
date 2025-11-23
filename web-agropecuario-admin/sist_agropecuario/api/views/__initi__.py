# api/views/__init__.py
from .usuario import (
    listar_usuarios,
    crear_usuario,
    editar_usuario,
    desactivar_usuario,
    activar_usuario
)

from .comprobante import (
    listar_comprobantes,
    generar_comprobante,
    ver_comprobante
)
 
from .cultivo import (
    listar_cultivos,
    crear_cultivo,
    editar_cultivo,
    desactivar_cultivo,
    activar_cultivo,
    ver_cultivos_asignados
)

from .estado_solicitud import (
    ver_historial_estados,
    cambiar_estado
)

from .historial_cultivo import (
    listar_historial,
    historial_por_usuario,
    historial_por_asignacion,
    historial_detalles
)

from .insumo import (
    listar_insumos,
    crear_insumo,
    editar_insumo,
    desactivar_insumo,
    insumos_stock_critico
)

from .pago import (
    listar_pagos,
    registrar_pago,
    actualizar_estado_pago,
    listar_pagos_por_usuario
)

from .proveedor import (
    listar_proveedores,
    crear_proveedor,
    editar_proveedor,
    desactivar_proveedor,
    activar_proveedor,
    listar_insumos_por_proveedor
)

from .solicitud import (
    listar_solicitudes,
    listar_solicitudes_con_detalles,
    obtener_solicitud_por_id,
    cambiar_estado_solicitud,
    filtrar_solicitudes_por_estado,
    solicitudes_por_usuario,
    historial_solicitud
)

from .solicitud_detalle import (
    ver_detalles_solicitud,
    agregar_item_solicitud,
    editar_item_solicitud,
    eliminar_item_solicitud
)

from .usuario_cultivo import (
    listar_usuariocultivos,
    cultivos_por_usuario,
    usuarios_por_cultivo   
)

from .historial_estado_solicitud import (
    listar_historial_estados,
    historial_por_solicitud,
    historial_por_usuario,
    historial_por_estado
)

