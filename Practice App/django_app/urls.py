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

# http://127.0.0.1:8000/admin --> redirected to admin.site.urls
# http://127.0.0.1:8000 --> redirected to api.urls 
# http://127.0.0.1:8000

# All routes must be referenced here.

urlpatterns = [
    path('', include('api.urls')),
    path('admin/', admin.site.urls),
    path('', views.home, name="index"),
    path('artitems/', views.all_artitems, name = "artitems"),
    path('artitems/id', views.artitem_by_id, name = "artitems_by_id"),
    path('artitems/users/id', views.artitem_by_user_id, name="artitems_by_user_id"),
    path('artitems/users/username', views.artitem_by_username, name="artitems_by_username"),
    path('artitems/new', views.add_artitem, name = "add_art_item"),
    path('episodes/', views.episodes, name="episodes"),
    path('about/', views.about, name="about_section"),
    path('searchbytag/form', views.formview, name="search_by_tag_form_main"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
