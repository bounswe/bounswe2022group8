from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from .user import User
from django.utils.translation import gettext_lazy as _

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
        DRAWING = 'DR', _('Drawing')
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

    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True) # tags are not required
    category = models.CharField(max_length=2, choices=Category.choices, default=Category.OTHER)
    artitem_image = models.ImageField( default='artitem/defaultart.jpg', upload_to='artitem/')
    artitem_path = models.TextField(default= 'artitem/defaultart.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-created_at"]  # order according to the timestamps

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
