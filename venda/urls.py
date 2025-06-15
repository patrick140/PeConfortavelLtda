from django.urls import path

from . import views

app_name = "venda"

urlpatterns = [
    path('lista', views.listar, name='listar'),
    path('cadastra', views.cadastrar, name='cadastrar'),
]