from django.db import models

class Usuario (models.Model):
    username = models.CharField(max_length=60)
#    apellidoP = models.CharField(max_length=60)
#    apellidoM = models.CharField(max_length=60)
#    correo = models.CharField(max_length=60)
#    password = models.CharField(max_length=60)
    
class Gente(models.Model):
    nombrePersona = models.CharField(max_length = 20)