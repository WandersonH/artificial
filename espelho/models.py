# Criando banco de dados

from django.db import models
from django.contrib.auth.models import User


class Produto(models.Model):
 # ... (código dos campos do modelo Produto)
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='produtos/')
    valor = models.DecimalField(max_digits=10, decimal_places=2)  # Exibido na página de reserva
    cores_disponiveis = models.CharField(max_length=255)
    categoria = models.CharField(max_length=100)
    quantidade_usos = models.PositiveIntegerField(default=0)
    data_criacao = models.DateTimeField(auto_now_add=True)
    estacao = models.CharField(max_length=20, choices=[
        ('primavera', 'Primavera'),
        ('verao', 'Verão'),
        ('outono', 'Outono'),
        ('inverno', 'Inverno'),
    ])

class Usuario(models.Model): 
# ... (código dos campos do modelo Produto)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    altura = models.DecimalField(max_digits=5, decimal_places=2)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    sexo = models.CharField(max_length=20, choices=[
        ('masculino', 'Masculino'),
        ('feminino', 'Feminino'),
        ('outro', 'Prefiro não declarar'),
    ])

class Experimentacao(models.Model):
# ... (código dos campos do modelo Experimentacao)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    data_hora = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')  # Vincula o perfil ao usuário

    # Dados do cliente
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)  # Imagem de perfil (opcional)
    medidas = models.JSONField(null=True, blank=True)  # Altura, peso, etc. (opcional)
    preferencias_estilo = models.CharField(max_length=100, blank=True)  # Casual, formal, etc. (opcional)

    # Dados do lojista (opcional, use apenas se aplicável)
    nome_loja = models.CharField(max_length=255, blank=True)
    endereco = models.CharField(max_length=255, blank=True)
    horario_funcionamento = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"