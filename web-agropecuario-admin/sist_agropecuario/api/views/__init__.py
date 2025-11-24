# -------------------------------
# API VIEWS — IMPORTS ORGANIZADOS
# -------------------------------

# 👉 AUTH / LOGIN / INICIO
from . import auth, inicio

# 👉 USUARIOS
from .usuario import (
    listar_usuarios,
    crear_usuario,
    editar_usuario,
    desactivar_usuario,
    activar_usuario
)

# 👉 CULTIVOS
from .cultivo import (
    listar_cultivos,
    crear_cultivo,
    editar_cultivo,
    desactivar_cultivo,
    activar_cultivo,
    ver_cultivos_asignados
)

# 👉 USUARIO – CULTIVO
from .usuario_cultivo import (
    panel_usuarios_cultivos,
    crear_usuariocultivo,
    editar_usuariocultivo,
    desactivar_usuariocultivo,
    activar_usuariocultivo,
    cultivos_por_usuario,     # <--- aquí
    usuarios_por_cultivo      # <--- y aquí
)

# 👉 PROVEEDORES
from .proveedor import (
    listar_proveedores,
    crear_proveedor,
    editar_proveedor,
    desactivar_proveedor,
    activar_proveedor,
    listar_insumos_por_proveedor
)

# 👉 INSUMOS
from .insumo import (
    listar_insumos,
    crear_insumo,
    editar_insumo,
    desactivar_insumo,
    activar_insumo,
    insumos_stock_critico
)


# 👉 SOLICITUDES (versión HTML, NO JSON)
from .solicitudes import (      # ← CORREGIDO
    listar_solicitudes,
    detalle_solicitud,
    historial_solicitud,
    cambiar_estado_solicitud
)

# 👉 DETALLES DE SOLICITUD
from .solicitud_detalle import (
    ver_detalles_solicitud,
    agregar_item_solicitud,
    editar_item_solicitud,
    eliminar_item_solicitud
)

# 👉 PAGOS
from .pago import (
    listar_pagos,
    registrar_pago,
    actualizar_estado_pago,
    listar_pagos_por_usuario
)

# 👉 HISTORIAL DE ESTADOS DE SOLICITUD
from .historial_estado_solicitud import (
    listar_historial_estados,
    historial_por_solicitud,
    historial_por_usuario,
    historial_por_estado
)

# 👉 HISTORIAL DE CULTIVO
from .historial_cultivo import (
    listar_historial,
    historial_por_usuario as historial_cultivo_por_usuario,
    historial_por_asignacion,
    historial_detalles
)
