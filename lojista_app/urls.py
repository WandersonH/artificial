from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('produtos/', views.listar_produtos, name='listar_produtos'),
    path('reservas/', views.reservas, name='reservas'),
    path('perfil/', views.perfil, name='perfil'),
    path('produtos/criar/', views.criar_produto, name='criar_produto'),
    path('atualizar/<int:pk>/', views.atualizar_produto, name='atualizar_produto'),
    path('deletar/<int:pk>/', views.deletar_produto, name='deletar_produto'),
]
