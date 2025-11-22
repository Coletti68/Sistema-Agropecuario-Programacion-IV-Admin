from django.db import models

# Create your models here.
class Rol(models.Model):
    rolid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'rol'
    

class Usuario(models.Model):
    rol = models.ForeignKey(Rol, on_delete=models.PROTECT, db_column='rolid')
    usuarioid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    telefono = models.CharField(max_length=30, blank=True, null=True)
    dni = models.CharField(max_length=20, unique=True, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    passwordhash = models.CharField(max_length=255)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'usuario'
    

class Cultivo(models.Model):
    cultivoid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'cultivo'
    

class UsuarioCultivo(models.Model):
    usuariocultivoid = models.AutoField(primary_key=True)
    usuarioid = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='usuarioid')
    cultivoid = models.ForeignKey(Cultivo, on_delete=models.CASCADE, db_column='cultivoid')
    latitud = models.DecimalField(max_digits=9, decimal_places=6)
    longitud = models.DecimalField(max_digits=9, decimal_places=6)
    fechasiembra = models.DateField()

    class Meta:
        db_table = 'usuariocultivo'
    

class HistorialCultivo(models.Model):
    historialid = models.AutoField(primary_key=True)
    usuariocultivo = models.ForeignKey('UsuarioCultivo', on_delete=models.CASCADE, db_column='usuariocultivoid')
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, db_column='usuarioid')
    latitud = models.DecimalField(max_digits=10, decimal_places=8)
    longitud = models.DecimalField(max_digits=11, decimal_places=8)
    fecha = models.DateTimeField(auto_now_add=True)
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'historialcultivo'


class Proveedor(models.Model):
    proveedorid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'proveedor'


class Insumo(models.Model):
    insumoid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, db_column='proveedorid')
    estado = models.BooleanField(default=True)
    stock = models.IntegerField(default=0)
    stock_minimo = models.IntegerField(default=0)

    class Meta:
        db_table = 'insumo'


class Solicitud(models.Model):
    solicitudid = models.AutoField(primary_key=True)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, db_column='usuarioid')
    fechasolicitud = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'solicitud'


class SolicitudDetalle(models.Model):
    solicituddetalleid = models.AutoField(primary_key=True)
    solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE, db_column='solicitudid')
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE, db_column='insumoid')
    cantidad = models.IntegerField()
    preciounitario = models.DecimalField(max_digits=10, decimal_places=2)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'solicituddetalle'


class Pago(models.Model):
    pagoid = models.AutoField(primary_key=True)
    solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE, db_column='solicitudid')
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, db_column='usuarioid')
    fecha_pago = models.DateTimeField(auto_now_add=True)
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    metodo_pago = models.CharField(max_length=50, blank=True, null=True)
    estado_pago = models.CharField(max_length=20, default='pendiente')
    observaciones = models.TextField(blank=True, null=True)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'pago'


class EstadoSolicitud(models.Model):
    estadosolicitudid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        db_table = 'estadosolicitud'


class HistorialEstadoSolicitud(models.Model):
    historialid = models.AutoField(primary_key=True)
    solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE, db_column='solicitudid')
    estadosolicitud = models.ForeignKey(EstadoSolicitud, on_delete=models.CASCADE, db_column='estadosolicitudid')
    usuario = models.ForeignKey('Usuario', on_delete=models.SET_NULL, db_column='usuarioid', null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'historialestadosolicitud'


class ComprobanteEntrega(models.Model):
    comprobanteid = models.AutoField(primary_key=True)
    solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE, db_column='solicitudid')
    fechaentrega = models.DateTimeField(blank=True, null=True)
    total = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    entregadopor = models.IntegerField()
    recibidopor = models.IntegerField()
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'comprobanteentrega'