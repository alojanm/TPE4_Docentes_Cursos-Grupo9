from django.urls import path

from .views import *


urlpatterns = [

    path(

        "verDocentes/",

        ListaDocentes.as_view(),

        name="lista_docentes"

    ),

    path(

        "nuevoDocente/",

        NuevoDocente.as_view(),

        name="nuevo_docente"

    ),

    path(

        "editarDocente/<int:pk>/",

        EditarDocente.as_view(),

        name="editar_docente"

    ),

    path(

        "eliminarDocente/<int:pk>/",

        EliminarDocente.as_view(),

        name="eliminar_docente"

    ),


]