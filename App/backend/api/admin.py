from django.contrib import admin
from .models.models import Comment
from .models.artitem import Tag, ArtItem, Bid, NewBids
from .models.user import User
from .models.exhibition import OfflineExhibition, VirtualExhibition, ExhibitionPoster

class UserAdmin(admin.ModelAdmin):
   # exclude = ('otp',)
    list_display = ['username', 'id', 'name', 'surname', 'email', 'created_at', 'updated_at']

class TagAdmin(admin.ModelAdmin):
    list_display =  ['tagname', 'id', 'description', 'created_at', 'updated_at']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['body', 'id', 'parent', 'commented_by', 'commented_on', 'created_at']

class ArtItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'description', 'owner', 'artitem_image']

class OfflineExhibitionAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner', 'title', 'description', 'poster', 'start_date', 'end_date', 'created_at', 'updated_at', 'city', 'country', 'address', 'latitude', 'longitude']

class VirtualExhibitionAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner', 'title', 'description', 'poster',  'start_date', 'end_date', 'created_at', 'updated_at']

class BidAdmin(admin.ModelAdmin):
    list_display = ['id', 'artitem', 'buyer', 'amount', 'created_at', 'deadline', 'accepted']

class ExhibitionPosterAdmin(admin.ModelAdmin):
    list_display = ['id', 'artitem_image', 'artitem_path', 'created_at']

admin.site.register(User, UserAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(ArtItem, ArtItemAdmin)
admin.site.register(OfflineExhibition, OfflineExhibitionAdmin)
admin.site.register(VirtualExhibition, VirtualExhibitionAdmin)
admin.site.register(Bid, BidAdmin)
admin.site.register(NewBids)
admin.site.register(ExhibitionPoster)