from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from .user import User
from ..models.artitem import ArtItem
import datetime
from django.utils import timezone
from django.db.models import F, Q


class AbstractExhibition(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    poster = models.OneToOneField(ArtItem, on_delete=models.CASCADE)  # a poster must be unique to an exhibition and each exhibition must have one
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    number_of_views = models.IntegerField(default=0)
    popularity = models.FloatField(default=0)

    def increaseViews(self, *args, **kwargs):
        self.number_of_views += 1
        super().save(*args, **kwargs)

    def updatePopularity(self, *args, **kwargs):
        self.popularity = 0.05*((self.created_at.year - 2020)*365 + self.created_at.month*30 + self.created_at.day) + self.number_of_views
        print(self.popularity)
        super().save(*args, **kwargs)


    class Meta:
        ordering = ["-popularity"]  # order according to popularity

    class Meta:
        ordering = ["-created_at"]  # order according to the timestamp
        abstract = True

    @property
    def get_status(self):
        currentTime = timezone.now()
        if(self.start_date > currentTime): return "Not Started Yet"
        elif(self.end_date < currentTime): return "Finished"
        else: return "Ongoing"

    def __str__(self):
        return "Exhibition: " + self.title

class VirtualExhibition(AbstractExhibition):
    artitems_gallery = models.ManyToManyField(ArtItem, related_name="gallery", blank=True)  # select an art item from gallery - nothing happens to art item if the exhibition is deleted 
    collaborators = models.ManyToManyField(User, related_name="virtualCollaborators", blank=True)     # it's not compulsory to have collaborators
    class Meta:
        ordering = ["-created_at"]  # order according to the timestamp
        constraints = [
            models.CheckConstraint(
                check=Q(end_date__gt=F('start_date')),
                name = "%(app_label)s_%(class)s has valid start-end dates."
            ),
    ]

    @property
    def get_uploaded_artitems(self):
        return ArtItem.objects.filter(virtualExhibition=self)

class OfflineExhibition(AbstractExhibition):
    city = models.CharField(max_length=200,blank=True, null=True)
    country = models.CharField(max_length=200,blank=True, null=True)
    address = models.CharField(max_length=200,blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    collaborators = models.ManyToManyField(User, related_name="offlineCollaborators", blank=True)      # it's not compulsory to have collaborators
    class Meta:
        ordering = ["-created_at"]  # order according to the timestamp
        constraints = [
            models.CheckConstraint(
                check=Q(end_date__gt=F('start_date')),
                name = "%(app_label)s_%(class)s has valid start-end dates."
            ),
    ]