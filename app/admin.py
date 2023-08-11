from django.contrib import admin
from .models import Carrera, Postgrado, Docente, Alumno, Avatar

# Register your models here.
admin.site.register(Carrera)
admin.site.register(Postgrado)
admin.site.register(Docente)
admin.site.register(Alumno)
admin.site.register(Avatar)