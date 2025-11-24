from django.shortcuts import render, redirect
from django.db import connection
from django.contrib import messages

def login_custom(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT usuarioid, nombre, rolid
                FROM usuario
                WHERE email = %s AND passwordhash = SHA2(%s, 256) AND activo = TRUE
            """, [email, password])
            user = cursor.fetchone()

        if user:
            request.session['usuarioid'] = user[0]
            request.session['nombre'] = user[1]
            request.session['rolid'] = user[2]
            return redirect('/')  # 🔥 redirige al panel
        else:
            messages.error(request, 'Credenciales inválidas.')

    return render(request, 'registro/login.html')

def logout_custom(request):
    request.session.flush()
    return redirect('login_custom')
