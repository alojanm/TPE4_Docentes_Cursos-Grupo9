from django.db import models

# Create your models here.
class Docente(models.Model):

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    cedula = models.CharField(max_length=10, unique=True)
    tipo_sangre = models.CharField(max_length=5)
    direccion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='docentes/', null=True, blank=True)

    def __str__(self):
<<<<<<< HEAD
        return f"{self.nombre} {self.apellido}"
=======
        return f"{self.nombre} {self.apellido}"
    
>>>>>>> f62071db688d5a2c636524db9797e5e29c2d9b4a
