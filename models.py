from django.db import models

class Paciente_Dental(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=1)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, blank=True, null=True)
    num_seguro_dental = models.CharField(max_length=50, blank=True, null=True)
    fecha_registro = models.DateField()
    historial_medico_previo = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Odontologo(models.Model):
    id_odontologo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, blank=True, null=True)
    licencia_dental = models.CharField(max_length=50)
    fecha_contratacion = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    turno = models.CharField(max_length=50)

    def __str__(self):
        return f"Dr. {self.nombre} {self.apellido} - {self.especialidad}"

class Tratamiento_Dental(models.Model):
    id_tratamiento = models.AutoField(primary_key=True)
    nombre_tratamiento = models.CharField(max_length=100)
    descripcion = models.TextField()
    costo_promedio = models.DecimalField(max_digits=10, decimal_places=2)
    duracion_estimada_minutos = models.IntegerField()
    es_invasivo = models.BooleanField()
    requiere_anestesia = models.BooleanField()
    materiales_comunes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre_tratamiento

class Cita_Dental(models.Model):
    id_cita = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey('Paciente_Dental', on_delete=models.CASCADE)
    id_odontologo = models.ForeignKey('Odontologo', on_delete=models.CASCADE)
    fecha_cita = models.DateField()
    hora_cita = models.TimeField()
    motivo_cita = models.TextField()
    estado_cita = models.CharField(max_length=50)
    comentarios = models.TextField(blank=True, null=True)
    tipo_tratamiento = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Cita {self.id_cita} - {self.id_paciente} - {self.fecha_cita}"

class Historial_Tratamiento(models.Model):
    id_historial = models.AutoField(primary_key=True)
    id_cita = models.ForeignKey('Cita_Dental', on_delete=models.CASCADE)
    id_paciente = models.ForeignKey('Paciente_Dental', on_delete=models.CASCADE)
    id_odontologo = models.ForeignKey('Odontologo', on_delete=models.CASCADE)
    id_tratamiento = models.ForeignKey('Tratamiento_Dental', on_delete=models.CASCADE)
    fecha_realizacion = models.DateTimeField()
    notas_tratamiento = models.TextField(blank=True, null=True)
    costo_final = models.DecimalField(max_digits=10, decimal_places=2)
    piezas_dentales_afectadas = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Historial {self.id_historial} - {self.id_paciente}"

class Factura_Dental(models.Model):
    id_factura = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey('Paciente_Dental', on_delete=models.CASCADE)
    fecha_emision = models.DateField()
    total_factura = models.DecimalField(max_digits=10, decimal_places=2)
    estado_pago = models.CharField(max_length=50)
    metodo_pago = models.CharField(max_length=50)
    fecha_vencimiento = models.DateField()
    id_cita_asociada = models.ForeignKey('Cita_Dental', on_delete=models.CASCADE)
    descuento_aplicado = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"Factura {self.id_factura} - {self.id_paciente}"

class Material_Odontologico(models.Model):
    id_material = models.AutoField(primary_key=True)
    nombre_material = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    stock_actual = models.IntegerField()
    fecha_caducidad = models.DateField(blank=True, null=True)
    id_proveedor = models.IntegerField()
    costo_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_material = models.CharField(max_length=50)
    ubicacion_almacen = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_material
