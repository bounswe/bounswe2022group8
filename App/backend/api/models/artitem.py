from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from .user import User, LikeArtItem

class Tag(models.Model):
    tagname = models.CharField(max_length=100)
    description = models.CharField(max_length=500)  # description about the tag
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tagname  

class ArtItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True) # tags are not required
    type = models.CharField(max_length=500)
    artitem_image = models.ImageField( default='artitem/defaultart.jpg', upload_to='artitem/')
    artitem_path = models.TextField(default= 'artitem/defaultart.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-created_at"]  # order according to the timestamps

    def __str__(self):
        return "Art item: " + self.title

    @property
    def get_numberof_likes(self):
        return len([liked.user for liked in LikeArtItem.objects.filter(artitem=self)])

    @property
    def get_users_who_liked(self):
        return [liked.user for liked in LikeArtItem.objects.filter(artitem=self)]

    

