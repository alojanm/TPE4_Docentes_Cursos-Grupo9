<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
=======
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CursoForm
from .models import Curso


def lista_cursos(request):
    """
    Muestra todos los cursos registrados junto con su docente.
    """
    cursos = Curso.objects.select_related("docente").all().order_by("nombre")

    return render(
        request,
        "cursos/lista_cursos.html",
        {
            "cursos": cursos,
        },
    )


def crear_curso(request):
    """
    Registra un nuevo curso.
    """
    if request.method == "POST":
        formulario = CursoForm(request.POST, request.FILES)

        if formulario.is_valid():
            formulario.save()

            messages.success(
                request,
                "El curso fue registrado correctamente.",
            )

            return redirect("cursos:lista_cursos")
    else:
        formulario = CursoForm()

    return render(
        request,
        "cursos/formulario_curso.html",
        {
            "formulario": formulario,
            "titulo": "Agregar curso",
            "texto_boton": "Guardar curso",
        },
    )


def editar_curso(request, curso_id):
    """
    Modifica la información de un curso existente.
    """
    curso = get_object_or_404(Curso, id=curso_id)

    if request.method == "POST":
        formulario = CursoForm(
            request.POST,
            request.FILES,
            instance=curso,
        )

        if formulario.is_valid():
            formulario.save()

            messages.success(
                request,
                "El curso fue actualizado correctamente.",
            )

            return redirect("cursos:lista_cursos")
    else:
        formulario = CursoForm(instance=curso)

    return render(
        request,
        "cursos/formulario_curso.html",
        {
            "formulario": formulario,
            "titulo": "Editar curso",
            "texto_boton": "Actualizar curso",
            "curso": curso,
        },
    )


def eliminar_curso(request, curso_id):
    """
    Elimina un curso luego de solicitar confirmación.
    """
    curso = get_object_or_404(Curso, id=curso_id)

    if request.method == "POST":
        curso.delete()

        messages.success(
            request,
            "El curso fue eliminado correctamente.",
        )

        return redirect("cursos:lista_cursos")

    return render(
        request,
        "cursos/eliminar_curso.html",
        {
            "curso": curso,
        },
    )
>>>>>>> f62071db688d5a2c636524db9797e5e29c2d9b4a
