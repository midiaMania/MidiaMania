from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome')
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255, verbose_name='Título')
    synopsis = models.TextField(verbose_name='Sinopse')
    categories = models.ManyToManyField(Category, verbose_name='Categorias')
    directors = models.CharField(max_length=255, verbose_name='Diretores')
    release_date = models.DateField(verbose_name='Data de lançamento')
    running_time = models.IntegerField(verbose_name='Duração')  # Em minutos
    rating = models.IntegerField(verbose_name='Classificação')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Preço')
    img = models.ImageField(upload_to='frontend/static/upload/movies/', verbose_name='Imagem')
    copias = models.IntegerField(verbose_name='Cópias')
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.title

#TODO: VERIFCAR SE HAVERA UM NUMERO FICTICIO DE COPIAS, SE SERÁ REALMENTE UM LINK PARA IMAGEM

