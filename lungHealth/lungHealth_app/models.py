from django.db import models


class Medico(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    hospital = models.CharField(max_length=100)
    
class Meta:
    db_table = 'medicos'
    
class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    hospital = models.CharField(max_length=100, default='DEFAULT VALUE')
    numero_seguro_social = models.CharField(max_length=20, unique=True)
    diagnostico = models.CharField(max_length=255, default='DEFAULT VALUE')
    

class Meta:
    db_table = 'pacientes'


class Tratamiento(models.Model):
    fecha_inicio = models.DateField()
    medicamentos_recetados = models.TextField()
    dosificacion = models.CharField(max_length=100)
    duracion_tratamiento = models.CharField(max_length=100)
    paciente = models.CharField(max_length=100)

class Meta:
    db_table = 'tratamientos'
