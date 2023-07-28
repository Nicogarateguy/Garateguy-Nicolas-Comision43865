from django.db import models

# Create your models here.
class Carrera(models.Model):

    nombre = models.CharField(max_length=50)
    modalidad = models.CharField(max_length=20)
    duracion = models.TextField(max_length=20)
    financiacion = models.TextField()
    

class Postgrado(models.Model):

    nombre = models.CharField(max_length=50)
    modalidad = models.CharField(max_length=20)
    duracion = models.TextField(max_length=20)
    financiacion = models.TextField()

 
class Docente(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)


class Alumno(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()