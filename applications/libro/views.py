from django.shortcuts import render

from django.views.generic import ListView

# Create your views here.
from .models import Libro

class ListLibro(ListView):
    model = Libro
    context_object_name =  'lista_libros'
    template_name = 'libro/lista.html'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        #fecha1
        f2= self.request.GET.get("fecha2", '')
        #fecha2
        f3= self.request.GET.get("fecha3", '')

        if f2 and f3:
            return Libro.objects.listar_libros2(palabra_clave,f2,f3)
        else:
            return Libro.objects.listar_libros(palabra_clave)