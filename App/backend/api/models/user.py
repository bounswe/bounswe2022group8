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
    
