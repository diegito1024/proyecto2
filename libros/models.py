from django.db import models


# Create your models here.


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    editorial = models.CharField(max_length=100)
    anio = models.IntegerField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
