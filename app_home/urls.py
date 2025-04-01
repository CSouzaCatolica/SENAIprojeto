
from django.contrib import admin
from django.urls import path
from app_home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pizza/', views.criar_pizza, name='pizza'),
    path('listar/', views.listar_pizzas, name='listar_pizzas'),
    path('delete/<int:id>/', views.deletar_pizza, name='deletar_pizza'),
    path('update/<int:id>/', views.editar_pizza, name='editar_pizza'),
]
