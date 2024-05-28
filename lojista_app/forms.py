from django import forms
from .models import Produto, Variante, Foto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control ckeditor'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'estacao': forms.Select(attrs={'class': 'form-control'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'preco_comparacao': forms.NumberInput(attrs={'class': 'form-control'}),
            'preco_venda': forms.NumberInput(attrs={'class': 'form-control'}),
            'localizacao': forms.TextInput(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
            'continuar_vendendo_sem_estoque': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class VarianteForm(forms.ModelForm):
    class Meta:
        model = Variante
        fields = '__all__'

class FotoForm(forms.ModelForm):
    class Meta:
        model = Foto
        fields = '__all__'
