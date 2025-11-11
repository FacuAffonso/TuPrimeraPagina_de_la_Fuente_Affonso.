from django import forms
from .models import Author, Category, Post

class AuthorForm(forms.ModelForm):
    class Meta: model = Author; fields = ['nombre', 'email']

class CategoryForm(forms.ModelForm):
    class Meta: model = Category; fields = ['nombre']

class PostForm(forms.ModelForm):
    class Meta: model = Post; fields = ['titulo', 'contenido', 'autor', 'categoria']

class SearchForm(forms.Form):
    q = forms.CharField(label='Buscar', max_length=200, required=False)
