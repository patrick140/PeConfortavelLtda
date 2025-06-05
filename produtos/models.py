from django.db import models

# Create your models here.

class Produtos(models.Model):
    codigo = models.AutoField(primary_key=True, 
                           help_text='Codigo do produto')
    nome = models.CharField(max_length=70, 
                            help_text='Nome do produto')
    precoDeCompra = models.FloatField(
                                help_text='Preço de compra do Produto')
    precoDeVenda = models.CharField(
                                help_text='Preço de venda do produto')
    cor = models.CharField(max_length=20, 
                           help_text='Cor do produto')
    dataFabricacao = models.DateField(max_length=50,
                                help_text='Cidade do cliente')
    imagem = models.CharField(max_length=25,
                                help_text='Nome da imagem do produto')
    
    
    def __str__(self):
        return f'{self.codigo} - {self.nome}'