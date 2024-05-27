from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='produtos/')
    valor = models.DecimalField(max_digits=10, decimal_places=2)
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

class LoginEspelho(models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    data_login = models.DateTimeField(auto_now_add=True)

class Experimentacao(models.Model):
    usuario = models.ForeignKey('usuario_app.Usuario', on_delete=models.CASCADE, related_name='experimentacoes_espelho')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='experimentacoes_espelho')
    data_hora = models.DateTimeField(auto_now_add=True)
