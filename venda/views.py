from django.shortcuts import render, redirect
from venda.models import Venda, item_venda
from produtos.models import Produtos
from clientes.models import Clientes
from venda.forms import VendaForm, item_vendaForm
# Create your views here.

def listar(request):
    Lista_vendas = Venda.objects.all()
    Lista_item_vendas = item_venda.objects.all()
    contexto = {
        'venda': Lista_vendas,
        'item_venda': Lista_item_vendas
    }
    return render(request, 'venda/listaVenda.html', context=contexto)

def cadastro(request):
    cadastra_produtos = Produtos.objects.all()
    cadastra_clientes = Clientes.objects.all()
    contexto = {
        'produtos': cadastra_produtos,
        'clientes': cadastra_clientes,
    }
    return render(request, 'venda/registroVendaCliente.html', context=contexto)

def cadastrar(request):
    if request.method == 'POST':
        # Create Venda first
        venda_form = VendaForm(request.POST)
        item_form = item_vendaForm(request.POST)
        
        if venda_form.is_valid() and item_form.is_valid():
            try:
                # Save Venda
                venda = Venda(
                    dataVenda=venda_form.cleaned_data['dataVenda'],
                    valorVenda=venda_form.cleaned_data['valorVenda'],
                    clienteCpf=venda_form.cleaned_data['clienteCpf'],
                )
                venda.save()
                
                # Save item_venda with the created Venda
                item_venda.objects.create(
                    vendaNumero=venda,
                    produtoCodigo=item_form.cleaned_data['produtoCodigo'],
                    quantidade=item_form.cleaned_data['quantidade'],
                    precoVenda=item_form.cleaned_data['precoVenda'],
                )
                
                return redirect('venda:sucesso')
                
            except Exception as e:
                # Handle any errors during save
                return render(request, 'venda/registroVendaCliente.html', {
                    'error': str(e),
                    'produtos': Produtos.objects.all(),
                    'clientes': Clientes.objects.all()
                })
    
    # If GET or invalid form
    return render(request, 'venda/registroVendaCliente.html', {
        'produtos': Produtos.objects.all(),
        'clientes': Clientes.objects.all()
    })