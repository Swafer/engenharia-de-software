from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(sefl):
        return self.nome
class Marca(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
class Produto(models.Model):
    nome = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    quatidade = models.IntegerField()
    preco = models.PositiveBigIntegerField()
    disponibilidade = models.BooleanField()
    data = models.DateField()


    def __str__(self):
        return f'{self.categoria}{self.marca}{self.nome}'
