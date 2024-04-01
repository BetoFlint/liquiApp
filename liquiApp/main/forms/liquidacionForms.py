# forms.py
from django import forms

class liquidacionForm (forms.Form):
    sueldo_base = forms.DecimalField(max_digits=10, decimal_places=2)
    otros_ingresos = forms.DecimalField(max_digits=10, decimal_places=2)
    asignaciones = forms.DecimalField(max_digits=10, decimal_places=2)
    descuentos = forms.DecimalField(max_digits=10, decimal_places=2)
    costo_plan_isapre = forms.DecimalField(max_digits=10, decimal_places=2)