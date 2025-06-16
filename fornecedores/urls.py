from django.urls import path

from . import views

app_name = "fornecedores"

urlpatterns = [
    path('lista', views.listar, name='listar'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('cadastra', views.cadastrar, name='cadastrar'),
    path('excluir/<int:codigo>', views.excluir, name='excluir_fornecedores'),
    path('carregar_fornecedores/<int:codigo>', views.carregar_fornecedores, name='carregar_fornecedores'),
    path('atualizar_fornecedores/', views.atualizar, name='atualizar_fornecedores'),
]