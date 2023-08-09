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

def becas(request):
    return render(request, "app/becas.html")

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
        

def docentes(request):
    ctx = {'docentes': Docente.objects.all() }
    return render(request, "app/docentes.html", ctx) 

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

def deleteDocente(request, id_docente):
    docente = Docente.objects.get(id=id_docente)
    docente.delete()
    return redirect(reverse_lazy('docentes'))

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


def carreras(request):
    ctx = {'carreras': Carrera.objects.all() }
    return render(request, "app/carreras.html", ctx)

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

def deleteCarrera(request, id_carrera):
    carrera = Carrera.objects.get(id=id_carrera)
    carrera.delete()
    return redirect(reverse_lazy('carreras'))

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



def postgrados(request):
    ctx = {'postgrados': Postgrado.objects.all() }
    return render(request, "app/postgrados.html", ctx)

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

def deletePostgrado(request, id_postgrado):
    postgrado = Postgrado.objects.get(id=id_postgrado)
    postgrado.delete()
    return redirect(reverse_lazy('postgrados'))

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


class AlumnoList(ListView):
    model = Alumno

class AlumnoCreate(CreateView):
    model = Alumno
    fields = ['nombre', 'apellido', 'email']
    success_url = reverse_lazy('alumnos')

class AlumnoDetail(DetailView):
    model = Alumno

class AlumnoUpdate(UpdateView):
    model = Alumno
    fields = ['nombre', 'apellido', 'email']
    success_url = reverse_lazy('alumnos') 

class AlumnoDelete(DeleteView):
    model = Alumno
    success_url = reverse_lazy('alumnos')           

