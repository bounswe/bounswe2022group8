from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
import random
import hashlib

from django.apps import apps
from django.utils.translation import gettext_lazy as _

# from .models import Comment
# from .artitem import ArtItem
# from history.models import History

levelThreshold = 10

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

    popularity = models.FloatField(default=0)

    new_bid_flag = models.BooleanField(default=False)
    
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

#level calculation is not dynamic, meaning even if levelThreshold is later raised, gained is_level2 status is not lost 
    def calculateLevel(self, *args, **kwargs):

        Comment = apps.get_model('api', 'Comment')
        ArtItem = apps.get_model('api', 'ArtItem')
        History = apps.get_model('history', 'History')

        comments = Comment.objects._mptt_filter(commented_by=self).count()
        artitems = ArtItem.objects.filter(owner=self).count()
        visits = History.objects.filter(user=self).count()
        result = 0.8*artitems + 0.1*comments + 0.02*visits
        print(result)
        if(result>levelThreshold and not self.is_level2):
            self.is_level2 = True
        return self.is_level2

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     super().save(*args, **kwargs)
    #     # create an instance of user interests
    #     UserInterest.objects.create(user=self)

    def updatePopularity(self, *args, **kwargs):

        ArtItem = apps.get_model('api', 'ArtItem')
        VirtualExhibition = apps.get_model('api', 'VirtualExhibition')
        OfflineExhibition = apps.get_model('api', 'OfflineExhibition')
        

        followers = self.get_followers
        #print(followers)
        artitems = ArtItem.objects.filter(owner=self).count()
        #print(artitems)
        ownedExhibitions = OfflineExhibition.objects.filter(owner=self).count() + VirtualExhibition.objects.filter(owner=self).count()
        #print(ownedExhibitions)
        #collaboratedExhibitions = VirtualExhibition.objects.filter(collaborators__in=[self]).count()

        self.popularity = followers + 0.5*artitems + 2*ownedExhibitions
        #print(self.popularity)
        super().save(*args, **kwargs)

    def __str__(self):
        return "User: " + self.name + " " + self.surname 
        

    @property
    def get_followers(self):
        return len([follow.from_user for follow in Follow.objects.filter(to_user=self)])
    
    @property
    def get_followings(self):
        return len([follow.to_user for follow in Follow.objects.filter(from_user=self)])


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


class UserInterest(models.Model):
    user = models.OneToOneField(User,
        primary_key=True,
        on_delete=models.CASCADE,
        help_text=_('User (Required).'),
    )
    AR = models.IntegerField(default=0)
    SC = models.IntegerField(default=0)
    SK = models.IntegerField(default=0)
    DR = models.IntegerField(default=0)
    PT = models.IntegerField(default=0)
    PH = models.IntegerField(default=0)
    PR = models.IntegerField(default=0)
    PA = models.IntegerField(default=0)
    PO = models.IntegerField(default=0)
    PW = models.IntegerField(default=0)
    PD = models.IntegerField(default=0)
    PM = models.IntegerField(default=0)
    PG = models.IntegerField(default=0)
    PP = models.IntegerField(default=0)
    PE = models.IntegerField(default=0)
    PF = models.IntegerField(default=0)
    PS = models.IntegerField(default=0)
    OP = models.IntegerField(default=0)
    OT = models.IntegerField(default=0)

    class Category(models.TextChoices):
        ARCHITECTURE = 'AR', _('Architecture')
        SCULPTURE = 'SC', _('Sculpture')
        SKETCH = 'SK', _('Sketch')
        DRAWING = 'DR', _('Drawing')
        POSTER = 'PT', _('Poster')
        PHOTOGRAPHY = 'PH', _('Photography')
        PRINTS = 'PR', _('Prints')
        PAINTING_ACRYLIC = 'PA', _('Painting/Acrylic')
        PAINTING_OILPAINT = 'PO', _("Painting Oilpaint")
        PAINTING_WATERCOLOUR = 'PW', _("Painting Watercolour")
        PAINTING_DIGITAL = 'PD', _("Painting Digital")
        PAINTING_MURAL = 'PM', _("Painting Mural")
        PAINTING_GOUACHE = 'PG', _("Painting Gouache")
        PAINTING_PASTEL = 'PP', _("Painting Pastel")
        PAINTING_ENCAUSTIC = 'PE', _("Painting Encaustic")
        PAINTING_FRESCO = 'PF', _("Painting Fresco")
        PAINTING_SPRAY = 'PS', _("Painting Spray")
        PAINTING_OTHER = 'OP', _("Painting Other")
        OTHER = 'OT', _("Other")

    first = models.CharField(max_length=2, choices=Category.choices, default=Category.OTHER)
    second = models.CharField(max_length=2, choices=Category.choices, default=Category.OTHER)
    third = models.CharField(max_length=2, choices=Category.choices, default=Category.OTHER)

    def updateFirstThree(self, field, *args, **kwargs):
        if(getattr(self, field) > getattr(self, self.first)):
            self.third = self.second
            self.second = self.first
            self.first = field
        elif(getattr(self, field) > getattr(self, self.second)):
            self.third = self.second
            self.second = field
        elif(getattr(self, field) > getattr(self, self.third)):
            self.third = field
        

    def updateInterest(self, field, number, *args, **kwargs):
        setattr(self, field, getattr(self, field) + number)
        self.updateFirstThree(field)
        super().save(*args, **kwargs)



