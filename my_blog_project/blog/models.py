# blog/models.py

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)  # Nom de la catégorie

    def __str__(self):
        return self.name  # Afficher le nom de la catégorie dans l'admin

class Article(models.Model):
    title = models.CharField(max_length=200)  # Titre de l'article
    content = models.TextField()  # Contenu de l'article
    image = models.ImageField(upload_to='images/', null=True, blank=True)  # Image de l'article
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Lien avec la catégorie
    created_at = models.DateTimeField(auto_now_add=True)  # Date de création

    def __str__(self):
        return self.title  # Afficher le titre de l'article dans l'admin
