from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME':env("DB_NAME"),
    'USER':env("DB_USER"),
    'PASSWORD': env("DB_PASSWORD"),
    'HOST':env("DB_HOST"),
    'PORT':env("DB_PORT"),
    }
}

#Email Settings
EMAIL_HOST = 'localhost'
EMAIL_PORT = '1025'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
#EMAIL_USE_SSL = False
