from django.shortcuts import render, redirect
from fornecedores.models import Fornecedores
from fornecedores.forms import FornecedoresForm, FornecedoresAtualizarForm

# Create your views here.

def listar(request):
    lista_fornecedores = Fornecedores.objects.all()
    contexto = {
        'fornecedores': lista_fornecedores,
    }
    return render(request, 'fornecedores/listarFornecedores.html', context=contexto)

def cadastro(request):
    return render(request, 'fornecedores/cadastroFornecedores.html')

def cadastrar(request):
    form = FornecedoresForm(request.POST)
    if form.is_valid():
        dados_fornecedores = form.cleaned_data
        fornecedores = Fornecedores(
            nome = dados_fornecedores['nome'],
        )
        fornecedores.save()
    return render(request, 'fornecedores/cadastroFornecedores.html')

def excluir(request, codigo):
    fornecedores = Fornecedores.objects.get(pk=codigo)
    fornecedores.delete()

    return redirect('fornecedores:listar')

def carregar_fornecedores(request, codigo):
    # obter titulo a atualizar baseado no codigo informado
    fornecedores = Fornecedores.objects.get(pk=codigo)
    contexto = {
        'fornecedores': fornecedores,
    }
    return render(request, 'fornecedores/atualizarFornecedores.html', context=contexto)

def atualizar(request):
    if request.method == 'POST':
        form = FornecedoresAtualizarForm(request.POST)
        if form.is_valid():

            dados_fornecedores = form.cleaned_data

            codigo = dados_fornecedores['codigo']

            fornecedores = Fornecedores.objects.get(pk=codigo)
            fornecedores.nome = dados_fornecedores['nome']
            

            fornecedores.save()

        # imprimir no console mensagens de erro na validação do formulario
        else:
            print(form.errors)
    return redirect('fornecedores:listar')