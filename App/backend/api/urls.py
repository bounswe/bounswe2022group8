
"""
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
"""

from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views.auth import RegisterView, LoginView
from knox import views as knox_views
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status

from drf_yasg import openapi


###
#
#   api/v1/auth/register
#   api/v1/auth/login
#   api/v1/auth/logout
#   api/v1/
#

decorated_logout_view = \
    swagger_auto_schema(
        method='post',
        responses={status.HTTP_204_NO_CONTENT: openapi.Response(
            description="Successfully logged out."
        ),
        status.HTTP_401_UNAUTHORIZED: openapi.Response(
            description="Unauthorized token.",
            examples={
                "application/json": {"detail": "Invalid token."
                }
            }
        )
        },
        tags=["auth"]
    )(knox_views.LogoutView.as_view())

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name="register"),
    path('auth/login/', LoginView.as_view(), name="login"),
    path('auth/logout/', decorated_logout_view, name='logout'),
]

# added to give us the option to choose between default Response template and regular json
# extend the url with <?format=json> to get json
# if you're having any trouble with your views make sure you added format=None to the arguments
# urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
