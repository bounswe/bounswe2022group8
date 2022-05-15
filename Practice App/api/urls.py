"""
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
"""

from django.urls import path
from .views import views
#from .views  import view_TVSeries
from .views import view_search_by_tag
from rest_framework.urlpatterns import format_suffix_patterns

# practice_home : pattern that matches with the empty route
# That pattern will be handled by the function views.home(request).
# It returns an HttpResponse.

# http://127.0.0.1:8000 --> index  (HTTP Response)
# http://127.0.0.1:8000/about --> about_section  (HTTP Response)
# http://127.0.0.1:8000/api_home --> REST API  (JSON Response) 

urlpatterns = [
    path('', views.home, name = "index"),
    path('about/', views.about, name = "about_section"),
    path('api_home/', views.api_home, name= "rest_api"),
    # path('episodes/<str:series>', view_TVSeries.episodes, name="episode_list")
    path('api/searchbytag/<str:tag>', view_search_by_tag.search_by_tag, name="search_by_tag") #if you're having trouble with tag names make sure it is encoded in the url format. Such as # -> %23. For reference https://www.w3schools.com/tags/ref_urlencode.asp
]

#added to give us the option to choose between default Response template and regular json
#extend the url with <?format=json> to get json
#if you're having any trouble with your views make sure you added format=None to the arguments
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])