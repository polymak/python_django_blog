from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Category
from .forms import ArticleForm, CategoryForm  # Assurez-vous d'avoir des formulaires pour Article et Category

def home(request):
    articles = Article.objects.order_by('-created_at')[:6]  # Obtenir les 6 derniers articles
    return render(request, 'blog/home.html', {'articles': articles})  # Afficher la page d'accueil

def article_list(request):
    articles = Article.objects.order_by('-created_at')  # Obtenir tous les articles en ordre décroissant
    return render(request, 'blog/article_list.html', {'articles': articles})  # Afficher la liste des articles

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)  # Obtenir l'article par son identifiant
    return render(request, 'blog/article_detail.html', {'article': article})  # Afficher les détails de l'article

def publish_article(request):
    categories = Category.objects.all()  # Récupérer toutes les catégories
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)  # Créer un formulaire avec les données soumises
        if form.is_valid():
            form.save()  # Sauvegarder l'article
            return redirect('home')  # Rediriger vers la page d'accueil
    else:
        form = ArticleForm()  # Créer un formulaire vide
    return render(request, 'blog/publish_article.html', {'form': form, 'categories': categories})  # Afficher le formulaire de publication


def edit_article(request, pk):
    article = get_object_or_404(Article, pk=pk)  # Obtenir l'article à modifier
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)  # Lier le formulaire à l'article
        if form.is_valid():
            form.save()  # Sauvegarder les modifications
            return redirect('article_detail', pk=article.pk)  # Rediriger vers les détails de l'article
    else:
        form = ArticleForm(instance=article)  # Créer un formulaire avec les données de l'article
    return render(request, 'blog/edit_article.html', {'form': form})  # Afficher le formulaire d'édition

def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk)  # Obtenir l'article à supprimer
    if request.method == 'POST':
        article.delete()  # Supprimer l'article
        return redirect('article_list')  # Rediriger vers la liste des articles
    return render(request, 'blog/delete_article.html', {'article': article})  # Confirmer la suppression

def category_list(request):
    categories = Category.objects.all()  # Obtenir toutes les catégories
    return render(request, 'blog/category_list.html', {'categories': categories})  # Afficher la liste des catégories

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)  # Créer un formulaire avec les données soumises
        if form.is_valid():
            form.save()  # Sauvegarder la catégorie
            return redirect('category_list')  # Redirige vers la liste des catégories
    else:
        form = CategoryForm()  # Créer un formulaire vide
    return render(request, 'blog/category_form.html', {'form': form})  # Afficher le formulaire de création de catégorie

def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)  # Obtenir la catégorie à modifier
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)  # Lier le formulaire à la catégorie
        if form.is_valid():
            form.save()  # Sauvegarder les modifications
            return redirect('category_list')  # Redirige vers la liste des catégories
    else:
        form = CategoryForm(instance=category)  # Créer un formulaire avec les données de la catégorie
    return render(request, 'blog/category_form.html', {'form': form})  # Afficher le formulaire d'édition de catégorie

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)  # Obtenir la catégorie à supprimer
    if request.method == 'POST':
        category.delete()  # Supprimer la catégorie
        return redirect('category_list')  # Redirige vers la liste des catégories
    return render(request, 'blog/category_confirm_delete.html', {'category': category})  # Confirmer la suppression de la catégorie
