from django.db import models
from django.contrib.auth.models import User
from espelho.models import Produto

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    altura = models.DecimalField(max_digits=5, decimal_places=2)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    sexo = models.CharField(max_length=20, choices=[
        ('masculino', 'Masculino'),
        ('feminino', 'Feminino'),
        ('outro', 'Prefiro não declarar'),
    ])

class Experimentacao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='experimentacoes_usuario')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='experimentacoes_usuario')
    data_hora = models.DateTimeField(auto_now_add=True)

class Reserva(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    data_reserva = models.DateTimeField(auto_now_add=True)
