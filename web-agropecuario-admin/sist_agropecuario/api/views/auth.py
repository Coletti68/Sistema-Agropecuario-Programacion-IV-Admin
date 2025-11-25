from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from ..models import Usuario

def login_custom(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = Usuario.objects.get(email=email, activo=True)
            if check_password(password, user.passwordhash):
                request.session['usuarioid'] = user.usuarioid
                request.session['nombre'] = user.nombre
                request.session['rolid'] = user.rol.rolid
                return redirect('/')
            else:
                messages.error(request, 'Credenciales inválidas.')
        except Usuario.DoesNotExist:
            messages.error(request, 'Credenciales inválidas.')

    return render(request, 'registro/login.html')

def logout_custom(request):
    request.session.flush()
    return redirect('login_custom')
