from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario (AbstractUser):
    rut = models.CharField(max_length = 10)
    nombre = models.CharField(max_length = 50)
    apellidopat = models.CharField(max_length = 50)
    apellidomat = models.CharField(max_length = 50)
    tipousuario = models.CharField(max_length = 10)

