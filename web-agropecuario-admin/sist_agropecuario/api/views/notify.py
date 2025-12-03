import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@csrf_exempt
def notify_new_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        payload = {
            "evento": "nuevo_usuario",
            "nombre": data.get("nombre", ""),
            "email": data.get("email", ""),
            "rol": data.get("rol", ""),
        }

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "notificaciones",
            {
                "type": "enviar_notificacion",
                "data": payload,
            }
        )
        return JsonResponse({"status": "ok"})
    return JsonResponse({"error": "Método no permitido"}, status=405)
