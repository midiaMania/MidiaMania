from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=255)
    platform = models.CharField(max_length=255)
    developer = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    release_date = models.DateField()
    rating = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='frontend/static/images/games/')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title
