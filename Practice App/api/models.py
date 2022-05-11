from datetime import datetime
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Django creates an automatic id field: https://stackoverflow.com/a/35770315/16530078

class myUser(models.Model):
    # Built-in User has username and password already.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=254)  # EmailField is a CharField that checks the value for a valid email address using EmailValidator
    followers = models.ManyToManyField(User, related_name= "followed_by")
    followed_users = models.ManyToManyField(User, related_name= "follows")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)


class Tag(models.Model):
    tagname = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

class Comment(models.Model):
    body = models.CharField(max_length=500)
    commented_by = models.ForeignKey(myUser, on_delete= models.CASCADE)   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

class ArtItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    owner = models.ForeignKey(myUser, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    comments = models.ManyToManyField(Comment)

    
def __str_(self):
    return self.id
  
    

# Create your models here.