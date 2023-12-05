from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    cpf = models.CharField(max_length=14)  # Adicionei o campo CPF
    city = models.CharField(max_length=255)
    neighborhood = models.CharField(max_length=255)
    number = models.CharField(max_length=10)
    street = models.CharField(max_length=255)
    cep = models.CharField(max_length=10)
    complement = models.CharField(max_length=255)

