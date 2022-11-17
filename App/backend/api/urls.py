
"""
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
"""

from django.urls import path
from .views.auth import RegisterView, LoginView
from .views.profile import profile_api, profile_me_api
from .views.artitem import get_artitems, artitems_by_userid, artitems_by_username, artitems_by_id, post_artitem, delete_artitem



from .views.comments import CommentView, CommentsView
from knox import views as knox_views
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status

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
        operation_description="Invalidates the token of the current session.",
        operation_summary="Log out from the application safely.",
        responses={status.HTTP_204_NO_CONTENT: openapi.Response(
            description="Successfully logged out."
        ),
            status.HTTP_401_UNAUTHORIZED: openapi.Response(
            description="Unauthorized token.",
            examples={
                "application/json": {"detail": "Invalid token."}
            }
        )
        },
        tags=["auth"])(knox_views.LogoutView.as_view())

# SWAGGER: localhost:8000/api/v1/swagger/schema
urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name="register"),
    path('auth/login/', LoginView.as_view(), name="login"),
    path('auth/logout/', decorated_logout_view, name='logout'),
    path('users/profile/<int:id>', profile_api, name="profile_by_id"),
    path('users/profile/me/', profile_me_api, name="profile_me"),
    path('artitems/<int:artitemid>/comments/', CommentsView, name="CommentsView"),
    path('artitems/<int:artitemid>/comments/<int:id>/', CommentView, name="CommentView"),
    path('artitems/', get_artitems, name="get_all_artitems"),
    path('artitems/users/<int:id>', artitems_by_userid, name="get_artitems_of_user_id"),
    path('artitems/users/username/<str:username>', artitems_by_username, name="get_artitems_of_user_username"),
    path('artitems/<int:id>', artitems_by_id, name="get_artitem_id"), 
    path('artitems/me/upload/', post_artitem, name="post_artitem"),
    path('artitems/me/remove/<int:id>', delete_artitem, name="delete_artitem")
]

# added to give us the option to choose between default Response template and regular json
# extend the url with <?format=json> to get json
# if you're having any trouble with your views make sure you added format=None to the arguments
# urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
