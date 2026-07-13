from django.contrib import admin
<<<<<<< HEAD

# Register your models here.
=======
from .models import Curso

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nivel', 'jornada', 'docente')
    search_fields = ('nombre',)
    list_filter = ('jornada', 'nivel')
>>>>>>> f62071db688d5a2c636524db9797e5e29c2d9b4a
