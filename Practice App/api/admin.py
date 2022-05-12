from django.contrib import admin
from .models import myUser, Tag, Comment, ArtItem, Follow

admin.site.register(myUser)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(ArtItem)
admin.site.register(Follow)
# Register your models here.
