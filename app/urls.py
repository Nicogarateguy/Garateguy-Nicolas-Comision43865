from django.urls import path, include
from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name="inicio"),

    path('carreras/', carreras, name="carreras"),
    path('postgrados/', postgrados, name="postgrados"),
    path('docentes/', docentes, name="docentes"),
    
    path('sobremi/', sobremi, name ="sobremi"),
    path('alumni_blue/', alumniblue, name ="alumni_blue"),
    
    path('carrera_form/', carreraForm, name="carrera_form"),
    path('postgrado_form/', postgradoForm, name="postgrado_form"),
    path('carrera_form2/', carreraForm2, name="carrera_form2"),
    path('docente_form/', docenteForm, name="docente_form"),

    path('buscar_duracion/', buscarDuracion, name="buscar_duracion"),
    path('buscar2/', buscar2, name="buscar2"),

    path('update_docente/<id_docente>/', updateDocente, name="update_docente"),
    path('update_carrera/<id_carrera>/', updateCarrera, name="update_carrera"),
    path('update_postgrado/<id_postgrado>/', updatePostgrado, name="update_postgrado"),
    path('delete_docente/<id_docente>/', deleteDocente, name="delete_docente"),
    path('delete_carrera/<id_carrera>/', deleteCarrera, name="delete_carrera"),
    path('delete_postgrado/<id_postgrado>/', deletePostgrado, name="delete_postgrado"),
    path('create_carrera/', createCarrera, name="create_carrera"),
    path('create_postgrado/', createPostgrado, name="create_postgrado"),
    path('create_docente/', createDocente, name="create_docente"),

    path('alumnos/', AlumnoList.as_view(), name="alumnos"),
    path('create_alumno/', AlumnoCreate.as_view(), name="create_alumno"),
    path('detail_alumno/<int:pk>/', AlumnoDetail.as_view(), name="detail_alumno"),
    path('update_alumno/<int:pk>/', AlumnoUpdate.as_view(), name="update_alumno"),
    path('delete_alumno/<int:pk>/', AlumnoDelete.as_view(), name="delete_alumno"),

    path('login/', login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name="app/logout.html"), name="logout"),
    path('register/', register, name="register"),

    path('editar_perfil/', editarPerfil, name="editar_perfil"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),

    path('view_postgrado/<id_postgrado>/', viewPostgrado, name="view_postgrado"),
    path('view_carrera/<id_carrera>/', viewCarrera, name="view_carrera"),
    path('view_docente/<id_docente>/', viewDocente, name="view_docente"),


]
