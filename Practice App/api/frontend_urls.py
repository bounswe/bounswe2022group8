"""
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
"""

from django.urls import path, include
from .views import views
from .views import view_artitems
from .views import views_frontend


# http://127.0.0.1:8000 --> (base route) index  (HTTP Response)
# http://127.0.0.1:8000/gallery 

# https://www.freecodecamp.org/news/rest-api-best-practices-rest-endpoint-design-examples/
# Check the article 8. It says that it's good practice to define versions for the API.
# Changed the route so that it includes v1.

urlpatterns = [
    path('', views_frontend.home, name = "base"),         # base route
    path('gallery/', views_frontend.gallery, name = "gallery"),  # dummy
    # path('api/v1/episodes/<str:series>', view_TVSeries.episodes, name="episode_list")
]