from .base import *

import environ

env = environ.Env()
environ.Env.read_env()

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

