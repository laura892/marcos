from django.db import models

# Create your models here.
class Clientes(models.Model):
 Nombre = models.CharField(max_length=100)
 Año = models.IntegerField()
 email = models.EmailField()
 Contraseña = models.CharField(max_length=100)