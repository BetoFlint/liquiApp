from django.contrib.auth.management.commands import createsuperuser
from django.core.management.base import CommandError
from django.db import transaction
from django.contrib.auth import get_user_model

class Command(createsuperuser.Command):
    help = 'Commando personalizado para crear un superusuario con campos adicionales.'

    def add_arguments(self, parser):
        super().add_arguments(parser)
        #parser.add_argument('--username', type=str, help='Nombre de usuario')
        #parser.add_argument('--email', type=str, help='Correo electrónico')
        #parser.add_argument('--password', type=str, help='Contraseña')
        # Argumentos para campos adicionales como opciones, pero no son requeridos para el comando
        parser.add_argument('--rut', type=str, default=None)
        parser.add_argument('--nombre', type=str, default=None)
        parser.add_argument('--apellidopat', type=str, default=None)
        parser.add_argument('--apellidomat', type=str, default=None)
        parser.add_argument('--tipousuario', type=str, default=None)

    def handle(self, *args, **options):
        # Usar una transacción atómica para asegurarse de que los cambios se reviertan en caso de error
        UserModel = get_user_model()
        
        username = 'Administrador'
        email = 'jalbornozr2@gmail.com'
        password = '12345'

        if not username or not email or not password:
            raise CommandError('Los campos "username", "email" y "password" son requeridos.')


        # Solicitar interactivamente los campos adicionales si no se proporcionaron como argumentos
        campos_adicionales = {
            'rut': 'RUT',
            'nombre': 'Nombre',
            'apellidopat': 'Apellido Paterno',
            'apellidomat': 'Apellido Materno',
            'tipousuario': 'Tipo de usuario ',
        }
        

        
        usuario = UserModel.objects.create_superuser(username=username,
                                                      email=email,
                                                      password=password)
       
        
        #if created:
            # Asignar campos adicionales aquí si el usuario fue creado
        for campo, desc in campos_adicionales.items():
            if options[campo] is None:
                valor = input(f'Introduce el valor para {desc}: ')
                options[campo] = valor 

        usuario.rut = options['rut']
        usuario.nombre = options['nombre']
        usuario.apellidopat = options['apellidopat']
        usuario.apellidomat = options['apellidomat']
        usuario.tipousuario = options['tipousuario']
        #usuario.set_password(options['password'])  # Importante para asegurar que la contraseña se hashea
        # Asignar otros campos adicionales como se hacía previamente
        usuario.save()

