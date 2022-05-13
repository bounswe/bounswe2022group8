from django.contrib import admin
from .models import myUser, Tag, Comment, ArtItem, Follow


class myUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'id', 'name', 'surname', 'email', 'created_at', 'updated_at']

class TagAdmin(admin.ModelAdmin):
    list_display =  ['tagname', 'id', 'description', 'created_at', 'updated_at']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['body', 'id', 'commented_by', 'commented_on', 'created_at', 'updated_at']

class ArtItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'description', 'owner', 'artitem_image']

admin.site.register(myUser, myUserAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(ArtItem, ArtItemAdmin)
admin.site.register(Follow)
# Register your models here.
