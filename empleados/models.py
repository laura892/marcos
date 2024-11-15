from django.db import models

# Create your models here.
class Empleados(models.Model):
 Cedula = models.IntegerField()
 Nombre = models.CharField(max_length=100)
 Apellido = models.CharField(max_length=100)
 Fecha_Nacimiento = models.DateField()
 Edad = models.IntegerField()
 Cargo= models.CharField(max_length=100)
 email = models.EmailField()