from django.test import SimpleTestCase
from main.functions import apiObtenerParidad

# Create your tests here.
class apiObtenerParidad_uf(SimpleTestCase):
    def test_apiObtenerParidad(self):
        resultado = apiObtenerParidad('uf', '13-03-2024')
        self.assertEqual(resultado, ('Unidad de fomento (UF)',36964.9))

class apiObtenerParidad_dolar(SimpleTestCase):
    def test_apiObtenerParidad(self):
        resultado = apiObtenerParidad('dolar', '13-03-2024')
        self.assertEqual(resultado, ('Dólar observado',965.18))
