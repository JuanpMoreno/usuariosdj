from django.db import models

#Modulo para trabajar con sesion de usuarios
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

#Importando managers
from .managers import UserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):

    class Meta:

        app_label = 'users'

    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otros')
    )

    username = models.CharField(max_length=10, unique=True)
    email = models.EmailField()
    nombres = models.CharField(max_length=30, blank=True)
    apellidos = models.CharField(max_length=30, blank=True)
    genero = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    #Codigo de registro a la app
    codregistro = models.CharField(max_length=6, blank=True)
    #
    is_staff = models.BooleanField(default=False)
    #El usuario esta activo si el email es correcto
    is_active = models.BooleanField(default=False)

    #Atributo para hacer login desde el administrador
    USERNAME_FIELD = 'username'

    #Campos requeridos para la creacion del superusuario
    REQUIRED_FIELDS = ['email',]

    objects = UserManager()

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.nombres  + ' ' + self.apellidos
