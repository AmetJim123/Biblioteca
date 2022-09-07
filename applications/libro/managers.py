import datetime

from django.db import models
from django.db.models import Q


class LibroManager(models.Manager):
    #Managers para el modelo autor
    
    def listar_libros(self, kword):

        resultado = self.filter(
            titulo__icontains=kword,
            fecha__range=('2000-01-01', '2002-01-01')
            )
        return resultado

    def listar_libros2(self, kword, fecha2, fecha3):
        date1 = datetime.datetime.strptime(fecha2, "%Y-%m-%d").date()
        date2 = datetime.datetime.strptime(fecha3, "%Y-%m-%d").date()


        resultado = self.filter(
            titulo__icontains=kword,
            fecha__range=(date1, date2)
            )
        return resultado
