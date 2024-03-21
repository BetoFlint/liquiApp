import requests
import logging

def creaLogger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)  # Puedes ajustar el nivel según necesites
    handler = logging.StreamHandler()  # Envía los registros a stderr
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def apiObtenerParidad(paridad, fecha):
    url = f'https://mindicador.cl/api/{paridad}/{fecha}'
    response = requests.get(url)
    #logger.info("Valor de responde " + str(response))
    if response.status_code == 200:
        # Procesar los datos recibidos
        dataJson = response.json()
        data = dataJson['nombre']
        valor= dataJson['serie'][0]['valor']
    else: 
        data = False
        valor = False
    return data, valor