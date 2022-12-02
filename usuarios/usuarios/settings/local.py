from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret('DB_NAME'),
        'USER' : get_secret('USER'),
        'PASSWORD' : get_secret('PASSWORD'),
        'HOST' : 'localhost',
        'PORT' : '5432',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = [BASE_DIR / 'media']


#Configuracion de email para envio de mensajes, codigo de verificacion, etc
#EMAIL SETTINGS
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'juan@mail.com'
EMAIL_HOST_PASSWORD = 'unacontraseñacualquiera'
EMAIL_PORT = 587