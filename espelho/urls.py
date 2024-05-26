# espelho/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('produtos/', views.listar_produtos, name='listar_produtos'),
]
