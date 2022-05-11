from datetime import datetime
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
import os
# Django creates an automatic id field: https://stackoverflow.com/a/35770315/16530078

def get_avatar_path(instance, filename):
    return os.path.join('avatar', str(instance.id) + "_" + filename)

def get_artitem_path(instance, filename):
    return os.path.join('artitem', str(instance.id) + "_" + filename)

class myUser(models.Model):
    # Built-in User has username and password already.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=254)  # EmailField is a CharField that checks the value for a valid email address using EmailValidator
    followers = models.ManyToManyField(
        to="self", 
        through= "follow",
        related_name="following", 
        symmetrical=False)   # not required
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    profile_image = models.ImageField(upload_to=get_avatar_path, null=True, blank=True)

    def __str__(self):
        return self.name + " " + self.surname 


class Follow(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")

    class Meta:
        constraints = [
            models.UniqueConstraint(name="%(app_label)s_%(class)s_unique_relationships",
            fields=["from_user", "to_user"],
            ),
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_prevent_self_follow",
                check=~models.Q(from_user=models.F("to_user")),
            ),
        ]
    
    def __str__(self):
        return str(self.from_user) + " follows " + str(self.to_user)

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
    owner = models.ForeignKey(myUser, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    artitem_image = models.ImageField(upload_to=get_artitem_path, null=True, blank=True)

    def __str__(self):
        return "Art item: " + self.title

class Comment(models.Model):
    body = models.CharField(max_length=500)
    commented_by = models.ForeignKey(myUser, on_delete= models.CASCADE)  # if user gets deleted from the system, then comment gets deleted
    commented_on = models.ForeignKey(ArtItem, on_delete= models.CASCADE) # if art item gets deleted, then comment gets deleted
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)


    def __str__(self):
        return "A comment made by " + str(self.commented_by) + " on " + str(self.commented_on) 


# Create your models here.