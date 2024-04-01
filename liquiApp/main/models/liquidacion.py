from django.db import models

class Ingresos (models.Model):
    nombreingreso = models.CharField(max_length=50)
    tipoingreso = models.CharField(max_length= 12)

class Descuentos (models.Model):
    nombredescuento = models.CharField(max_length=50)
    tipodescuento = models.CharField(max_length= 12)

