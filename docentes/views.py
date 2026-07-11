from django.shortcuts import render
from django.views.generic import ListView
from .models import Docente


class ListaDocentes(ListView):

    model = Docente
    template_name = "docentes/listaDocentes.html"
    context_object_name = "docentes"
# Create your views here.
