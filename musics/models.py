from django.db import models

class MusicCategory(models.Model):
    name = models.CharField(max_length=255)

class Music(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    record_label = models.CharField(max_length=255)
    release_date = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    num_tracks = models.IntegerField()
    format = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    categories = models.ManyToManyField(MusicCategory)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title
