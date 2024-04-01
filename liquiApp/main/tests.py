from django.test import SimpleTestCase, TestCase
from main.functions import apiObtenerParidad, enviar_correo
from main.models.sii import obtener_impuesto_por_monto_y_periodo

# Create your tests here.
class apiObtenerParidad_uf(SimpleTestCase):
    def test_apiObtenerParidad(self):
        resultado = apiObtenerParidad('uf', '13-03-2024')
        self.assertEqual(resultado, ('Unidad de fomento (UF)',36964.9))

class apiObtenerParidad_dolar(SimpleTestCase):
    def test_apiObtenerParidad(self):
        resultado = apiObtenerParidad('dolar', '13-03-2024')
        self.assertEqual(resultado, ('Dólar observado',965.18))

class enviarCorreo_test (SimpleTestCase):
    def test_enviarCorreo(self):
        resultado = enviar_correo('jalbornozr2@gmail.com', 'test', 'test', )
        self.assertEqual(resultado, 1)

class obtener_impuesto_por_monto_y_periodo_test (TestCase):
    def test_impSegCat(self):
        resultado = obtener_impuesto_por_monto_y_periodo(100000, '202312')
        self.assertEqual(resultado, 1)