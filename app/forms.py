from django import forms

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