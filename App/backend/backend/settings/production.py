from .base import *

DEBUG = True  # Set this to False in the future and fill in the allowed_hosts section.
ALLOWED_HOSTS = []

DATABASES = {
'default': {
   'ENGINE': 'django.db.backends.postgresql',
    'NAME':"postgres",
    'USER':"postgres",
    'PASSWORD':"postgres",
    'HOST':"db",
    'PORT':5432
    }
}