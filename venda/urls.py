from django.urls import path

from . import views

app_name = "venda"

urlpatterns = [
    path('lista', views.listar, name='listar'),
    path('cadastrar', views.cadastrar, name='cadastrar'),
    path('cadastro', views.cadastro, name='cadastro'),
]