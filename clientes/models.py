from django.db import models
from django.utils import timezone


class Clientes(models.Model):
    cpf = models.CharField(primary_key=True, max_length=14, 
                         help_text='CPF do cliente', unique=True)
    nome = models.CharField(max_length=70, 
                            help_text='Nome do cliente')
    endereco = models.CharField(max_length=100,
                                help_text='Endereço do Cliente')
    telefone = models.CharField(max_length=11,
                                help_text='Telefone do cliente')
    uf = models.CharField(max_length=2,
                                help_text='Estado de Domicilío do cliente')
    cidade = models.CharField(max_length=50,
                                help_text='Cidade do cliente')
    genero = models.CharField(max_length=1,
                                help_text='Genero do cliente')
    contato = models.CharField(max_length=1,
                                help_text='Contato do cliente')
    email = models.CharField(max_length=100,
                                help_text='E-mail do cliente')
    senha = models.CharField(max_length=256,
                                help_text='Senha')
    
    def __str__(self):
        return f'{self.nome} - {self.nome}'


