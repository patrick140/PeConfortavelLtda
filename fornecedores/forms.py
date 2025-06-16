from django import forms

#classe formulario inclusao
class FornecedoresForm(forms.Form):
    nome = forms.CharField(max_length=70, 
                            help_text='Nome do fornecedor')
    
class FornecedoresAtualizarForm(forms.Form):
    codigo = forms.IntegerField( 
                           help_text='Codigo do fornecedor')
    nome = forms.CharField(max_length=70, 
                            help_text='Nome do fornecedor')
    