from django.urls import reverse_lazy

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from .models import Docente
from .forms import DocenteForm


class ListaDocentes(ListView):

    model = Docente

    template_name = "docentes/listaDocentes.html"

    context_object_name = "docentes"


class NuevoDocente(CreateView):

    model = Docente

    form_class = DocenteForm

    template_name = "docentes/nuevoDocente.html"

    success_url = reverse_lazy("lista_docentes")


class EditarDocente(UpdateView):

    model = Docente

    form_class = DocenteForm

    template_name = "docentes/editarDocente.html"

    success_url = reverse_lazy ("lista_docentes")


class EliminarDocente(DeleteView):

    model = Docente

    template_name = "docentes/eliminarDocente.html"

    success_url =reverse_lazy("lista_docentes")
    
    
# Create your views here.
