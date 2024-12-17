# core/forms.py
from django import forms
from .models import Filme

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ['titulo', 'sinopse', 'data_lancamento', 'duracao', 'genero', 'diretor', 'url_trailer', 'poster']