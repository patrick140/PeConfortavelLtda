from django.shortcuts import render, redirect
from produtos.models import Produtos
from produtos.forms import ProdutosForm, ProdutosAtualizaForm
from fornecedores.models import Fornecedores
# Create your views here.

def listar(request):
    lista_produtos = Produtos.objects.all()
    contexto = {
        'produtos': lista_produtos,
    }
    return render(request, 'produtos/listarProdutos.html', context=contexto)

def cadastro(request):
    cadastra_produtos = Fornecedores.objects.all()
    contexto = {
        'fornecedores': cadastra_produtos,
    }
    return render(request, 'produtos/cadastroProdutos.html', context=contexto)

def cadastrar(request):
    form = ProdutosForm(request.POST)
    if form.is_valid():
        dados_produtos = form.cleaned_data
        produtos = Produtos(
            nome = dados_produtos['nome'],
            precoCompra = dados_produtos['precoCompra'],
            precoVenda = dados_produtos['precoVenda'],
            cor = dados_produtos['cor'],
            imagem = dados_produtos['imagem'],
            fornecedoresCodigo = dados_produtos['fornecedoresCodigo'],
        )
        produtos.save()
    return render(request, 'produtos/cadastroProdutos.html')

def excluir(request, codigo):
    produtos = Produtos.objects.get(pk=codigo)
    produtos.delete()

    return redirect('produtos:listar')

def carregar_produtos(request, codigo):
    # obter titulo a atualizar baseado no codigo informado
    produtos = Produtos.objects.get(pk=codigo)
    fornecedores = Fornecedores.objects.all()
    contexto = {
        'produtos': produtos,
        'fornecedores': fornecedores,
    }
    return render(request, 'produtos/atualizarProdutos.html', context=contexto)

def atualizar(request):
    if request.method == 'POST':
        form = ProdutosAtualizaForm(request.POST)
        if form.is_valid():

            dados_produtos = form.cleaned_data

            codigo = dados_produtos['codigo']

            produtos = Produtos.objects.get(pk=codigo)
            produtos.nome = dados_produtos['nome']
            produtos.precoCompra = dados_produtos['precoCompra']
            produtos.precoVenda = dados_produtos['precoVenda']
            produtos.cor = dados_produtos['cor']
            produtos.imagem = dados_produtos['imagem']
            produtos.fornecedoresCodigo = dados_produtos['fornecedoresCodigo']

            produtos.save()

        # imprimir no console mensagens de erro na validação do formulario
        else:
            print(form.errors)
    return redirect('produtos:listar')



