from typing import Text
from django import forms
from django.forms import widgets
from .models import Arte


class FormPublicar(forms.ModelForm):
    class Meta:
        model = Arte
        fields = ('nome', 'descricao', 'formato',
                  'tematica', 'categoria', 'preco', 'foto')

        widgets = {
            'nome': forms.TextInput(attrs={"type": "text", "placeholder": "Nome"}),
            'descricao': forms.Textarea(attrs={"type": "textarea", "placeholder": "Descrição"}),
            'preco': forms.NumberInput(attrs={"type": "text", "placeholder": "Valor"}),
            'foto': forms.ClearableFileInput(attrs={"type": "file", "placeholder": "Upload"}),
            'formato': forms.Select(attrs={"type": "select", "placeholder": "formato"}),
            'tematica': forms.Select(attrs={"type": "select", "placeholder": "Tematica"}),
            'categoria': forms.Select(attrs={"type": "select", "placeholder": "Categoria"}),
        }
