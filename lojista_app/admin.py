from django.contrib import admin
from .models import Categoria, Produto, ImagemProduto, Variante, Foto, Profile

# Certifique-se de que o modelo Produto não está sendo registrado duas vezes
admin.site.register(Categoria)
# Remova a linha duplicada
# admin.site.register(Produto)  # Esta linha deve ser removida se já estiver registrada
admin.site.register(ImagemProduto)
admin.site.register(Variante)
admin.site.register(Foto)
admin.site.register(Profile)
