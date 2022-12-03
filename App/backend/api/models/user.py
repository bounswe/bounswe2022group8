from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
import random
import hashlib
from artitem import ArtItem
from models import Comment

class User(AbstractUser):
    is_level2 = models.BooleanField('Level2 user (active)', default=False)
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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    profile_image = models.ImageField( default='avatar/default.png', upload_to='avatar/')  # amazon
    profile_path = models.TextField(default='avatar/default.png')                          # avatar/profile.png
    
    #OTP (one time password for password reset)
    otp = models.CharField(max_length=256, null=True, blank=True)

    # # Method to Put a Random OTP in the User table, every time the save is called.
    # def save(self, *args, **kwargs):
    #     number_list = [x for x in range(10)]  # Use of list comprehension
    #     code_items_for_otp = []

    #     for i in range(6):
    #         num = random.choice(number_list)
    #         code_items_for_otp.append(num)

    #     code_string = "".join(str(item) for item in code_items_for_otp)  # list comprehension again
    #     # A six digit random number from the list will be saved in otp field
    #     self.otp = code_string
    #     super().save(*args, **kwargs)

    def changeOTP(self, *args, **kwargs):
        number_list = [x for x in range(10)]  # Use of list comprehension
        code_items_for_otp = []

        for i in range(6):
            num = random.choice(number_list)
            code_items_for_otp.append(num)

        code_string = "".join(str(item) for item in code_items_for_otp)  # list comprehension again
        # A six digit random number from the list will be saved in otp field
        self.otp = hashlib.sha256(code_string.encode('utf-8')).hexdigest()
        super().save(*args, **kwargs)
        return code_string

    def __str__(self):
        return self.name + " " + self.surname 

    @property
    def get_followers(self):
        return len([follow.from_user for follow in Follow.objects.filter(to_user=self)])
    
    @property
    def get_followings(self):
        return len([follow.to_user for follow in Follow.objects.filter(from_user=self)])

    @property
    def get_liked_art_items(self):
        return [liked.artitem for liked in LikeArtItem.objects.filter(user=self)]


class Follow(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)

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
        ordering = ["-created_at"]
    
    def __str__(self):
        return str(self.from_user) + " follows " + str(self.to_user)

class LikeArtItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    artitem = models.ForeignKey(ArtItem, on_delete=models.CASCADE, related_name="+")
    liked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(name="%(app_label)s_%(class)s_unique_relationships",
            fields=["user", "artitem"],
            ),
        ]
        ordering = ["-liked_at"]

    def __str__(self):
        return str(self.user) + " liked " + str(self.artitem)

class LikeComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="+")
    liked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(name="%(app_label)s_%(class)s_unique_relationships",
            fields=["user", "comment"],
            ),
        ]
        ordering = ["-liked_at"]

    def __str__(self):
        return str(self.user) + " liked " + str(self.comment)
