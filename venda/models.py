from django.db import models
from django.utils import timezone
from clientes.models import Clientes
from produtos.models import Produtos

# Create your models here.

class Venda(models.Model):
    numero = models.AutoField(primary_key=True, 
                           help_text='Numero da venda')
    dataVenda = models.DateTimeField(null=True,
                                  blank=True,
                                  default=timezone.now(), 
                            help_text='data da venda')
    valorVenda = models.FloatField(help_text='Valor da venda')
    
    clienteCpf = models.ForeignKey(Clientes, null=True, blank=True,
                                      related_name='clienteCpf',
                                      on_delete=models.SET_NULL,)
    
    
    def __str__(self):
        return f'{self.numero} - {self.clienteCpf}'
    
class item_venda(models.Model):
    numero = models.AutoField(primary_key=True, 
                           help_text='Numero da venda')
    vendaNumero = models.ForeignKey(Venda, null=True, blank=True,
                                     related_name='vendaNumero',
                                     on_delete=models.SET_NULL,
                                     to_field='numero')
    produtoCodigo = models.ForeignKey(Produtos, null=True, blank=True,
                                     related_name='produtoCodigo',
                                     on_delete=models.SET_NULL,
                                     to_field='codigo')
    quantidade = models.IntegerField(help_text='quantidade do item')
    precoVenda = models.FloatField(
                                 help_text='Preço de venda do produto')
    
    def __str__(self):
        return f'{self.numero} - {self.precoVenda}'