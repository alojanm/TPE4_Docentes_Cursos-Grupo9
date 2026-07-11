from django.db import models
from docentes.models import Docente


class Curso(models.Model):
    JORNADA_CHOICES = [
        ('matutina', 'Matutina'),
        ('vespertina', 'Vespertina'),
        ('nocturna', 'Nocturna'),
    ]

    nombre = models.CharField(max_length=100)
    numero_creditos = models.PositiveIntegerField()
    nivel = models.CharField(max_length=50)
    horas_clase_semana = models.PositiveIntegerField()
    jornada = models.CharField(max_length=20, choices=JORNADA_CHOICES)
    imagen = models.ImageField(upload_to='cursos/', blank=True, null=True)
    docente = models.ForeignKey(
        Docente,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='cursos'
    )

    def __str__(self):
        return self.nombre