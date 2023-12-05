import os
from django.db import models
from django.contrib.auth.models import User

def get_image_upload_path(instance, filename):
    # Obtém a extensão do arquivo
    ext = filename.split('.')[-1]
    # Monta o caminho do arquivo com base no tipo e nome do produto
    path = os.path.join('frontend', 'static', 'images', instance.product_type, f"{instance.product_name}.{ext}")
    return path

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    cpf = models.CharField(max_length=14)
    city = models.CharField(max_length=255)
    neighborhood = models.CharField(max_length=255)
    number = models.CharField(max_length=10)
    street = models.CharField(max_length=255)
    cep = models.CharField(max_length=10)
    complement = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.username}'s Profile"

class ShoppingCartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_type = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_image = models.ImageField(upload_to=get_image_upload_path)
    purchase_date = models.DateField()

    def __str__(self):
        return f"{self.product_name} - {self.user.username}"

class PurchasedItem(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product_type = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=5, decimal_places=2)
    product_image = models.ImageField(upload_to=get_image_upload_path)
    date = models.DateField()

    def __str__(self):
        return f"{self.product_name} - {self.user_profile.user.username}"
