
"""
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
"""

from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views.auth import RegisterView

###
#
#   api/v1/auth/register
#   api/v1/auth/login
#   api/v1/auth/logout
#   api/v1/
#
#

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name="register"),
]

# added to give us the option to choose between default Response template and regular json
# extend the url with <?format=json> to get json
# if you're having any trouble with your views make sure you added format=None to the arguments
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
