from django.db import models
from django.contrib.auth.models import User

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=100)
    quantidade_usos = models.PositiveIntegerField(default=0)
    data_criacao = models.DateTimeField(auto_now_add=True)
    estacao = models.CharField(max_length=20, choices=[
        ('primavera', 'Primavera'),
        ('verao', 'Verão'),
        ('outono', 'Outono'),
        ('inverno', 'Inverno'),
    ])
    estoque = models.IntegerField()

    def __str__(self):
        return self.nome

class ProdutoFilho(models.Model):
    produto_principal = models.ForeignKey(Produto, related_name='cores', on_delete=models.CASCADE)
    cor = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='fotos_produtos/')

    def __str__(self):
        return f"{self.produto_principal.nome} - {self.cor}"

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
    horario_funcionamento = models.CharField(max_length=255, blank=True)  # Corrigido de maxlength para max_length

    def __str__(self):
        return f"Perfil de {self.user.username}"
