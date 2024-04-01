from django import template
import re

register = template.Library()

@register.filter(name='format_number')
def format_number(value):
    # Primero, asegúrate de que el valor sea un float o decimal para mantener los decimales
    value = float(value)
    # Convierte el número a un string para poder manipularlo
    number_as_string = "{:,.0f}".format(value)
    # Reemplaza comas por puntos y puntos por comas
    formatted_number = number_as_string.replace(",", "X").replace(".", ",").replace("X", ".")
    return formatted_number

@register.filter(name='float_number')
def float_number(value):
    # Primero, asegúrate de que el valor sea un float o decimal para mantener los decimales
    value = float(value)
    # Convierte el número a un string para poder manipularlo
    number_as_string = "{:,.2f}".format(value)
    # Reemplaza comas por puntos y puntos por comas
    formatted_number = number_as_string.replace(",", "X").replace(".", ",").replace("X", ".")
    return formatted_number
