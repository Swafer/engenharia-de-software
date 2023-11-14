from django.shortcuts import render
from .models import*

def carros(request):
    carros = {
         'carros':carro.objects.all()
        }
    return render(request, 'carros/carros.html', carros)

def espaco(request):
    espaco = {
         'espaco':vagas.objects.all()
        }
    return render(request, 'vagas/vagas.html', espaco)

def quiz(request):
    quiz = {
         'quiz':vagas.objects.all()
        }
    return render(request, 'quiz/quiz.html', quiz)

def marcas(request):
    marcas = {
        'marca' :marca.objects.all(),
        'modelo':modelo.objects.all()
        }
    return render(request, 'marcas/marcas.html', marcas)