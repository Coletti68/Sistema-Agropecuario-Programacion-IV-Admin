from django.shortcuts import redirect
from django.urls import reverse

class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Lista de rutas exentas de autenticación
        exempt_urls = [
            reverse('login_custom'),
            '/admin/',  # Si usas el admin de Django
        ]
        
        # Permitir acceso a archivos estáticos y media
        if request.path.startswith('/static/') or request.path.startswith('/media/'):
            return self.get_response(request)

        # Si la URL actual está en las exentas, continuar
        if request.path in exempt_urls or request.path.startswith('/admin/'):
            return self.get_response(request)

        # Verificar si el usuario tiene sesión iniciada (nuestro sistema custom)
        if not request.session.get('usuarioid'):
            return redirect('login_custom')

        response = self.get_response(request)
        return response
