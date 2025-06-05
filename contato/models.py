from django.db import models

# Create your models here.

class Contato(models.Model):
    nomeCompleto = models.CharField(primary_key=True,max_length=100, 
                           help_text='Nome completo do contato')
    email = models.CharField(max_length=100, 
                            help_text='E-mail do contato')
    telefone = models.CharField(max_length=11,
                                help_text='Telefone do contato')
    melhorHoraContato = models.CharField(max_length=10,
                                help_text='Melhor hora para contato do cliente')
    mensagem = models.CharField(max_length=1024,
                                help_text='Text com a mensagem a ser enviada ao SAC da empresa')

    def __str__(self):
            return f'{self.nomeCompleto}'    