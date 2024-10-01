# blog/forms.py

from django import forms
from .models import Article
from .models import Category

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'image', 'category']  # Champs du formulaire


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']  # Ajoutez les champs que vous voulez
