from django.db import models
import datetime

class Fuente(models.Model):
    nombre = models.CharField(max_length=60)
    url = models.URLField()
    
    def __str__(self):
        return self.nombre

class Titular(models.Model):
    titulo = models.CharField(max_length=200)
    fuente = models.ForeignKey(Fuente, on_delete=models.CASCADE)
    url = models.URLField()
    fecha = models.DateField
        
    def __str__(self):
        return self.titulo