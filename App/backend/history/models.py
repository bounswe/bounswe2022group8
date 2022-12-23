from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.conf import settings

from .signals import object_viewed_signal

from api.models.artitem import ArtItem
from api.models.user import UserInterest
from api.models.exhibition import AbstractExhibition, OfflineExhibition

User = settings.AUTH_USER_MODEL

class History(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type    = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True) #ArtItem, UserProfile
    object_id       = models.PositiveIntegerField()
    content_object  = GenericForeignKey() #the actual object
    viewed_on       = models.DateTimeField(auto_now_add=True)
    is_art          = models.BooleanField(default=False)
    art_id          = models.IntegerField(default=-1)
    is_exhibition_off   = models.BooleanField(default=False)
    is_exhibition_on   = models.BooleanField(default=False)
    exhibition_id   = models.IntegerField(default=-1)

    def __str__(self):
        return "%s viewed: on %s by %s" %(self.content_object, self.viewed_on, self.user)

    class Meta:
        verbose_name_plural = "Histories"


def object_viewed_receiver(sender, instance, request, *args, **kwargs):
    new_history         = History.objects.create(
        user            =  request.user,
        content_type    = ContentType.objects.get_for_model(sender),
        object_id       = instance.id,
    )
    if(isinstance(instance, ArtItem)):
        new_history.is_art =True
        new_history.art_id =instance.pk
        new_history.save()
        instance.increaseViews()
        instance.updatePopularity()
        userinterest = UserInterest.objects.get(user = request.user)
        userinterest.updateInterest(instance.category, 1)
    elif(isinstance(instance, AbstractExhibition)):
        instance.increaseViews()
        instance.updatePopularity()
        if(isinstance(instance, OfflineExhibition)):
            new_history.is_exhibition_off =True
            new_history.exhibition_id =instance.pk
        else:
            new_history.is_exhibition_on =True
            new_history.exhibition_id =instance.pk
        new_history.save()

object_viewed_signal.connect(object_viewed_receiver)
