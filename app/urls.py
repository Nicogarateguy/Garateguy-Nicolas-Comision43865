from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name="inicio"),

    path('carreras/', carreras, name="carreras"),
    path('postgrados/', postgrados, name="postgrados"),
    path('docentes/', docentes, name="docentes"),
    path('alumnos/', alumnos, name="alumnos"),
    path('becas/', becas, name ="becas"),
    path('alumni_blue/', alumniblue, name ="alumni_blue"),
    
    path('carrera_form/', carreraForm, name="carrera_form"),
    path('postgrado_form/', postgradoForm, name="postgrado_form"),
    path('carrera_form2/', carreraForm2, name="carrera_form2"),
    path('docente_form/', docenteForm, name="docente_form"),

    path('buscar_duracion/', buscarDuracion, name="buscar_duracion"),
    path('buscar2/', buscar2, name="buscar2"),


]
