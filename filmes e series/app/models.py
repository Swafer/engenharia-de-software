from tarfile import data_filter
from urllib.request import DataHandler
from django.db import models

# Create your models here.
class Cidade(models.Model):
    nome_cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    def __str__(self):
        return f"{self.nome_cidade}, {self.uf}"

class filme(models.Model):
    nome = models.CharField(max_length=100)
    dura = models.CharField(max_length=100)
    site_oficial = models.CharField(max_length=100)
    data_lancamento = models.DateField()
    nota = models.CharField(max_length=100)
    genero = models.ManyToManyField(genero)
    pais = models.ManyToManyField(pais)

    def __str__(self):
        return f'{self.nome} {self.dura} {self.site_oficial} {self.data_lancamento} {self.nota} {self.genero} {self.pais} {self.data_lancamento} {self.nota}'

class filmetor(models.Model):
    filme = models.ManyToManyField(filme)
    genero = models.ManyToManyField(genero)    
