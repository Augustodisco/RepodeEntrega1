from django import forms

class PersonaFormulario(forms.Form):
    nombre=forms.CharField(max_length=50)
    telefono=forms.IntegerField()
