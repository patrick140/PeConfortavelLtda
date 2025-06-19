from django import forms
from clientes.models import Clientes
from venda.models import Venda
from produtos.models import Produtos

#classe formulario inclusao
class VendaForm(forms.Form):
    dataVenda = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        help_text='Data da venda'
    )
    valorVenda = forms.FloatField(
        widget=forms.NumberInput(attrs={'readonly': 'readonly'}),
        help_text='Valor total da venda'
    )
    clienteCpf = forms.ModelChoiceField(
        queryset=Clientes.objects.all(),
        to_field_name='cpf',
        help_text='Selecione o cliente'
    )

class item_vendaForm(forms.Form):
    produtoCodigo = forms.ModelChoiceField(
        queryset=Produtos.objects.all(),
        to_field_name='codigo',
        help_text='Selecione o produto'
    )
    quantidade = forms.IntegerField(
        min_value=1,
        help_text='Quantidade do item'
    )
    precoVenda = forms.FloatField(
        widget=forms.NumberInput(attrs={'readonly': 'readonly'}),
        help_text='Preço unitário do produto'
    )

