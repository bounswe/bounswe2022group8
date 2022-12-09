from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from .artitem import ArtItem
from mptt.models import MPTTModel, TreeForeignKey
from .user import User

class Comment(MPTTModel):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    body = models.CharField(max_length=500)
    commented_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)  # if user gets deleted from the system, then comment gets deleted
    commented_on = models.ForeignKey(ArtItem, on_delete= models.CASCADE) # if art item gets deleted, then comment gets deleted
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['created_at']

    def __str__(self):
        return "A comment made by " + str(self.commented_by) + " on " + str(self.commented_on) 

    @property
    def get_numberof_likes(self):
        return len([liked.user for liked in LikeComment.objects.filter(comment=self)])

    @property
    def get_users_who_liked(self):
        return [liked.user for liked in LikeComment.objects.filter(comment=self)]


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