from django import forms
from .models import GanhoDiario, GastoCombustivel, AluguelSemanal, Meta

class GanhoDiarioForm(forms.ModelForm):
    class Meta:
        model = GanhoDiario
        fields = ['data', 'receita', 'ganho_por_km', 'lucro']

class GastoCombustivelForm(forms.ModelForm):
    class Meta:
        model = GastoCombustivel
        fields = ['data', 'valor', 'percurso']

class AluguelSemanalForm(forms.ModelForm):
    class Meta:
        model = AluguelSemanal
        fields = ['data_inicio', 'data_fim', 'valor']

class MetaForm(forms.ModelForm):
    class Meta:
        model = Meta
        fields = ['meta_receita', 'meta_ganho']