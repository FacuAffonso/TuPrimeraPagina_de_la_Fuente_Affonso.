from django.db import models

class Author(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    def __str__(self): return self.nombre

class Category(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self): return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.ForeignKey(Author, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    publicado = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.titulo
