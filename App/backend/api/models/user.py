from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_level2 = models.BooleanField('active user', default=False)
    name = models.CharField(max_length=100, blank=True)
    surname = models.CharField(max_length=100, blank=True)
    about = models.TextField(blank = True)
    location = models.CharField(max_length=100, blank=True)
    username = models.CharField(unique=True, max_length=100, error_messages={
        'unique':  'User with this username already exists.',
    })
    email = models.EmailField(unique=True, max_length=254, error_messages={
        'unique':  'User with this email already exists.',
    }) 

    password = models.CharField(max_length=128)
    # last_login = models.DateTimeField(_("last login"), blank=True, null=True) ? maybe
    # implement follow later
    # followers = models.ManyToManyField(
    #     to="self", 
    #     through= "follow",
    #     related_name="follower",   # user.follower.all() --> return all the followers
    #     symmetrical=False)   # not required
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    profile_image = models.ImageField( default='avatar/default.png', upload_to='avatar/')
    
    def __str__(self):
        return self.name + " " + self.surname 
