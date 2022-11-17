from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from .artitem import ArtItem

class Comment(models.Model):
    body = models.CharField(max_length=500)
    commented_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)  # if user gets deleted from the system, then comment gets deleted
    commented_on = models.ForeignKey(ArtItem, on_delete= models.CASCADE) # if art item gets deleted, then comment gets deleted
    created_at = models.DateTimeField(auto_now_add=True)
    #can we update comments?
    #updated_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return "A comment made by " + str(self.commented_by) + " on " + str(self.commented_on) 

