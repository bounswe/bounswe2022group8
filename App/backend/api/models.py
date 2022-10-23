from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    is_active_user = models.BooleanField('active user', default=False)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=254)  # EmailField is a CharField that checks the value for a valid email address using EmailValidator
    #implement follow later
    # followers = models.ManyToManyField(
    #     to="self", 
    #     through= "follow",
    #     related_name="follower",   # user.follower.all() --> return all the followers
    #     symmetrical=False)   # not required
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    profile_image = models.ImageField( default='avatar/profiledef.png', upload_to='avatar/')
    
    def __str__(self):
        return self.name + " " + self.surname 
    

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
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True) # tags are not required
    artitem_image = models.ImageField( default='artitem/defaultart.jpg', upload_to='artitem/')

    def __str__(self):
        return "Art item: " + self.title


class Comment(models.Model):
    body = models.CharField(max_length=500)
    commented_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)  # if user gets deleted from the system, then comment gets deleted
    commented_on = models.ForeignKey(ArtItem, on_delete= models.CASCADE) # if art item gets deleted, then comment gets deleted
    created_at = models.DateTimeField(auto_now_add=True)
    #can we update comments?
    #updated_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return "A comment made by " + str(self.commented_by) + " on " + str(self.commented_on) 

