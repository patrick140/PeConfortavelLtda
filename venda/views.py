from django.shortcuts import render

# Create your views here.

def listar(request):
    return render(request, 'venda/listaVenda.html')

def cadastrar(request):
    return render(request, 'venda/registroVendaCliente.html')