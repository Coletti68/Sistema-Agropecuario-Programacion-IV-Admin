# api/views/__init__.py
from .usuarios import (
    listar_usuarios,
    crear_usuario,
    editar_usuario,
    desactivar_usuario,
)

from .cultivos import (
    listar_cultivos,
    crear_cultivo,
    editar_cultivo,
    asignar_cultivo_usuario,
    ver_historial_cultivo,
)

from .proveedores import (
    listar_proveedores,
    crear_proveedor,
    editar_proveedor,
    desactivar_proveedor,
)

from .insumos import (
    listar_insumos,
    crear_insumo,
    editar_insumo,
    desactivar_insumo,
)

from .solicitudes import (
    listar_solicitudes,
    ver_detalle,
    cambiar_estado,
    ver_historial_estados,
)

from .pagos import (
    listar_pagos,
    registrar_pago,
    cambiar_estado_pago,
)

from .comprobantes import (
    listar_comprobantes,
    generar_comprobante,
)

from .informes import (
    informe_stock_critico,
    informe_insumos_por_periodo,
    informe_costos_por_productor,
)

