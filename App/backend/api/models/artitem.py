from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from .user import User, UserInterest

from django.template.defaultfilters import date
from django.utils.translation import gettext_lazy as _

import datetime
from django.core.validators import MinValueValidator 

from ..signals import user_created_signal

class Tag(models.Model):
    tagname = models.CharField(max_length=100)
    description = models.CharField(max_length=500)  # description about the tag
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tagname  

class ArtItem(models.Model):

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

    class SaleStatus(models.TextChoices):
        NOTFORSALE = 'NS', _('Not For Sale')
        FORSALE = 'FS', _('For Sale')
        SOLD = 'SO', _('Sold')

    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True) # tags are not required
    category = models.CharField(max_length=2, choices=Category.choices, default=Category.OTHER)
    artitem_image = models.ImageField( default='artitem/defaultart.jpg', upload_to='artitem/')
    artitem_path = models.TextField(default= 'artitem/defaultart.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    virtualExhibition = models.ForeignKey('api.VirtualExhibition', on_delete=models.CASCADE, blank=True, null=True) 
    number_of_views = models.IntegerField(default=0)

    popularity = models.FloatField(default=0)
    sale_status = models.CharField(max_length=2, choices=SaleStatus.choices, default=SaleStatus.NOTFORSALE)
    minimum_price = models.PositiveIntegerField(default=0)
    bought_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="bought_art")

    def increaseViews(self, *args, **kwargs):
        self.number_of_views += 1
        super().save(*args, **kwargs)

    def updatePopularity(self, *args, **kwargs):
        self.popularity = 0.1*((self.created_at.year - 2020)*365 + self.created_at.month*30 + self.created_at.day) + 2*self.get_numberof_likes + 0.5*self.number_of_views
        print(self.popularity)
        super().save(*args, **kwargs)


    class Meta:
        ordering = ["-popularity"]  # order according to popularity
    
    def __str__(self):
        return "Art item: " + self.title

    @property
    def get_numberof_likes(self):
        return len([liked.user for liked in LikeArtItem.objects.filter(artitem=self)])

    @property
    def get_users_who_liked(self):
        return [liked.user for liked in LikeArtItem.objects.filter(artitem=self)]

    
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


class Bid(models.Model):
    class Response(models.TextChoices):
        REJECTED = 'RE', _('Rejected')
        ACCEPTED = 'AC', _('Accepted')
        NORESPONSE = 'NR', _('No Response')

    artitem = models.ForeignKey(ArtItem, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField(validators=[MinValueValidator(0.0)])
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    accepted = models.CharField(max_length=2, choices=Response.choices, default=Response.NORESPONSE)

    def save(self, *args, **kwargs):
        if not self.deadline:
            self.deadline = datetime.datetime.now() + datetime.timedelta(days=2)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.buyer) + " bid " + str(self.amount)  + " on " + str(self.artitem) 

class NewBids(models.Model):
    user = models.OneToOneField(User,
        primary_key=True,
        on_delete=models.CASCADE,
        help_text=_('User (Required).'),
    )
    new_bids = models.ManyToManyField(ArtItem, blank=True)

    class Meta:
        verbose_name_plural = "NewBids"

def user_created_receiver(sender, request, *args, **kwargs):
    new_newbids         = NewBids.objects.create(
        user            =  sender
    )

    userInterest = UserInterest.objects.create(user=sender)

user_created_signal.connect(user_created_receiver)


