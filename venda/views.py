from django.shortcuts import render
from venda.models import Venda, item_venda
from produtos.models import Produtos
from venda.forms import VendaForm, VendaAtualizaForm, item_vendaForm
# Create your views here.

def listar(request):
    Lista_vendas = Venda.objects.all()
    contexto = {
        'venda': Lista_vendas,
    }
    return render(request, 'venda/listaVenda.html', context=contexto)

def cadastro(request):
    cadastra_produtos = Produtos.objects.all()
    contexto = {
        'produtos': cadastra_produtos,
    }
    return render(request, 'venda/registroVendaCliente.html', context=contexto)

def cadastrar(request):
    form = VendaForm(request.POST)
    form2 = item_vendaForm(request.POST) 
    if form.is_valid() and form2.is_valid():
        dados_venda = form.cleaned_data
        dados_itemVenda = form.cleaned_data
        venda = Venda(
            dataVenda = dados_venda['dataVenda'],
            valorVenda = dados_venda['valorVenda'],
            clienteCpf = dados_venda['clienteCpf'],
        )
        itemVenda = item_venda(
            vendaNumero = dados_itemVenda['vendaNumero'],
            produtoCodigo = dados_itemVenda['produtoCodigo'],
            quantidade = dados_itemVenda['quantidade'],
            precoVenda = dados_itemVenda['precoVenda'],
        )
        venda.save()
        itemVenda.save()
    return render(request, 'venda/registroVendaCliente.html')