# UIII-Act-7-Consultorio-Dental-No.Lista-33-5I

# Sistema de Gestión de Consultorio Dental - Grupo 33

## 📊 Diseño de Base de Datos - DBDesigner

![Diseño de Base de Datos Dental](https://dbdesigner.page.link/dtE1JBsTTgBvjqQ17)

## 🐍 Modelo Django - models.py

```python
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
```

## 🗄️ Script MySQL

```sql
-- Creación de la base de datos
CREATE DATABASE IF NOT EXISTS consultorio_dental;
USE consultorio_dental;

-- Tabla Paciente_Dental
CREATE TABLE Paciente_Dental (
    id_paciente INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    genero CHAR(1) NOT NULL,
    direccion VARCHAR(255) NOT NULL,
    telefono VARCHAR(20) NOT NULL,
    email VARCHAR(100),
    num_seguro_dental VARCHAR(50),
    fecha_registro DATE NOT NULL,
    historial_medico_previo TEXT
);

-- Tabla Odontologo
CREATE TABLE Odontologo (
    id_odontologo INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    especialidad VARCHAR(100) NOT NULL,
    telefono VARCHAR(20) NOT NULL,
    email VARCHAR(100),
    licencia_dental VARCHAR(50) NOT NULL,
    fecha_contratacion DATE NOT NULL,
    salario DECIMAL(10,2) NOT NULL,
    turno VARCHAR(50) NOT NULL
);

-- Tabla Cita_Dental
CREATE TABLE Cita_Dental (
    id_cita INT PRIMARY KEY AUTO_INCREMENT,
    id_paciente INT NOT NULL,
    id_odontologo INT NOT NULL,
    fecha_cita DATE NOT NULL,
    hora_cita TIME NOT NULL,
    motivo_cita TEXT NOT NULL,
    estado_cita VARCHAR(50) NOT NULL,
    comentarios TEXT,
    tipo_tratamiento VARCHAR(100),
    FOREIGN KEY (id_paciente) REFERENCES Paciente_Dental(id_paciente),
    FOREIGN KEY (id_odontologo) REFERENCES Odontologo(id_odontologo)
);

-- Tabla Tratamiento_Dental
CREATE TABLE Tratamiento_Dental (
    id_tratamiento INT PRIMARY KEY AUTO_INCREMENT,
    nombre_tratamiento VARCHAR(100) NOT NULL,
    descripcion TEXT NOT NULL,
    costo_promedio DECIMAL(10,2) NOT NULL,
    duracion_estimada_minutos INT NOT NULL,
    es_invasivo BOOLEAN NOT NULL,
    requiere_anestesia BOOLEAN NOT NULL,
    materiales_comunes TEXT
);

-- Tabla Historial_Tratamiento
CREATE TABLE Historial_Tratamiento (
    id_historial INT PRIMARY KEY AUTO_INCREMENT,
    id_cita INT NOT NULL,
    id_paciente INT NOT NULL,
    id_odontologo INT NOT NULL,
    id_tratamiento INT NOT NULL,
    fecha_realizacion DATETIME NOT NULL,
    notas_tratamiento TEXT,
    costo_final DECIMAL(10,2) NOT NULL,
    piezas_dentales_afectadas TEXT,
    FOREIGN KEY (id_cita) REFERENCES Cita_Dental(id_cita),
    FOREIGN KEY (id_paciente) REFERENCES Paciente_Dental(id_paciente),
    FOREIGN KEY (id_odontologo) REFERENCES Odontologo(id_odontologo),
    FOREIGN KEY (id_tratamiento) REFERENCES Tratamiento_Dental(id_tratamiento)
);

-- Tabla Factura_Dental
CREATE TABLE Factura_Dental (
    id_factura INT PRIMARY KEY AUTO_INCREMENT,
    id_paciente INT NOT NULL,
    fecha_emision DATE NOT NULL,
    total_factura DECIMAL(10,2) NOT NULL,
    estado_pago VARCHAR(50) NOT NULL,
    metodo_pago VARCHAR(50) NOT NULL,
    fecha_vencimiento DATE NOT NULL,
    id_cita_asociada INT NOT NULL,
    descuento_aplicado DECIMAL(5,2),
    FOREIGN KEY (id_paciente) REFERENCES Paciente_Dental(id_paciente),
    FOREIGN KEY (id_cita_asociada) REFERENCES Cita_Dental(id_cita)
);

-- Tabla Material_Odontologico
CREATE TABLE Material_Odontologico (
    id_material INT PRIMARY KEY AUTO_INCREMENT,
    nombre_material VARCHAR(255) NOT NULL,
    descripcion TEXT,
    stock_actual INT NOT NULL,
    fecha_caducidad DATE,
    id_proveedor INT NOT NULL,
    costo_unitario DECIMAL(10,2) NOT NULL,
    tipo_material VARCHAR(50) NOT NULL,
    ubicacion_almacen VARCHAR(100) NOT NULL
);
```

<img width="1026" height="349" alt="image" src="https://github.com/user-attachments/assets/21327a0f-da6a-4c55-9958-c36c09245841" />
<img width="970" height="508" alt="image" src="https://github.com/user-attachments/assets/9b529e2c-675c-48d8-9cfa-b964d6e1ba9d" />
<img width="961" height="462" alt="image" src="https://github.com/user-attachments/assets/cf7c4d71-a6b2-4842-b228-70bcee4cd690" />
<img width="608" height="383" alt="image" src="https://github.com/user-attachments/assets/1b407806-3460-4b4e-890f-5ea585b4a075" />
<img width="460" height="750" alt="image" src="https://github.com/user-attachments/assets/b252746d-ccdc-4aca-b709-7e4347d0c5d4" />
