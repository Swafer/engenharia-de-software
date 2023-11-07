from django.db import models

class pessoa(models.Model):
    idpessoa = models.CharField(max_length=3)
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nome} {self.idpessoa} {self.idade} {self.tipo}'

class modelo(models.Model):
    idmodelo = models.CharField(max_length=3)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nome} {self.idmodelo}'
    
class marca(models.Model):
    idmarca = models.CharField(max_length=3)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nome} {self.idmarca}'
    
class categoria(models.Model):
    idcategoria = models.CharField(max_length=3)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nome} {self.idcategoria}'

class vagas(models.Model):
    idvaga = models.CharField(max_length=3)
    lvaga = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.idvaga} {self.lvaga}'
    
class carro(models.Model):
    idcarro = models.CharField(max_length=3)
    data_entrada = models.DateField()
    data_saida = models.DateField()
    cor = models.CharField(max_length=50)
    placa = models.CharField(max_length=50)
    modelo= models.ForeignKey(modelo,on_delete=models.CASCADE)
    marca= models.ForeignKey(marca,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.idcarro} {self.data_entrada} {self.data_saida} {self.cor} {self.placa}'
    
class reparo(models.Model):
    idmodelo = models.CharField(max_length=3)
    nome = models.CharField(max_length=50)
    veiculo= models.ForeignKey(carro,on_delete=models.CASCADE)
    mecanico= models.ForeignKey(pessoa,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.nome} {self.idmodelo} {self.veiculo} {self.mecanico}'
