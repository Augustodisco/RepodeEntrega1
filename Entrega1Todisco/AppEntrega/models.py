from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre= models.CharField(max_length=50)
    telefono=models.IntegerField()

class Viaje(models.Model):
    destino=models.CharField(max_length=50)

class Pasaje(models.Model):
    piso=models.CharField(max_length=10)
    asiento=models.IntegerField()
    fecha=models.CharField(max_length=10)

class Colectivo(models.Model):
    marca=models.CharField(max_length=50)
    patente=models.IntegerField()
