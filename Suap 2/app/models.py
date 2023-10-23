from django.db import models

#-------------------------------------------------------

class cidade(models.Model):
    nome = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)
    def __str__(self):
        return f'{self.nome} {self.uf}'

#-------------------------------------------------------

class instituicao(models.Model):
    nome = models.CharField(max_length=50)
    site = models.CharField(max_length=50)
    numero = models.CharField(max_length=50)
    cidade = models.ForeignKey(cidade, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.nome} {self.site} {self.cidade}'
    
#-------------------------------------------------------

class horario(models.Model):
    periodo = models.CharField(max_length=50)
    horario = models.CharField(max_length=50)

    def __str__(self):
         return f'{self.periodo} {self.horario}'
    
#-------------------------------------------------------

class areasaber(models.Model):
    nome = models.CharField(max_length=50)
    area = models.CharField(max_length=50)

    def __str__(self):
        
        return f' {self.nome} {self.area}'

#-------------------------------------------------------

class disciplina(models.Model):
    nome = models.CharField(max_length=50)
    ementa = models.CharField(max_length=50)
    areasaber = models.ForeignKey(areasaber, on_delete=models.CASCADE)

    def __str__(self):
         return f'{self.nome} {self.ementa}'
    
#-------------------------------------------------------

class ocupacao(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
#------------------------------------------------------

class curso(models.Model):
    nome = models.CharField(max_length=50)
    disciplina = models.ForeignKey(disciplina, on_delete=models.CASCADE)
    ementa = models.CharField(max_length=50)
    carga = models.CharField(max_length=50)
    duracao = models.CharField(max_length=50)
    instituicao = models.ForeignKey(instituicao, on_delete=models.CASCADE)

    def __str__(self):
        return f' {self.nome} {self.disciplina} {self.carga} {self.ementa} {self.instituicao} {self.carga} {self.duracao}'

# -------------------------------------------------------

class pessoa(models.Model):
    ocupacao = models.ForeignKey(ocupacao, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    pai = models.CharField(max_length=50)
    mae = models.CharField(max_length=50)
    cpf = models.CharField(max_length=50)
    nascimento = models.DateField()
    email = models.CharField(max_length=50)
    cidade = models.ForeignKey(cidade, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.ocupacao} {self.nome} {self.pai} {self.mae} {self.cpf} {self.nascimento} {self.email} {self.cidade}'

# -------------------------------------------------------

class matricula(models.Model):
    pessoa = models.ForeignKey(pessoa, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=50)
    instituicao = models.ForeignKey(instituicao, on_delete=models.CASCADE)
    curso = models.ForeignKey(curso, on_delete=models.CASCADE)
    inicio = models.DateField()
    fim = models.DateField()

    def __str__(self):
        return f'{self.pessoa} {self.instituição} {self.curso} {self.pessoa} {self.cpf} {self.inicio} {self.fim} '

# -------------------------------------------------------

class turma(models.Model):
    nome_do_curso = models.CharField(max_length=50)
    pessoa = models.ForeignKey(pessoa, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nome} {self.email} {self.cpf}'

# -------------------------------------------------------

class frequencia(models.Model):
    data = models.DateField()
    turma = models.ForeignKey(turma, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(pessoa , on_delete=models.CASCADE)
    faltas = models.CharField(max_length=1)
    
    def __str__(self):
        return f'{self.data} {self.turma} {self.pessoa}{self.faltas}'
    
# -------------------------------------------------------

class ocorrencia(models.Model):
    data = models.DateField()
    nome = models.CharField(max_length=20)
    disciplina = models.ForeignKey(disciplina, on_delete=models.CASCADE)
    curso = models.ForeignKey(curso, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(pessoa , on_delete=models.CASCADE)


    descricao = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.nome} {self.descricao} {self.data} {self.curso} {self.pessoa}'

# -------------------------------------------------------

class avaliacao(models.Model):
    nome = models.CharField(max_length=20)
    descricao = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.nome} {self.descricao}'
    
# -------------------------------------------------------

