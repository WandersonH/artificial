from django.contrib import admin
from .models import Produto, LoginEspelho, Experimentacao as ExperimentacaoEspelho

admin.site.register(Produto)
admin.site.register(LoginEspelho)
admin.site.register(ExperimentacaoEspelho)
