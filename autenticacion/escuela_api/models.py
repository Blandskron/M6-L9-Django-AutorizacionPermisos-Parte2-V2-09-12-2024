from django.db import models

# Create your models here.
class Escuela(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    direccion = models.CharField(max_length=100)
    fecha_fundacion = models.DateField()

    def __str__(self):
        return f"{self.nombre}, {self.direccion}, {self.fecha_fundacion}"
    