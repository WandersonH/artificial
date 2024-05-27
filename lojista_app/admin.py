from django.contrib import admin
from .models import Profile, Produto, ProdutoFilho, Foto

# Registre os modelos no admin
admin.site.register(Profile)
admin.site.register(Produto)
admin.site.register(ProdutoFilho)
admin.site.register(Foto)