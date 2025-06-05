from django.db import models

# Create your models here.

class Fornecedores(models.Model):
    codigo = models.AutoField(primary_key=True, 
                           help_text='Codigo do fornecedor')
    nome = models.CharField(max_length=70, 
                            help_text='Nome do fornecedor')
    
    def __str__(self):
        return f'{self.codigo} - {self.nome}'