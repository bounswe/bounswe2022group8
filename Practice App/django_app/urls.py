"""django_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

# http://127.0.0.1:8000/admin/ --> redirected to admin.site.urls
# http://127.0.0.1:8000 --> redirected to api.urls 
# http://127.0.0.1:8000/about/ --> redirected to about page

# All routes must be referenced here.

urlpatterns = [
    path('', include('api.urls')),
    path('admin/', admin.site.urls),
    path('', views.home, name="index"),
    path('artitems/', views.all_artitems, name = "artitems"),
    path('artitems/id', views.artitem_by_id, name = "artitems_by_id"),
    path('artitems/id/delete', views.artitem_by_id_delete, name="artitems_by_id_delete_frontend"),
    path('artitems/users/id', views.artitem_by_user_id, name="artitems_by_user_id"),
    path('artitems/users/username', views.artitem_by_username, name="artitems_by_username"),
    path('artitems/new', views.add_artitem, name = "add_art_item"),
    path('episodes/', views.episodes, name="episodes"),
    path('users/', views.all_users, name = 'users_frontend'),
    path('users/new', views.add_user, name='add_user_frontend'),
    path('users/id', views.get_user_by_id, name="user_by_id_frontend"),
    path('users/id/delete', views.delete_user_by_id, name="delete_user_by_id_frontend"),
    path('about/', views.about, name="about_section"),
    path('searchbytag/form', views.formview, name="search_by_tag_form_main"),
    path('tag/', views.list_tags, name="list_tags"),
    path('comments/artitem/id', views.commentsOfArtItem, name= "commentsOfArtItem"),
    path('comments/artitem/new', views.commentOnArtItem, name= "commentOnArtItem"),
    path('user/id/comment/commentid', views.deleteComment, name= "deleteComment"),
    path('tag/id', views.delete_tag, name="delete_tag"),
    path('tag/new', views.add_tags, name="add_tags"),
    path('search_user/',views.search_user ,name="search_user")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
