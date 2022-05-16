from django import views
from django.urls import path
from .views import *

urlpatterns= [
path('', inicio, name='inicio'),
path('colectivo/', colectivo, name='colectivo'),
path('pasaje/', pasaje, name='pasaje'),
path('persona/', persona, name='persona'),
path('viaje/', viaje, name='viaje'),
path('formularios/',formularios, name='formularios')






]