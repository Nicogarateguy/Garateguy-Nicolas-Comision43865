from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, "app/base.html")

def carreras(request):
    ctx = {"carreras": Carrera.objects.all() }
    return render(request, "app/carreras.html", ctx)

def postgrados(request):
    ctx = {"postgrados": Postgrado.objects.all() }
    return render(request, "app/postgrados.html", ctx)

def docentes(request):
    ctx = {"docentes": Docente.objects.all() }
    return render(request, "app/docentes.html", ctx)

def alumnos(request):
    return render(request, "app/alumnos.html")

def sobremi(request):
    return render(request, "app/sobremi.html")

def alumniblue(request):
    return render(request, "app/alumniblue.html")

def carreraForm(request):
    if request.method == "POST":
        carrera = Carrera(nombre=request.POST['nombre'], modalidad=request.POST['modalidad'], duracion=request.POST['duracion'], financiacion=request.POST['financiacion'])
        carrera.save()
        return HttpResponse("Carrera ingresada correctamente") 
    return render(request, "app/carreraForm.html")

def postgradoForm(request): 
    if request.method == "POST":
        postgrado = Postgrado(nombre=request.POST['nombre'], modalidad=request.POST['modalidad'], duracion=request.POST['duracion'], financiacion=request.POST['financiacion'])
        postgrado.save()
        return HttpResponse("Postgrado ingresado correctamente") 
    return render(request, "app/postgradoForm.html")

def docenteForm(request): 
    if request.method == "POST":
        docente = Docente(nombre=request.POST['nombre'], apellido=request.POST['apellido'], email=request.POST['email'], profesion=request.POST['profesion'])
        docente.save()
        return HttpResponse("Docente ingresado correctamente") 
    return render(request, "app/docenteForm.html")

def carreraForm2(request):
    if request.method == "POST":
       miForm = CarreraForm(request.POST)
       print(miForm)
       if miForm.is_valid:
           info = miForm.cleaned_data
           carrera = Carrera(nombre=info['nombre'], modalidad=info['modalidad'], duracion=info ['duracion'], financiacion=info['financiacion'])
           carrera.save()
           return render(request, "app/base.html")
    else:
        miForm = CarreraForm()      
    return render(request, "app/carreraForm2.html", {"form":miForm})



def buscarDuracion(request):
    return render(request, "app/buscarDuracion.html")

def buscar2(request):
    if 'duracion' in request.GET:
        duracion = request.GET['duracion']
        carreras = Carrera.objects.filter(duracion__icontains=duracion)
        if duracion:
            return render(request, "app/resultadosDuracion.html", {"duracion": duracion, "carreras":carreras})
        else:
            return HttpResponse("No se ingresaron datos")
        
@login_required
def docentes(request):
    ctx = {'docentes': Docente.objects.all() }
    return render(request, "app/docentes.html", ctx) 

@login_required
def updateDocente(request, id_docente):
    docente = Docente.objects.get(id=id_docente)
    if request.method == "POST":
        miForm = DocenteForm(request.POST)
        if miForm.is_valid():
            docente.nombre = miForm.cleaned_data.get('nombre')
            docente.apellido = miForm.cleaned_data.get('apellido')
            docente.email = miForm.cleaned_data.get('email')
            docente.profesion = miForm.cleaned_data.get('profesion')
            docente.save()
            return redirect(reverse_lazy('docentes'))      
    else:
        miForm = DocenteForm(initial={'nombre':docente.nombre, 
                                       'apellido':docente.apellido, 
                                       'email':docente.email, 
                                       'profesion':docente.profesion})         
    return render(request, "app/docenteForm.html", {'form': miForm})  

@login_required
def deleteDocente(request, id_docente):
    docente = Docente.objects.get(id=id_docente)
    docente.delete()
    return redirect(reverse_lazy('docentes'))

@login_required
def createDocente(request):
    if request.method == "POST":
        miForm = DocenteForm(request.POST)
        if miForm.is_valid():
            d_nombre = miForm.cleaned_data.get('nombre')
            d_apellido = miForm.cleaned_data.get('apellido')
            d_email = miForm.cleaned_data.get('email')
            d_profesion = miForm.cleaned_data.get('profesion')
            docente = Docente( nombre=d_nombre, 
                              apellido=d_apellido, 
                              email=d_email, 
                              profesion=d_profesion, 
                              )

            docente.save()
            return redirect(reverse_lazy('docentes'))      
    else:
        miForm = DocenteForm()   

    return render(request, "app/docenteForm.html", {'form': miForm}) 

@login_required
def viewDocente(request, id_docente):
    docente = Docente.objects.get(id=id_docente)
    return render(request, "app/docente_view.html", {'docente': docente}) 

@login_required
def carreras(request):
    ctx = {'carreras': Carrera.objects.all() }
    return render(request, "app/carreras.html", ctx)

@login_required
def updateCarrera(request, id_carrera):
    carrera = Carrera.objects.get(id=id_carrera)
    if request.method == "POST":
        miForm = CarreraForm(request.POST)
        if miForm.is_valid():
            carrera.nombre = miForm.cleaned_data.get('nombre')
            carrera.modalidad = miForm.cleaned_data.get('modalidad')
            carrera.duracion = miForm.cleaned_data.get('duracion')
            carrera.financiacion = miForm.cleaned_data.get('financiacion')
            carrera.save()
            return redirect(reverse_lazy('carreras'))      
    else:
        miForm = CarreraForm(initial={'nombre':carrera.nombre, 
                                      'modalidad':carrera.modalidad, 
                                      'duracion':carrera.duracion, 
                                      'financiacion':carrera.financiacion})         
    return render(request, "app/carreraForm2.html", {'form': miForm})  

@login_required
def deleteCarrera(request, id_carrera):
    carrera = Carrera.objects.get(id=id_carrera)
    carrera.delete()
    return redirect(reverse_lazy('carreras'))

@login_required
def createCarrera(request):
    if request.method == "POST":
        miForm = CarreraForm(request.POST)
        if miForm.is_valid():
            c_nombre = miForm.cleaned_data.get('nombre')
            c_modalidad = miForm.cleaned_data.get('modalidad')
            c_duracion = miForm.cleaned_data.get('duracion')
            c_financiacion = miForm.cleaned_data.get('financiacion')
            carrera = Carrera( nombre=c_nombre, 
                              modalidad=c_modalidad, 
                              duracion=c_duracion, 
                              financiacion=c_financiacion, 
                              )

            carrera.save()
            return redirect(reverse_lazy('carreras'))      
    else:
        miForm = CarreraForm()   

    return render(request, "app/carreraForm2.html", {'form': miForm})

@login_required
def viewCarrera(request, id_carrera):
    carrera = Carrera.objects.get(id=id_carrera)
    return render(request, "app/carrera_view.html", {'carrera': carrera}) 


@login_required
def postgrados(request):
    ctx = {'postgrados': Postgrado.objects.all() }
    return render(request, "app/postgrados.html", ctx)

@login_required
def updatePostgrado(request, id_postgrado):
    postgrado = Postgrado.objects.get(id=id_postgrado)
    if request.method == "POST":
        miForm = PostgradoForm(request.POST)
        if miForm.is_valid():
            postgrado.nombre = miForm.cleaned_data.get('nombre')
            postgrado.modalidad = miForm.cleaned_data.get('modalidad')
            postgrado.duracion = miForm.cleaned_data.get('duracion')
            postgrado.financiacion = miForm.cleaned_data.get('financiacion')
            postgrado.save()
            return redirect(reverse_lazy('postgrados'))      
    else:
        miForm = PostgradoForm(initial={'nombre':postgrado.nombre, 
                                      'modalidad':postgrado.modalidad, 
                                      'duracion':postgrado.duracion, 
                                      'financiacion':postgrado.financiacion})         
    return render(request, "app/postgradoForm.html", {'form': miForm})

@login_required
def deletePostgrado(request, id_postgrado):
    postgrado = Postgrado.objects.get(id=id_postgrado)
    postgrado.delete()
    return redirect(reverse_lazy('postgrados'))

@login_required
def createPostgrado(request):
    if request.method == "POST":
        miForm = PostgradoForm(request.POST)
        if miForm.is_valid():
            p_nombre = miForm.cleaned_data.get('nombre')
            p_modalidad = miForm.cleaned_data.get('modalidad')
            p_duracion = miForm.cleaned_data.get('duracion')
            p_financiacion = miForm.cleaned_data.get('financiacion')
            postgrado = Postgrado( nombre=p_nombre, 
                              modalidad=p_modalidad, 
                              duracion=p_duracion, 
                              financiacion=p_financiacion, 
                              )

            postgrado.save()
            return redirect(reverse_lazy('postgrados'))      
    else:
        miForm = PostgradoForm()   

    return render(request, "app/postgradoForm.html", {'form': miForm}) 

@login_required
def viewPostgrado(request, id_postgrado):
    postgrado = Postgrado.objects.get(id=id_postgrado)
    return render(request, "app/postgrado_view.html", {'postgrado': postgrado}) 


class AlumnoList(LoginRequiredMixin, ListView):
    model = Alumno

class AlumnoCreate(LoginRequiredMixin, CreateView):
    model = Alumno
    fields = ['nombre', 'apellido', 'email']
    success_url = reverse_lazy('alumnos')

class AlumnoDetail(LoginRequiredMixin, DetailView):
    model = Alumno

class AlumnoUpdate(LoginRequiredMixin, UpdateView):
    model = Alumno
    fields = ['nombre', 'apellido', 'email']
    success_url = reverse_lazy('alumnos') 

class AlumnoDelete(LoginRequiredMixin, DeleteView):
    model = Alumno
    success_url = reverse_lazy('alumnos') 


def login_request(request):
    miForm = AuthenticationForm()

    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            clave = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = '/media/avatares/default.png'
                finally:
                    request.session['avatar'] = avatar
                    
                return render(request, 'app/base.html', {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render(request, 'app/login.html', {"form":miForm, "mensaje": "Datos incorrectos"})
        else:
            return render(request, 'app/login.html', {"form":miForm, "mensaje": "Datos incorrectos"})

    return render(request, "app/login.html", {"form":miForm})

def register(request):
    if request.method == 'POST':
        form = RegistroUsuariosForm(request.POST) # UserCreationForm 
        if form.is_valid():  # Si pasó la validación de Django
            usuario = form.cleaned_data.get('username')
            form.save()
            return render(request, "app/base.html", {"mensaje1":"Usuario Creado con Éxito"})        
    else:
        form = RegistroUsuariosForm()

    return render(request, "app/registro.html", {"form": form}) 

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request, "app/base.html", {'mensaje': f"Usuario {usuario.username} actualizado correctamente"})
        else:
            return render(request, "app/editarPerfil.html", {'form': form})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "app/editarPerfil.html", {'form': form, 'usuario':usuario.username})


@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)
            #_________________ Esto es para borrar el avatar anterior
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0: # Si esto es verdad quiere decir que hay un Avatar previo
                avatarViejo[0].delete()

            #_________________ Grabo avatar nuevo
            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()

            #_________________ Almacenar en session la url del avatar para mostrarla en base
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session['avatar'] = imagen

            return render(request, "app/base.html")
    else:
        form = AvatarFormulario()
    return render(request, "app/agregarAvatar.html", {'form': form})


