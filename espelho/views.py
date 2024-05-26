from django.shortcuts import render
from .models import Produto

# Exemplo de view para a home page
def home(request):
    return render(request, 'espelho/home.html')

# Exemplo de view para listar produtos
def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'espelho/listar_produtos.html', {'produtos': produtos})
