# blog/urls.py

from django.urls import path
from .views import (
    home,
    article_list,
    article_detail,
    publish_article,
    edit_article,
    delete_article,
    category_list,
    category_create,
    category_edit,
    category_delete,
)

urlpatterns = [
    path('', home, name='home'),  # Page d'accueil
    path('articles/', article_list, name='article_list'),  # Liste des articles
    path('articles/<int:pk>/', article_detail, name='article_detail'),  # Détails de l'article
    path('publish/', publish_article, name='publish_article'),  # Publier un article
    path('edit/<int:pk>/', edit_article, name='edit_article'),  # Modifier un article
    path('delete/<int:pk>/', delete_article, name='delete_article'),  # Supprimer un article
    path('categories/', category_list, name='category_list'),  # Liste des catégories
    path('categories/create/', category_create, name='category_create'),  # Créer une catégorie
    path('categories/<int:pk>/edit/', category_edit, name='category_edit'),  # Modifier une catégorie
    path('categories/<int:pk>/delete/', category_delete, name='category_delete'),  # Supprimer une catégorie
]
