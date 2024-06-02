from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from .forms import ProdutoForm, VarianteForm, FotoForm, CategoriaForm
from .models import Produto, Variante, Foto

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
        variante_forms = [VarianteForm(request.POST, prefix=str(i)) for i in range(5)]
        foto_form = FotoForm(request.POST, request.FILES)

        if produto_form.is_valid() and all([vf.is_valid() for vf in variante_forms]) and foto_form.is_valid():
            produto = produto_form.save()
            for vf in variante_forms:
                variante = vf.save(commit=False)
                variante.produto = produto
                variante.save()
            fotos = request.FILES.getlist('imagem')
            for foto in fotos:
                Foto.objects.create(produto=produto, imagem=foto)
            return redirect('sucesso')
    else:
        produto_form = ProdutoForm()
        variante_forms = [VarianteForm(prefix=str(i)) for i in range(5)]
        foto_form = FotoForm()

    return render(request, 'lojista_app/criar_produto.html', {
        'produto_form': produto_form,
        'variante_forms': variante_forms,
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

def cadastrar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cadastrar_produto')  # Redirecionar para a página de cadastro de produto
    else:
        form = CategoriaForm()
    return render(request, 'lojista_app/cadastrar_categoria.html', {'form': form})
