from datetime import datetime
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Django creates an automatic id field: https://stackoverflow.com/a/35770315/16530078

class myUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)  
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