from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from .forms import ProdutoForm, ProdutoFilhoForm, FotoForm
from .models import Produto, ProdutoFilho, Foto

def home(request):
    return render(request, 'lojista_app/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'lojista_app/register.html', {'form': form})

def dashboard(request):
    return render(request, 'lojista_app/dashboard.html')

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'lojista_app/listar_produtos.html', {'produtos': produtos})

def reservas(request):
    return render(request, 'lojista_app/reservas.html')

def perfil(request):
    return render(request, 'lojista_app/perfil.html')

def criar_produto(request):
    if request.method == "POST":
        produto_form = ProdutoForm(request.POST, request.FILES)
        produto_filho_form = ProdutoFilhoForm(request.POST)
        foto_form = FotoForm(request.POST, request.FILES)
        
        if produto_form.is_valid() and produto_filho_form.is_valid() and foto_form.is_valid():
            produto = produto_form.save()
            produto_filho = produto_filho_form.save(commit=False)
            produto_filho.produto = produto
            produto_filho.save()
            foto = foto_form.save(commit=False)
            foto.produto = produto
            foto.save()
            return redirect('sucesso')
    else:
        produto_form = ProdutoForm()
        produto_filho_form = ProdutoFilhoForm()
        foto_form = FotoForm()

    return render(request, 'lojista_app/criar_produto.html', {
        'produto_form': produto_form,
        'produto_filho_form': produto_filho_form,
        'foto_form': foto_form,
    })


def atualizar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form_produto = ProdutoForm(request.POST, request.FILES, instance=produto)
        form_fotos = FotoForm(request.POST, request.FILES)
        if form_produto.is_valid() and form_fotos.is_valid():
            produto = form_produto.save()
            produto.fotos.all().delete()
            for f in request.FILES.getlist('fotos'):
                Foto.objects.create(produto=produto, imagem=f)
            return redirect('listar_produtos')
    else:
        form_produto = ProdutoForm(instance=produto)
        form_fotos = FotoForm()
    return render(request, 'lojista_app/atualizar_produto.html', {'form_produto': form_produto, 'form_fotos': form_fotos})

def deletar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete()
        return redirect('listar_produtos')
    return render(request, 'lojista_app/deletar_produto.html', {'produto': produto})
