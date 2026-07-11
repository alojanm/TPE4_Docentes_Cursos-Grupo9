from django.contrib import admin
from .models import Curso

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nivel', 'jornada', 'docente')
    search_fields = ('nombre',)
    list_filter = ('jornada', 'nivel')