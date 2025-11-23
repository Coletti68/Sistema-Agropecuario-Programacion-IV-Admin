from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from ..models import UsuarioCultivo, Usuario, Cultivo

# GET /usuariocultivos
def listar_usuariocultivos(request):
    asignaciones = UsuarioCultivo.objects.select_related('usuarioid', 'cultivoid').all()
    data = [{
        'id': a.usuariocultivoid,
        'usuario': a.usuarioid.nombre,
        'cultivo': a.cultivoid.nombre,
        'latitud': a.latitud,
        'longitud': a.longitud,
        'fechasiembra': a.fechasiembra
    } for a in asignaciones]
    return JsonResponse(data, safe=False)


# GET /usuariocultivos/usuario/:usuarioId
def cultivos_por_usuario(request, usuarioId):
    usuario = get_object_or_404(Usuario, pk=usuarioId)
    asignaciones = UsuarioCultivo.objects.filter(usuarioid=usuario)
    data = [{
        'id': a.usuariocultivoid,
        'cultivo': a.cultivoid.nombre,
        'latitud': a.latitud,
        'longitud': a.longitud,
        'fechasiembra': a.fechasiembra
    } for a in asignaciones]
    return JsonResponse(data, safe=False)


# GET /usuariocultivos/cultivo/:cultivoId
def usuarios_por_cultivo(request, cultivoId):
    cultivo = get_object_or_404(Cultivo, pk=cultivoId)
    asignaciones = UsuarioCultivo.objects.filter(cultivoid=cultivo)
    data = [{
        'id': a.usuariocultivoid,
        'usuario': a.usuarioid.nombre,
        'latitud': a.latitud,
        'longitud': a.longitud,
        'fechasiembra': a.fechasiembra
    } for a in asignaciones]
    return JsonResponse(data, safe=False)
