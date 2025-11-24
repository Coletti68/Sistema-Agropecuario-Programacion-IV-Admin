from django.shortcuts import render, redirect

def inicio(request):
    usuarioid = request.session.get('usuarioid')
    nombre = request.session.get('nombre')

    if not usuarioid:
        return redirect('login_custom')

    return render(request, 'inicio.html', {'nombre': nombre})
