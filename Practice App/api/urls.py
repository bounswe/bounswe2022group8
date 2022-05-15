
"""
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
"""

from django.urls import path, include
from .views import views
from .views import view_TVSeries
# from .views  import view_TVSeries

# practice_home : pattern that matches with the empty route
# That pattern will be handled by the function views.home(request).
# It returns an HttpResponse.

# http://127.0.0.1:8000 --> (base route) index  (HTTP Response)
# http://127.0.0.1:8000/about --> about section (HTTP Response)
# http://127.0.0.1:8000/api/v1 --> REST API  (JSON Response) 

# https://www.freecodecamp.org/news/rest-api-best-practices-rest-endpoint-design-examples/
# Check the article 8. It says that it's good practice to define versions for the API.
# Changed the route so that it includes v1.

urlpatterns = [
    path('', views.home, name = "index"),         # base route
    path('about/', views.about, name = "about"),  # dummy
    path('api/v1/', views.api, name= "api"),
    path('api/v1/episodes/<str:series>', view_TVSeries.episodes, name="episode_list")
]
