from django import forms

#classe formulario inclusao
class ProdutosForm(forms.Form):

    nome = forms.CharField(max_length=70, 
                            help_text='Nome do produto')
    preco_Compra = forms.FloatField(
                                help_text='Preço de compra do Produto')
    preco_Venda = forms.FloatField(
                                help_text='Preço de venda do produto')
    cor = forms.CharField(max_length=20, 
                           help_text='Cor do produto')
    imagem = forms.CharField(max_length=25,
                                help_text='Nome da imagem do produto')
    fornecedores_codigo = forms.CharField(max_length=70,
                                            help_text='Informe o fornecedor')
    
class ProdutosAtualizaForm(forms.Form):
    codigo = forms.IntegerField( 
                           help_text='Codigo do produto')
    nome = forms.CharField(max_length=70, 
                            help_text='Nome do produto')
    preco_Compra = forms.FloatField(
                                help_text='Preço de compra do Produto')
    preco_Venda = forms.FloatField(
                                help_text='Preço de venda do produto')
    cor = forms.CharField(max_length=20, 
                           help_text='Cor do produto')
    imagem = forms.CharField(max_length=25,
                                help_text='Nome da imagem do produto')
    fornecedores_codigo = forms.CharField(max_length=70,
                                            help_text='Informe o fornecedor')