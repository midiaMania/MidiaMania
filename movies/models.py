from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    synopsis = models.TextField()
    categories = models.ManyToManyField(Category)
    directors = models.CharField(max_length=255)
    release_date = models.DateField()
    running_time = models.IntegerField()  # Em minutos
    rating = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    img = models.ImageField(upload_to='frontend/static/images/movies/')
    copias = models.IntegerField()
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.title

#TODO: VERIFCAR SE HAVERA UM NUMERO FICTICIO DE COPIAS, SE SERÁ REALMENTE UM LINK PARA IMAGEM

