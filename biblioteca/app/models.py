from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)
    def __str__(self):
        return f'{self.nome} {self.uf}'

class Autor(models.Model):
    nome = models.CharField(max_length=50)
    site = models.CharField(max_length=50)
    Cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.nome} {self.site} {self.Cidade}'

class Editora(models.Model):
    nome = models.CharField(max_length=50)
    site = models.CharField(max_length=50)
    Cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
         return f'{self.nome} {self.site} {self.Cidade}'

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    nome = models.CharField(max_length=50)
    Autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    Editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    preço = models.PositiveBigIntegerField()
    publicação = models.DateField()

    def __str__(self):
        return f'{self.nome} {self.Autor} {self.Editora} {self.Categoria} {self.preço} {self.publicação}'


class Leitor(models.Model):
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    cpf = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nome} {self.email} {self.cpf}'

class Emprestimo(models.Model):
    data = models.DateField()
    Livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    Leitor = models.ForeignKey(Leitor , on_delete=models.CASCADE)
    devolucaodata = models.DateField()
    
    def __str__(self):
        return f'{self.data} {self.Livro} {self.Leitor}{self.devolucaodata}'