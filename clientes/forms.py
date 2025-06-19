from django import forms

#classe formulario inclusao
class ClientesForm(forms.Form):
    cpf = forms.CharField(max_length=14, required=True, help_text='CPF do cliente')
    # ... other fields remain the same ...
    nome = forms.CharField(max_length=70,
                           required=True, 
                            help_text='Nome do cliente')
    endereco = forms.CharField(max_length=100,
                               required=True,
                                help_text='Endereço do Cliente')
    telefone = forms.CharField(max_length=11,
                               required=True,
                                help_text='Telefone do cliente')
    uf = forms.CharField(max_length=2,
                         required=True,
                                help_text='Estado de Domicilío do cliente')
    cidade = forms.CharField(max_length=50,
                             required=True,
                                help_text='Cidade do cliente')
    genero = forms.CharField(max_length=1,
                             required=True,
                                help_text='Genero do cliente')
    contato = forms.CharField(max_length=1,
                              required=True,
                                help_text='Contato do cliente')
    email = forms.CharField(max_length=100,
                            required=True,
                                help_text='E-mail do cliente')
    senha = forms.CharField(max_length=256,
                            required=True,
                                help_text='Senha')
    
class ClientesAtualizaForm(forms.Form):
    cpf = forms.CharField(max_length=14,
                          required=True, 
                           help_text='Cpf do cliente')
    nome = forms.CharField(max_length=70,
                           required=True, 
                            help_text='Nome do cliente')
    endereco = forms.CharField(max_length=100,
                               required=True,
                                help_text='Endereço do cliente')
    telefone = forms.CharField(max_length=11,
                               required=True,
                                help_text='Telefone do cliente')
    uf = forms.CharField(max_length=2,
                         required=True,
                                help_text='Estado de Domicilío do cliente')
    cidade = forms.CharField(max_length=50,
                             required=True,
                                help_text='Cidade do cliente')
    genero = forms.CharField(max_length=1,
                             required=True,
                                help_text='Genero do cliente')
    contato = forms.CharField(max_length=1,
                              required=True,
                                help_text='Contato do cliente')
    email = forms.CharField(max_length=100,
                            required=True,
                                help_text='E-mail do cliente')
    senha = forms.CharField(max_length=256,
                            required=True,
                                help_text='Senha')
    
