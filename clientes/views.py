from django.shortcuts import render, redirect
from clientes.models import Clientes
from clientes.forms import ClientesForm, ClientesAtualizaForm

# Create your views here.

def listar(request):
    lista_clientes = Clientes.objects.all()
    contexto = {
        'clientes': lista_clientes,
    }
    return render(request, 'clientes/listarClientes.html', context=contexto)

def cadastrar(request):
    form = ClientesForm(request.POST)
    if form.is_valid():
        dados_clientes = form.cleaned_data
        clientes = Clientes(
            cpf = dados_clientes['cpf'],
            nome = dados_clientes['nome'],
            endereco = dados_clientes['endereco'],
            telefone = dados_clientes['telefone'],
            uf = dados_clientes['uf'],
            cidade = dados_clientes['cidade'],
            genero = dados_clientes['genero'],
            contato = dados_clientes['contato'],
            email = dados_clientes['email'],
            senha = dados_clientes['senha'],
        )
        clientes.save()
    return render(request, 'clientes/cadastroClientes.html')

def cadastro(request):
    return render(request, 'clientes/cadastroClientes.html')

def excluir(request, cpf):
    clientes = Clientes.objects.get(pk=cpf)
    clientes.delete()

    return redirect('clientes:listar')

def carregar_clientes(request, cpf):
    # obter titulo a atualizar baseado no codigo informado
    clientes = Clientes.objects.get(pk=cpf)
    contexto = {
        'clientes': clientes,
    }
    return render(request, 'clientes/atualizarClientes.html', context=contexto)

def atualizar(request):
    if request.method == 'POST':
        form = ClientesAtualizaForm(request.POST)
        if form.is_valid():

            dados_clientes = form.cleaned_data

            cpf = dados_clientes['cpf']

            clientes = Clientes.objects.get(pk=cpf)
            clientes.nome = dados_clientes['nome']
            clientes.telefone = dados_clientes['telefone']
            clientes.endereco = dados_clientes['endereco']
            clientes.cidade = dados_clientes['cidade']
            clientes.uf = dados_clientes['uf']
            clientes.contato = dados_clientes['contato']
            clientes.genero = dados_clientes['genero']
            clientes.email = dados_clientes['email']
            clientes.senha = dados_clientes['senha']

            clientes.save()

        # imprimir no console mensagens de erro na validação do formulario
        else:
            print(form.errors)
    return redirect('clientes:listar')

