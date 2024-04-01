import requests
import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

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

def enviar_correo(destinatario, asunto, mensaje, archivo_adjunto=None):
    # Configura tus credenciales y servidor SMTP
    #remitente = 'slsmagubo@gmail.com'
    #password = 'slsmagubo123$'
    remitente = 'jalbornozr2@gmail.com'
    password = 'yvee xkkk nbkv xzrz'
    
    servidor_smtp = 'smtp.gmail.com'
    puerto_smtp = 587
    
    # Crea el objeto del mensaje
    msg = MIMEMultipart()
    msg['From'] = remitente
    msg['To'] = destinatario
    msg['Subject'] = asunto
    
    # Adjunta el mensaje al correo
    msg.attach(MIMEText(mensaje, 'plain'))
    
    # Procesa el archivo adjunto si se proporciona
    if archivo_adjunto:
        with open(archivo_adjunto, 'rb') as archivo:
            parte = MIMEBase('application', 'octet-stream')
            parte.set_payload((archivo).read())
            encoders.encode_base64(parte)
            parte.add_header('Content-Disposition', f"attachment; filename= {archivo_adjunto}")
            msg.attach(parte)
    
    # Inicia la sesión SMTP y envía el correo
    server = smtplib.SMTP(servidor_smtp, puerto_smtp)
    server.starttls()
    server.login(remitente, password)
    texto = msg.as_string()
    server.sendmail(remitente, destinatario, texto)
    server.quit()

    return 1