from django import forms
from .models import Produto, ProdutoFilho, Foto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'

class ProdutoFilhoForm(forms.ModelForm):
    class Meta:
        model = ProdutoFilho
        fields = '__all__'

class FotoForm(forms.ModelForm):
    class Meta:
        model = Foto
        fields = '__all__'
