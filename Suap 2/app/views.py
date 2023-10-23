from django.shortcuts import render
from .models  import *

def consulta(request):
    consultas = {
         'matriculas':matricula.objects.all(),}

    return render(request,'consulta/Matriculas.html',consultas)

def cidadi(request):
    cidades = {
         'cidades':cidade.objects.all(),}

    return render(request,'consulta/cidades.html',cidades)

    