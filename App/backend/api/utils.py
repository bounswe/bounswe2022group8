from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class ArtItemStorage(S3Boto3Storage):
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    location = 'artitem'

class ProfileImageStorage(S3Boto3Storage):
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    location = 'avatar'