from django.db import models

class Libro(models.Model):
    nombre = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    editorial = models.CharField(max_length=100)
    paginas = models.IntegerField()
    fecha = models.DateField()

    def _str_(self):
        return self.nombre