from django import forms
from clientes.models import Clientes
from venda.models import Venda
from produtos.models import Produtos

#classe formulario inclusao
class VendaForm(forms.Form):
    dataVenda = forms.DateField(help_text='Valor da venda')

    valorVenda = forms.FloatField(help_text='Valor da venda')

    clienteCpf = forms.ModelChoiceField(
        queryset=Clientes.objects.all(),
        help_text='Informe o cpf do cliente'
    )

class VendaAtualizaForm(forms.Form):
    numero = forms.IntegerField(
                           help_text='Numero da venda')
    dataVenda = forms.DateField(help_text='Valor da venda')

    valorVenda = forms.FloatField(help_text='Valor da venda')

    clienteCpf = forms.ModelChoiceField(
        queryset=Clientes.objects.all(),
        help_text='Informe o cpf do cliente'
    )

class item_vendaForm(forms.Form):
    vendaNumero = forms.ModelChoiceField(
        queryset=Venda.objects.all(),
        help_text='Informe o numero da venda'
    )
    
    produtoCodigo = forms.ModelChoiceField(
        queryset=Produtos.objects.all(),
        help_text='Informe o codigo do produto'
    )

    quantidade = forms.IntegerField(
        help_text='Informe a quantidade do item'
    )

    precoVenda = forms.FloatField(
        help_text='Informe o preço de venda do produto'
    )

