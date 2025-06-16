from django.urls import path

from . import views

app_name = "clientes"

urlpatterns = [
    path('lista/', views.listar, name='listar'),
    path('cadastra/', views.cadastrar, name='cadastrar'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('excluir/<str:cpf>', views.excluir, name='excluir_clientes'),
    path('carregar_clientes/<str:cpf>', views.carregar_clientes, name='carregar_clientes'),
    path('atualizar_clientes/', views.atualizar, name='atualizar_clientes'),
]
