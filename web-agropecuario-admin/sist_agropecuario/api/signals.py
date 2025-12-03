from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .models import Usuario

def _send_event(evento, instance):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "notificaciones",
        {
            "type": "enviar_notificacion",
            "data": {
                "evento": evento,
                "modelo": "usuario",
                "usuarioid": instance.usuarioid,
                "nombre": instance.nombre,
                "email": instance.email,
            },
        },
    )

@receiver(post_save, sender=Usuario)
def usuario_post_save(sender, instance, created, **kwargs):
    if created:
        _send_event("usuario_creado", instance)
    else:
        _send_event("usuario_actualizado", instance)

@receiver(post_delete, sender=Usuario)
def usuario_post_delete(sender, instance, **kwargs):
    _send_event("usuario_eliminado", instance)
