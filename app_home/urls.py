from django.contrib import admin
from django.urls import path
from app_home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pizza/', views.criar_pizza, name='pizza'),
    path('listar/', views.listar_pizzas, name='listar_pizzas'),
    path('delete/<int:id>/', views.deletar_pizza, name='deletar_pizza'),
    path('update/<int:id>/', views.editar_pizza, name='editar_pizza'),
    path('carrinho/<int:id>/', views.carrinho_pizzas, name='carrinho_pizzas'),
    path('carrinho/', views.carrinho_comprar, name='carrinho_comprar'),
    path('limpar_carrinho/', views.limpar_carrinho, name='limpar_carrinho'),
    path('deletar_pizza_carrinho/<int:id>/', views.deletar_pizza_carrinho, name='deletar_pizza_carrinho'),
]
