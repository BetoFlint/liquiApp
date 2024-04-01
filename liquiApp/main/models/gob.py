from django.db import models

class SueldoMinimo(models.Model):
    periodo =  models.CharField(max_length = 10)
    sueldo = models.IntegerField()