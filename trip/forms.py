from django import forms
from .models import *

class CadastroPostagem(forms.ModelForm):
    class Meta:
        model = Postagem
        fields = [
            'data_hora',
            'conteudo',
            'categoria',
            'descricao',
            'titulo',
            'imagem',
            'autor',
        ]
