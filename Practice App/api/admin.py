from django.contrib import admin
from .models import myUser, Tag, Comment, ArtItem

admin.site.register(myUser)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(ArtItem)
# Register your models here.
