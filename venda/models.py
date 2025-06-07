from django.db import models
from django.utils import timezone

# Create your models here.

class Venda(models.Model):
    numero = models.AutoField(primary_key=True, 
                           help_text='Numero da venda')
    data_venda = models.DateField(null=True,
                                  blank=True,
                                  default=timezone.now(), 
                            help_text='data da venda')
    valor_venda = models.FloatField(help_text='Valor da venda')
    
    cliente_cpf = models.CharField(max_length=11, 
                                   unique=True)
    
    def __str__(self):
        return f'{self.numero} - {self.cliente_cpf}'
