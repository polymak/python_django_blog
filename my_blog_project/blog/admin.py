# blog/admin.py

from django.contrib import admin
from .models import Article, Category

admin.site.register(Category)  # Enregistrer le modèle Category
admin.site.register(Article)    # Enregistrer le modèle Article
