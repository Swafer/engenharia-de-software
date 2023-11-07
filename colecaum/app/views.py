from django.shortcuts import render
from .models import*

def carros(request):
    carros = {
         'carros':carro.objects.all()
        }
    return render(request, 'carros/carros.html', carros)
