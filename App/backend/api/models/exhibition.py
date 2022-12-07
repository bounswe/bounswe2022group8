from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from .user import User
from ..models.artitem import ArtItem


class Exhibition(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    collaborators = models.ManyToManyField(User)
    poster = models.OneToOneRel(ArtItem, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    class Meta:
        ordering = ["-created_at"]  # order according to the timestamps

    def __str__(self):
        return "Exhibition: " + self.title

class VirtualExhibition(Exhibition):
    pass

class OnlineExhibition(Exhibition):
    pass
