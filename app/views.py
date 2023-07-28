from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

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
