"""
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
"""

from django.urls import path, include
from .views import view_artitems, view_myusers, view_search_by_tag
from rest_framework.urlpatterns import format_suffix_patterns
# from .views  import view_TVSeries

# practice_home : pattern that matches with the empty route
# That pattern will be handled by the function views.home(request).
# It returns an HttpResponse.


# https://www.freecodecamp.org/news/rest-api-best-practices-rest-endpoint-design-examples/
# Check the article 8. It says that it's good practice to define versions for the API.
# Changed the route so that it includes v1.

urlpatterns = [
    path('api/v1/artitems/', view_artitems.artitems, name="artitems"),
    path('api/v1/artitems/users/<int:id>', view_artitems.artitems_by_userid, name="artitems_by_userid"),
    path('api/v1/artitems/users/<str:username>', view_artitems.artitems_by_username, name="artitems_by_username"),
    path('api/v1/artitems/<int:id>', view_artitems.artitems_by_id, name="artitem_by_id"),
    path('api/v1/users/', view_myusers.users, name="users"),
    path('api/v1/users/<int:id>', view_myusers.users_by_id, name="users_by_id"),
    path('api/v1/searchbytag/<str:tag>', view_search_by_tag.search_by_tag, name="search_by_tag"), #if you're having trouble with tag names make sure it is encoded in the url format. Such as # -> %23. For reference https://www.w3schools.com/tags/ref_urlencode.asp
    path('api/v1/searchbytagkeyword/<str:tag>', view_search_by_tag.search_by_tag_keyword, name="search_by_tag_keyword"),
]

#added to give us the option to choose between default Response template and regular json
#extend the url with <?format=json> to get json
#if you're having any trouble with your views make sure you added format=None to the arguments
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])