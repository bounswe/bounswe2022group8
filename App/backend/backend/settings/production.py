from .base import *

DEBUG = True  # Set this to False in the future and fill in the allowed_hosts section.
ALLOWED_HOSTS = ['34.125.134.88']

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

#Email Settings 
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = 587
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
#EMAIL_USE_SSL = True

