from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Carrera(models.Model):

    nombre = models.CharField(max_length=50)
    modalidad = models.CharField(max_length=20)
    duracion = models.TextField(max_length=20)
    financiacion = models.TextField()

    def __str__(self):
        return f"{self.nombre} "
    

class Postgrado(models.Model):

    nombre = models.CharField(max_length=50)
    modalidad = models.CharField(max_length=20)
    duracion = models.TextField(max_length=20)
    financiacion = models.TextField()

    def __str__(self):
        return f"{self.nombre} "

 
class Docente(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.apellido}, {self.nombre} "


class Alumno(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.apellido}, {self.nombre} "
    

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return f"{self.user} [{self.imagen}]"    