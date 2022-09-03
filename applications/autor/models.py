from ctypes.wintypes import CHAR
from tabnanny import verbose
from django.db import models

# Create your models here.
from .managers import AutorManager

class Autor(models.Model):
    #Modelo Autores
    nombre = models.CharField(
        max_length=50
    )
    apellido = models.CharField(
        max_length=50
    )
    nacionalidad = models.CharField(
        max_length=50
    )
    edad = models.PositiveIntegerField(
        
    )        

    objects =  AutorManager()
    class Meta:
        verbose_name =  'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['id']
    def __str__(self):

        return str(self.id) + ') ' + self.nombre + ' ' + self.apellido