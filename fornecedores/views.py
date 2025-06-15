from django.shortcuts import render

# Create your views here.

def listar(request):
    return render(request, 'fornecedores/listarFornecedores.html')

def cadastrar(request):
    return render(request, 'fornecedores/cadastroFornecedores.html')