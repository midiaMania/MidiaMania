from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome')
    def __str__(self):
        return self.name
    
class Music(models.Model):    
    title = models.CharField(max_length=255, verbose_name='Título')
    artist = models.CharField(max_length=255, verbose_name='Artista')
    record_label = models.CharField(max_length=255, verbose_name='Gravadora')
    release_date = models.DateField(verbose_name='Data de lançamento')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço')
    img = models.ImageField(upload_to='frontend/static/upload/musics/', verbose_name='Imagem')
    categories = models.ManyToManyField(Category, verbose_name='Categorias')
    slug = models.SlugField(unique=True)

    FORMAT_CHOICES = [
        ('CD', 'CD'),
        ('DVD', 'DVD'),
        ('Disco de Vinil', 'Disco de Vinil'),
        ('Blu-ray', 'Blu-ray'),
    ]

    format = models.CharField(max_length=14, choices=FORMAT_CHOICES, verbose_name='Formato')
    
    def __str__(self):
        return self.title

class Track(models.Model):
    title = models.CharField(max_length=100, verbose_name="Título da Faixa")
    duration = models.DurationField(verbose_name='Duração')
    album = models.ForeignKey(Music, on_delete=models.CASCADE)

    def __str__(self):
        return self.title