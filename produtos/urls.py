from django.urls import path

from . import views

app_name = "produtos"

urlpatterns = [
    path('lista/', views.listar, name='listar'),
    path('cadastra/', views.cadastrar, name='cadastrar'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('excluir/<int:codigo>', views.excluir, name='excluir_produtos'),
    path('carregar_produtos/<int:codigo>', views.carregar_produtos, name='carregar_produtos'),
    path('atualizar_produtos/', views.atualizar, name='atualizar_produtos'),    
]