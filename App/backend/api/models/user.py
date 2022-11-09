from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
import random

class User(AbstractUser):
    is_level2 = models.BooleanField('Level2 user (active)', default=False)
    name = models.CharField(max_length=100, blank=True)
    surname = models.CharField(max_length=100, blank=True)
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
    
    #OTP (one time password for password reset)
    otp = models.CharField(max_length=6, null=True, blank=True)

    # Method to Put a Random OTP in the User table, every time the save is called.
    def save(self, *args, **kwargs):
        number_list = [x for x in range(10)]  # Use of list comprehension
        code_items_for_otp = []

        for i in range(6):
            num = random.choice(number_list)
            code_items_for_otp.append(num)

        code_string = "".join(str(item) for item in code_items_for_otp)  # list comprehension again
        # A six digit random number from the list will be saved in otp field
        self.otp = code_string
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name + " " + self.surname 
    
