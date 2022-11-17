from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from .artitem import ArtItem

class Comment(MPTTModel):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    body = models.CharField(max_length=500)
    commented_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)  # if user gets deleted from the system, then comment gets deleted
    commented_on = models.ForeignKey(ArtItem, on_delete= models.CASCADE) # if art item gets deleted, then comment gets deleted
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['created_at']

    def __str__(self):
        return "A comment made by " + str(self.commented_by) + " on " + str(self.commented_on) 

