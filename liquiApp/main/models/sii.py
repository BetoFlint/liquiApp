from django.db import models

class ImpuestoSegCategoria(models.Model):
    periodo=models.CharField(max_length = 10)
    tipoperiodo = models.CharField(max_length = 10)
    desde = models.IntegerField()
    hasta = models.IntegerField()
    factor = models.CharField(max_length = 10)
    rebaja = models.IntegerField()
    tasa = models.CharField(max_length = 20)

    def __str__(self):
        return f"{self.periodo} - Desde: {self.desde}, Hasta: {self.hasta}"

def obtener_impuesto_por_monto_y_periodo(monto, periodo):
    try:
        impuesto = ImpuestoSegCategoria.objects.get(desde__lte=monto, hasta__gte=monto, periodo=periodo)
        return impuesto
    except ImpuestoSegCategoria.DoesNotExist:
        return None
    