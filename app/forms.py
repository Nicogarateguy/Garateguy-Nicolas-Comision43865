from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CarreraForm(forms.Form):
    nombre = forms.CharField(label="Nombre de la carrera", max_length=50, required=True)
    modalidad = forms.CharField(label="Modalidad", max_length=20, required=True)
    duracion = forms.CharField(label="Duracion", max_length=20, required=True)
    financiacion = forms.CharField(label="Financiacion", max_length=20, required=False)

class PostgradoForm(forms.Form):
    nombre = forms.CharField(label="Nombre del postgrado", max_length=50, required=True)
    modalidad = forms.CharField(label="Modalidad", max_length=20, required=True)
    duracion = forms.CharField(label="Duracion", max_length=20, required=True)
    financiacion = forms.CharField(label="Financiacion", max_length=20, required=False)    


class DocenteForm(forms.Form):
    nombre = forms.CharField(label="Nombre del docente", max_length=50, required=True)
    apellido = forms.CharField(label="Apellido del docente", max_length=20, required=True)
    email = forms.EmailField(label="Email", required=False)
    profesion = forms.CharField(label="Profesion", max_length=20, required=True)  

class RegistroUsuariosForm(UserCreationForm):
    email = forms.EmailField(label="Email Usuario")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] 
        #Saca los mensajes de ayuda
        help_texts = { k:"" for k in fields}   


class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=False)
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=False)

    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2', 'first_name', 'last_name' ] 
        #Saca los mensajes de ayuda
        help_texts = { k:"" for k in fields}


class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)        