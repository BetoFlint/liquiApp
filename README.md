# liquidacion

<em> Repositorio de trabajo Magister UBO </em>


Etapa 1: Instalación de Software necesario

Debes contar con las siguientes aplicaciones de base para poder utilizar este ambiente:

-Docker Desktop

-Python

-Git

Instalación de docker:
Se debe instalar el aplicativo docker, lo puedes encontrar en la siguiente ruta:

https://www.docker.com/products/docker-desktop/

Posterior a la instalación debes crearte una cuenta.

Instalación de Git:
Se debe instalar Git a traves del siguiente link.
https://git-scm.com/downloads

Debes crear una cuenta.

![Prueba](https://miro.medium.com/v2/resize:fit:720/format:webp/1*ycIMlwgwicqlO6PcFRA-Iw.png)

Instalación de Python

https://www.python.org/downloads/

Recordar que al momento de instalar python, se debe escoger que se añadan las variables de entorno al sistema. De lo contrario deberán ser configuradas manualmente. Es probable que para que el sistema reconozca el comando python, se deba reiniciar el equipo posterior a la instalación.

Una vez reiniciado el sistema, se puede validar la correcta instalación de ambis sistemas mediante los siguientes comandos en la terminal.

Validación de python:

python --version
docker --version
git --version

Con esto cerramos la etapa de instalación de software necesarios.

Etapa 2: Clonación de proyecto Git

Crear una carpeta específica en donde trabajaremos el aplicativo web.
Acceder mediante terminal a esta ruta y ejecutar el siguiente comando para clonar y traer la última versión existente en GitHub.

git clone https://github.com/BetoFlint/liquiApp

Eso nos traerá todos los elementos y los almacenará en la carpeta seleccionada.

Etapa 3: Construcción del ambiente.

Para los siguientes pasos necesitamos que este corriendo el aplicativo docker desktop.

acceder a la ruta del proyecto en la carpeta que creamos anteriormente
Ingresar a liquiApp con cd liquiApp

Activar el entorno virtual existente:

.\venv\Scripts\Activate
source venv/Scripts/activate

Con este comando utilizamos la versión de los componentes que existen dentro de ese entorno virtual.

Ejecutar el Build
Debemos asegurarnos de encontrarnos en la misma ruta donde está el archivo Docker-Compose.yml

docker-compose build

docker-compose up -d

docker-compose run python manage.py migrate

docker-compose run python manage.py createsuperuser

Con esto ya podemos trabajar en nuestro aplicativo con visual studio y realizar modificaciones.

PUNTOS A INCORPORAR COMO SIGUIENTES PASOS NO ABORDADOS:

Implementación de Jenkins para pipeline de CI/CD
Pasos a producción
Ambiente de Certificación.
Seguimiento y monitoreo
Gestion de incidentes (Algun gestor de ticket o algo asi)
