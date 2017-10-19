from django.db import models
from django.utils import timezone

class Aluno(models.Model):
    nome = models.CharField(blank=False, max_length=200)
    idade = models.IntegerField(blank=False)
    nome_responsavel = models.CharField(blank=False)
    contato = models.CharField(blank=False)
    data_de_atendimento = models.DateField(blank=False, default=timezone.now)

    def __init__(self, nome, idade, nome_responsavel, contato, data_de_atendimento):
        self.nome = nome
        self.idade = idade
        self.nome_responsavel = nome_responsavel
        self.contato = contato

