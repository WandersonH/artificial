from django.contrib import admin

# Register your models here.
from .models import Usuario, Produto, Profile

admin.site.register(Usuario)
admin.site.register(Produto)
admin.site.register(Profile)