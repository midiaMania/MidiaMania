from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
class Game(models.Model):
    title = models.CharField(max_length=255, verbose_name='Título')
    about = models.TextField(verbose_name='Sobre o Jogo')
    
    PLATFORM_CHOICES = [
        ('PC', 'PC'),
        ('Playstation 1', 'Playstation 1'),
        ('Playstation 2', 'Playstation 2'),
        ('Playstation 3', 'Playstation 3'),
        ('Playstation 4', 'Playstation 4'),
        ('Playstation 5', 'Playstation 5'),
        ('Xbox 360', 'Xbox 360'),
        ('Xbox One', 'Xbox One'),
        ('Mega Drive', 'Mega Drive'),
        ('Super Nintendo', 'Super Nintendo'),
        ('Nintendo 64', 'Nintendo 64'),
        ('Game Boy Color', 'Game Boy Color'),
        ('Game Boy Advance', 'Game Boy Advance'),
        ('Nintendo Wii', 'Nintendo Wii'),
        ('Nintendo DS', 'Nintendo DS'),
        ('Nintendo Switch', 'Nintendo Switch')
    ]

    platform = models.CharField(max_length=16, choices=PLATFORM_CHOICES, verbose_name='Plataforma')
    
    developer = models.CharField(max_length=255, verbose_name='Desenvolvedor')
    publisher = models.CharField(max_length=255, verbose_name='Distribuidor')
    release_date = models.DateField(verbose_name='Data de lançamento')
    rating = models.IntegerField(verbose_name='Classificação')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço')
    img = models.ImageField(upload_to='frontend/static/upload/games/', verbose_name='Imagem')
    categories = models.ManyToManyField(Category, verbose_name='Categorias')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title
