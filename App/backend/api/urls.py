
"""
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
"""

from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views.auth import RegisterView, LoginView, resetRequestView, resetPasswordView, resetPasswordLoggedView, delete_account
from .views.profile import profile_api, profile_me_api, LevelView
from .views.artitem import get_artitems, artitems_by_userid, artitems_by_username, artitems_by_id, post_artitem, delete_artitem, artitems_of_followings, artitems_by_tags
from .views.follow import follow_user, unfollow_user, get_my_followers, get_my_followings, get_followers, get_followings
from .views.comments import CommentView, CommentsView
from .views.tags import TagView, TagsView
from .views.search import LexSearchView, LexSearchUserView
from .views.user import users_api
from .views.exhibition import get_exhibitions, get_my_exhibitions, create_offline_exhibition, create_online_exhibition, get_online_exhibitions_by_id, get_offline_exhibitions_by_id, get_offline_exhibitions_by_userid, get_online_exhibitions_by_userid
from .views.like import like_artitem, unlike_artitem, get_liked_artitems_of_user, get_users_who_liked_artitem, like_comment, unlike_comment, get_users_who_liked_comment
from .views.recommendation import RecommendArtItemView, RecommendExhibitionView, RecommendUserView
from .views.bidding import BidArtItemView, BidView

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
    path('auth/request-reset/', resetRequestView, name = "resetRequest"),
    path('auth/password-reset/', resetPasswordView, name = "resetPassword"),
    path('auth/account/delete/', delete_account, name = "delete_account"),
    path('profile/me/password-reset/', resetPasswordLoggedView, name = "resetPasswordLogged"),
    path('users/profile/<int:id>', profile_api, name="profile_by_id"),
    path('users/profile/me/', profile_me_api, name="profile_me"),
    path('users/profile/users/', users_api, name="profile_users"),
    path('artitems/<int:artitemid>/comments/', CommentsView, name="CommentsView"),
    path('artitems/<int:artitemid>/comments/<int:id>/', CommentView, name="CommentView"),
    path('artitems/', get_artitems, name="get_all_artitems"),
    path('artitems/users/<int:id>', artitems_by_userid, name="get_artitems_of_user_id"),
    path('artitems/users/username/<str:username>', artitems_by_username, name="get_artitems_of_user_username"),
    path('artitems/<int:id>', artitems_by_id, name="get_artitem_id"), 
    path('artitems/me/upload/', post_artitem, name="post_artitem"),
    path('artitems/me/remove/<int:id>', delete_artitem, name="delete_artitem"),
    path('users/follow/<int:id>', follow_user, name="follow_user"),
    path('users/unfollow/<int:id>', unfollow_user, name="unfollow_user"),
    path('users/me/followers/', get_my_followers, name="get_my_followers"),
    path('users/me/followings/', get_my_followings, name="get_my_followings"),
    path('users/<int:id>/followers/', get_followers, name="get_followers"),
    path('users/<int:id>/followings/', get_followings, name="get_followings"),
    path('artitems/me/followings/', artitems_of_followings, name="get_artitems_of_followings"),
    path('users/artitems/<int:id>/like/', like_artitem, name="like_artitem"),
    path('users/artitems/<int:id>/unlike/', unlike_artitem, name="unlike_artitem"),
    path('users/<int:id>/liked-artitems/', get_liked_artitems_of_user, name="get_liked_artitems_of_user"),
    path('artitems/<int:id>/likers/', get_users_who_liked_artitem, name="get_users_who_liked_artitem"),
    path('users/comments/<int:id>/like/', like_comment, name="like_comment"),
    path('users/comments/<int:id>unlike/', unlike_comment, name="unlike_comment"),
    path('comments/<int:id>/likers/', get_users_who_liked_comment, name="get_users_who_liked_comment"),
    path('tags/<int:id>', TagView, name="Tagview"),
    path('tags/', TagsView, name="TagsView"),
    path('users/me/level', LevelView, name="LevelView"),
    path('exhibitions/', get_exhibitions, name="get_exhibitions"),
    path('exhibitions/me/offline/', create_offline_exhibition, name="create_offline_exhibitions"),
    path('exhibitions/me/online/', create_online_exhibition, name="create_online_exhibitions"),
    path('exhibitions/online/<int:id>', get_online_exhibitions_by_id, name="get_online_exhibition_by_id"),
    path('exhibitions/offline/<int:id>', get_offline_exhibitions_by_id, name="get_offline_exhibitions_by_id"),
    path('exhibitions/users/<int:userid>/offline/', get_offline_exhibitions_by_userid, name="get_offline_exhibitions_by_userid"),
    path('exhibitions/users/<int:userid>/online/', get_online_exhibitions_by_userid, name="get_online_exhibitions_by_userid"),
    path('artitems/tags/', artitems_by_tags, name="get_artitems_by_tags"),
    path('exhibitions/me/', get_my_exhibitions, name="get my exhibitions"),
    path('recommendations/artitems/', RecommendArtItemView, name="RecommendArtItem"),
    path('recommendations/exhibitions/', RecommendExhibitionView, name="RecommendExhibition"),
    path('recommendations/users/', RecommendUserView, name="RecommendUser"),
    path('artitems/<int:artitemid>/bids/', BidArtItemView, name="BidArtItemView"),
    path('artitems/bids/<int:id>/', BidView, name="BidView"),
    path('artitems/tags/', artitems_by_tags, name="get_artitems_by_tags"),
    path('search/lexical/', LexSearchView.as_view(), name='LexicalSearch'),
    path('search/lexical/users/', LexSearchUserView.as_view(), name='LexicalSearchUser')
]

# added to give us the option to choose between default Response template and regular json
# extend the url with <?format=json> to get json
# if you're having any trouble with your views make sure you added format=None to the arguments
# urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
