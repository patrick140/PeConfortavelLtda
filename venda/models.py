from django.db import models
from django.utils import timezone
from clientes.models import Clientes

# Create your models here.

class Venda(models.Model):
    numero = models.AutoField(primary_key=True, 
                           help_text='Numero da venda')
    data_venda = models.DateField(null=True,
                                  blank=True,
                                  default=timezone.now(), 
                            help_text='data da venda')
    valor_venda = models.FloatField(help_text='Valor da venda')
    
    cliente_cpf = models.ForeignKey(Clientes, null=True, blank=True,
                                      related_name='cliente',
                                      on_delete=models.SET_NULL,)
    
    
    def __str__(self):
        return f'{self.numero} - {self.cliente_cpf}'
