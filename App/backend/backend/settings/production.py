from .base import *

DEBUG = True  # Set this to False in the future and fill in the allowed_hosts section.
ALLOWED_HOSTS = ['34.125.134.88', 'localhost', '127.0.0.1']

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

AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
AWS_QUERYSTRING_AUTH = False # might change in the future

# s3 public media settings
PUBLIC_MEDIA_LOCATION = 'media'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'