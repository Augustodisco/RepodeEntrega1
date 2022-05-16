from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from AppEntrega.forms import PersonaFormulario
from .models import Persona

# Create your views here.
def inicio(request):
    return render (request, 'AppEntrega/inicio.html')

def colectivo(request):
    return render (request, 'AppEntrega/colectivo.html' )

def pasaje(request):
    return render (request, 'AppEntrega/pasaje.html')

def persona(request):
    return render (request, 'AppEntrega/persona.html')

def viaje(request):
    return render (request, 'AppEntrega/viaje.html')

def formularios(request):
    return render (request, 'AppEntrega/formularios.html')

def personas(request):
    if request.method == 'POST':
        
        miFormulario=PersonaFormulario(request.POST)
        print(miFormulario)
        
        

        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            persona=Persona(nombre=informacion['nombre'],telefono=informacion['telefono'])
            persona.save()
            return render(request, 'AppEntrega/inicio.html')
    else:
        miFormulario=PersonaFormulario()    
    return render(request, 'AppEntrega/persona.html', {'miformulario': miFormulario})



