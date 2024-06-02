from django.urls import path
from . import views

app_name = 'usuario_app'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('', views.home, name='home'),
    # Adicione outras URLs do app usuario aqui
]
