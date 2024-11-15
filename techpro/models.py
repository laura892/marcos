from django.db import models

# Create your models here.
class Techpro(models.Model):
 Cliente = models.CharField(max_length=100)
 Tecnico = models.CharField(max_length=100)
 Fecha_Solicitud = models.DateField()
 Fecha_Finalizacion = models.DateField()
 Estado = models.CharField(max_length=50)
 Descripcion= models.CharField(max_length=300)