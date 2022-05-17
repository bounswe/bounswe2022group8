
"""
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
"""

from django.urls import path, include
from .views import view_artitems
from rest_framework.urlpatterns import format_suffix_patterns
from .views  import view_TVSeries

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
    path('api/v1/episodes/<str:series>', view_TVSeries.episodes, name="episode_list")
]

#added to give us the option to choose between default Response template and regular json
#extend the url with <?format=json> to get json
#if you're having any trouble with your views make sure you added format=None to the arguments
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
