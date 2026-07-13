from django import forms

from .models import Curso


class CursoForm(forms.ModelForm):

    class Meta:
        model = Curso

        fields = [
            "nombre",
            "numero_creditos",
            "nivel",
            "horas_clase_semana",
            "jornada",
            "imagen",
            "docente",
        ]

        labels = {
            "nombre": "Nombre del curso",
            "numero_creditos": "Número de créditos",
            "nivel": "Nivel",
            "horas_clase_semana": "Horas por semana",
            "jornada": "Jornada",
            "imagen": "Imagen del curso",
            "docente": "Docente",
        }

        widgets = {
            "nombre": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese el nombre del curso",
                }
            ),
            "numero_creditos": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": 1,
                }
            ),
            "nivel": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese el nivel",
                }
            ),
            "horas_clase_semana": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": 1,
                }
            ),
            "jornada": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
            "imagen": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "docente": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
        }