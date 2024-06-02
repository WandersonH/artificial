from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Categoria(models.Model):
    nome = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='categorias/')

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = RichTextField()
    preco_comparacao = models.DecimalField(max_digits=10, decimal_places=2)
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estacao = models.CharField(max_length=20, choices=[
        ('primavera', 'Primavera'),
        ('verao', 'Verão'),
        ('outono', 'Outono'),
        ('inverno', 'Inverno'),
    ])
    genero = models.CharField(max_length=10, choices=[
        ('feminino', 'Feminino'),
        ('masculino', 'Masculino'),
        ('unisex', 'Unisex'),
    ])
    localizacao = models.CharField(max_length=255)
    quantidade = models.IntegerField()
    continuar_vendendo_sem_estoque = models.BooleanField(default=False)
    quantidade_usos = models.PositiveIntegerField(default=0)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class ImagemProduto(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='produtos/')

class Variante(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    valor = models.CharField(max_length=100)
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()
    sku = models.CharField(max_length=100, blank=True, null=True)
    barcode = models.CharField(max_length=100, blank=True, null=True)
    harmonized_system_code = models.CharField(max_length=100, blank=True, null=True)

class Foto(models.Model):
    produto = models.ForeignKey(Produto, related_name='fotos', on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='fotos_produtos/')

    def __str__(self):
        return f"Foto de {self.produto.nome}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    medidas = models.JSONField(null=True, blank=True)
    preferencias_estilo = models.CharField(max_length=100, blank=True)
    nome_loja = models.CharField(max_length=255, blank=True)
    endereco = models.CharField(max_length=255, blank=True)
    horario_funcionamento = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"
