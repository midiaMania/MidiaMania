from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
class Music(models.Model):
    name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='frontend/static/images/musics/')
    categories = models.ManyToManyField(Category)
    slug = models.SlugField(unique=True)


    def __str__(self):
        return self.name
