"""
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
"""

from django.urls import path
from .views import views
#from .views  import view_TVSeries

# practice_home : pattern that matches with the empty route
# That pattern will be handled by the function views.home(request).
# It returns an HttpResponse.

# http://127.0.0.1:8000/practice --> practice_home  (HTTP Response)
# http://127.0.0.1:8000/practice/about --> about_section  (HTTP Response)
# http://127.0.0.1:8000/practice/api_home --> REST API  (JSON Response) 

urlpatterns = [
    path('', views.home, name = "practice_home"),
    path('about/', views.about, name = "about_section"),
    path('api_home/', views.api_home, name= "rest_api"),
    # path('episodes/<str:series>', view_TVSeries.episodes, name="episode_list")
]