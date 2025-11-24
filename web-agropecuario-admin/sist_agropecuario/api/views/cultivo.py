from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from ..models import Cultivo, UsuarioCultivo, Usuario

# GET /cultivos
def listar_cultivos(request):
    cultivos = Cultivo.objects.filter(activo=True)
    return render(request, 'cultivos/listar.html', {'cultivos': cultivos})

# POST /cultivos
def crear_cultivo(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        if not nombre:
            return JsonResponse({'error': 'Nombre obligatorio'}, status=400)
        Cultivo.objects.create(nombre=nombre, descripcion=descripcion, activo=True)
        return JsonResponse({'mensaje': 'Cultivo creado correctamente'})
    return render(request, 'cultivos/crear.html')

# PUT /cultivos/:id
def editar_cultivo(request, pk):
    cultivo = get_object_or_404(Cultivo, pk=pk)
    if request.method == 'POST':
        cultivo.nombre = request.POST.get('nombre') or cultivo.nombre
        cultivo.descripcion = request.POST.get('descripcion') or cultivo.descripcion
        cultivo.save()
        return JsonResponse({'mensaje': 'Cultivo actualizado'})
    return render(request, 'cultivos/editar.html', {'cultivo': cultivo})

# DELETE /cultivos/:id
def desactivar_cultivo(request, pk):
    cultivo = get_object_or_404(Cultivo, pk=pk)
    cultivo.activo = False
    cultivo.save()
    return JsonResponse({'mensaje': 'Cultivo desactivado'})

# PUT /cultivos/:id/activar
def activar_cultivo(request, pk):
    cultivo = get_object_or_404(Cultivo, pk=pk)
    cultivo.activo = True
    cultivo.save()
    return JsonResponse({'mensaje': 'Cultivo activado'})

# GET /cultivos/asignados
from django.http import JsonResponse
from ..models import UsuarioCultivo

def ver_cultivos_asignados(request):
    # Traemos todas las asignaciones sin filtrar por activo
    asignaciones = UsuarioCultivo.objects.select_related('usuarioid', 'cultivoid').all()

    # Creamos la lista de datos
    data = [{
        'id': a.usuariocultivoid,
        'usuario': a.usuarioid.nombre,
        'cultivo': a.cultivoid.nombre,
        'latitud': a.latitud,
        'longitud': a.longitud,
        'fechasiembra': a.fechasiembra
    } for a in asignaciones]

    return JsonResponse(data, safe=False)
