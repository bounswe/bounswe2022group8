from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from .user import User
from ..models.artitem import ArtItem

class AbstractExhibition(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    poster = models.OneToOneField(ArtItem, on_delete=models.CASCADE)  # a poster must be unique to an exhibition and each exhibition must have one
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    class Meta:
        ordering = ["-created_at"]  # order according to the timestamp
        abstract = True

    def __str__(self):
        return "Exhibition: " + self.title

class VirtualExhibition(AbstractExhibition):
    artitems_gallery = models.ManyToManyField(ArtItem, related_name="gallery", blank=True)  # select an art item from gallery - nothing happens to art item if the exhibition is deleted 
    collaborators = models.ManyToManyField(User, related_name="virtualCollaborators", blank=True)     # it's not compulsory to have collaborators

    @property
    def get_uploaded_artitems(self):
        return ExhibitionArtItem.objects.filter(virtualExhibition=self)

class ExhibitionArtItem(ArtItem):
    virtualExhibition =  models.ForeignKey(VirtualExhibition, on_delete=models.CASCADE)  # upladed for the exhibition and will be gone if the exhibition is deleted

class OfflineExhibition(AbstractExhibition):
    city = models.CharField(max_length=200,blank=True, null=True)
    country = models.CharField(max_length=200,blank=True, null=True)
    address = models.CharField(max_length=200,blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    collaborators = models.ManyToManyField(User, related_name="offlineCollaborators", blank=True)      # it's not compulsory to have collaborators
