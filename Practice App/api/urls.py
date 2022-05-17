"""
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
"""

from django.urls import path
from .views import views
from .views import view_search_user
from rest_framework.urlpatterns import format_suffix_patterns
#from .views  import view_TVSeries

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
    path('api/search_user/<str:username>', view_search_user.search_user, name="username")
]
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])