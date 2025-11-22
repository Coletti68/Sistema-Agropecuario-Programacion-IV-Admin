## Web-Sistema Agropecuario (Administración)
Proyecto web para gestión administrativa del sistema agropecuario. Desarrollado con Django y conectado a la misma base de datos que la web de productores.

## BACKEND (Django) 

## Estructura general

🔹 manage.py

Script principal para ejecutar comandos Django (runserver, migrate, createsuperuser, etc.).

🔹 .env

Variables sensibles: credenciales de base, claves secretas, etc.

Se usa con python-decouple o django-environ.

env
DB_NAME=sist_agropecuario  
DB_USER=root  
DB_PASS=tu_clave  
DB_HOST=localhost  
SECRET_KEY=clave_secreta  
DEBUG=True  

🔹 requirements.txt

Lista de dependencias del proyecto.

Se instala con:

bash
pip install -r requirements.txt
Carpetas y sus funcionalidades
📦 sistadmin/

Proyecto principal Django.

Contiene settings.py, urls.py, wsgi.py.

📦 apps/

Aplicaciones modulares por dominio:

usuarios, cultivos, solicitudes, pagos, insumos, etc.

📦 apps/usuarios/

Modelos, vistas, formularios y templates para gestión de usuarios.

Admin puede crear, editar, desactivar usuarios.

📦 apps/solicitudes/

Gestión de solicitudes, estados, pagos y comprobantes.

Visualización de historial y control de entregas.

📦 apps/insumos/

ABM de insumos y proveedores.

Control de stock y precios.

📦 templates/

HTML renderizado por Django.

Interfaz web para el administrador.

📦 static/

Archivos estáticos: CSS, JS, imágenes.

📦 migrations/

Migraciones automáticas de modelos a la base de datos.

## Funcionalidades previstas

Login de administrador

Panel de control con métricas

ABM de usuarios, cultivos, insumos, proveedores

Gestión de solicitudes y pagos

Visualización de historial y comprobantes

Filtros por estado, fecha, productor

Exportación de datos (PDF, Excel)

Envío de notificaciones (opcional)

## Dependencias recomendadas

django: Framework principal

mysqlclient o django-mysql: Conexión con MySQL

python-decouple o django-environ: Variables de entorno

django-crispy-forms: Formularios estilizados

django-rest-framework (opcional): API REST si se expone

django-filter: Filtros en vistas

django-extensions: Comandos útiles

django-import-export: Exportar datos

django-notifications (opcional): Notificaciones internas

## Comandos útiles

python manage.py runserver           # Iniciar servidor
python manage.py makemigrations     # Crear migraciones
python manage.py migrate            # Aplicar migraciones
python manage.py createsuperuser    # Crear usuario admin


## INSTALACIONES Y SUS ESPECIFICACIONES

1. pip install django mysqlclient python-decouple
Django: framework web, te da toda la estructura (apps, modelos, vistas, templates, admin).

mysqlclient: conector para que Django pueda hablar con MySQL.

python-decouple: permite leer variables desde .env (ej. credenciales de la base) sin hardcodearlas en settings.py.

2. django-admin startproject sist_agropecuario
Crea el proyecto base con carpetas y archivos (settings.py, urls.py, manage.py).


3. python manage.py startapp api
Crea una nueva app dentro del proyecto (api/).

Ahí definís tus modelos, vistas, templates y lógica específica.

Django funciona modular: cada app representa un módulo funcional (usuarios, insumos, etc.).

4. Registrar la app en INSTALLED_APPS
Le dice a Django que esa app existe y debe cargarse.

Sin esto, no se crean sus tablas ni se reconocen sus templates.

5. Configurar .env y settings.py
.env: guarda credenciales y configuración sensible (nombre de DB, usuario, contraseña).

settings.py: usa decouple para leer esas variables y configurar la conexión a MySQL.

6. python manage.py makemigrations
Escanea tus models.py y genera archivos de migración (planes de cambios).

Ejemplo: si definís un modelo Usuario, crea un archivo que describe cómo generar la tabla usuario.

7. python manage.py migrate
Aplica esas migraciones en la base de datos real.

Ejecuta el SQL necesario para crear/modificar tablas según tus modelos.

Resultado: tu esquema en MySQL queda sincronizado con el código Django.

8. python manage.py runserver
Levanta el servidor de desarrollo en http://127.0.0.1:8000/.

Te permite probar vistas, templates y APIs sin necesidad de un servidor externo.