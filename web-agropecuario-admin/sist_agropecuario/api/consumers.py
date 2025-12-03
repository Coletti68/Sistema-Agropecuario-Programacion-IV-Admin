import json
from channels.generic.websocket import AsyncWebsocketConsumer

class NotificacionesConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Unirse al grupo "notificaciones"
        await self.channel_layer.group_add("notificaciones", self.channel_name)
        await self.accept()
        await self.send(text_data=json.dumps({
            "evento": "conexion",
            "mensaje": "WebSocket conectado correctamente"
        }))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("notificaciones", self.channel_name)

    async def enviar_notificacion(self, event):
        # Recibe lo que manda signals.py
        await self.send(text_data=json.dumps(event["data"]))
