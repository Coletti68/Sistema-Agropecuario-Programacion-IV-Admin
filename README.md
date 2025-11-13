##Web-Sistema Agropecuario (Administración)
Proyecto web para gestión administrativa del sistema agropecuario. Desarrollado con Django y conectado a la misma base de datos que la web de productores.

##BACKEND (Django) 

##Estructura general

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
