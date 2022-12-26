from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.generics import ListAPIView
from knox.auth import TokenAuthentication, AuthToken
from rest_framework.filters import SearchFilter, OrderingFilter

from ..models.artitem import ArtItem
from ..models.user import User
from ..serializers.serializers import ArtItemSerializer, SimpleUserSerializer, UserSerializer

from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth.models import AnonymousUser

from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

from drf_yasg import openapi
import base64
from django.db.models import Q

#  http://${host}:8000/api/v1/search-lex/  [Method= GET]

@swagger_auto_schema(
    # method='get',
    operation_description= "Searchs for art items' title, description, owner name and surname, and tags and sorts according to any of these params.",
    operation_summary="Get all the art items according to the search filter.",
    tags=['search'],
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Successfully retrieved all the art items according to the search params.",
            examples={
                "application/json": [
                    {
                        "id": 1,
                        "title": "Flamingos",
                        "description": "Photo I took during my trip to Manavgat",
                        "owner": {
                            "id": 1,
                            "username": "LenaCaptured",
                            "name": "Lena",
                            "surname": "Smith",
                            "profile_path": "avatar/default.png"
                        },
                        "type": "photo",
                        "tags": [],
                        "likes": 5,
                        "artitem_path": "artitem/flamingos.jpg"
                    }
                ]
            }
        )
    }

)
class LexSearchView(ListAPIView):
    queryset = ArtItem.objects.all()
    serializer_class = ArtItemSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', 'description', 'owner__name', 'owner__surname', 'tags__tagname')


#  http://${host}:8000/api/v1/search-lex-user/  [Method= GET]

@swagger_auto_schema(
    # method='get',
    operation_description= "Searchs for users' username, name and surname.",
    operation_summary="Get all the users according to the search filter.",
    tags=['search'],
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Successfully retrieved all the users according to the search params.",
            examples={
                "application/json": [
                    {
                        "id": 1,
                        "username" : "profiladam",
                        "name": "Furkan",
                        "surname" : "Keskin",
                        "profile_path": "dummy_path"
                    }
                ]
            }
        )
    }

)

class LexSearchUserView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = SimpleUserSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('username', 'name', 'surname')



@swagger_auto_schema(
    method='get',
    operation_description= "Searchs for art items' title, description, owner username, and tags in full text search mode. Full text search enables you to make search based on a combination of words (sentence). You have to provide a sentence as a query parameter as follows: ?search=this+is+a+sentence",
    operation_summary="Get all the art items that have semantically related titles, descriptions, owner usernames or tags.",
    tags=['search'],
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Successfully retrieved all the art items according to the search params.",
            examples={
                "application/json": [
                    {
                        "id": 1,
                        "title": "Flamingos",
                        "description": "Photo I took during my trip to Manavgat",
                        "owner": {
                            "id": 1,
                            "username": "LenaCaptured",
                            "name": "Lena",
                            "surname": "Smith",
                            "profile_path": "avatar/default.png"
                        },
                        "type": "photo",
                        "tags": [],
                        "likes": 5,
                        "artitem_path": "artitem/flamingos.jpg"
                    }
                ]
            }
        )
    }
)
@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def search_artitems_fulltext(request):    # ?search=message+goes+here
    if (request.method == "GET"):
        try:
            param = request.query_params['search'].replace("+", " ")
        except:
            return Response({"Please provide the search items as query parameters."}, status=status.HTTP_400_BAD_REQUEST)
        vector = SearchVector('title', 'description', 'owner__username', 'tags__tagname', 'tags__description')
        query = SearchQuery(param, search_type='phrase')
        res = ArtItem.objects.annotate(rank=SearchRank(vector, query)).order_by('-rank')
        return Response(ArtItemSerializer(res, many=True).data, status=status.HTTP_200_OK)



@swagger_auto_schema(
    method='get',
    operation_description= "Searchs for users' username, name and surname.  Full text search enables you to make search based on a combination of words (sentence). You have to provide a sentence as a query parameter as follows: ?search=this+is+a+sentence",
    operation_summary="Get all the users with the given username, name and surname (full text search)",
    tags=['search'],
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Successfully retrieved all the art items according to the search params.",
            examples={
                "application/json": [{
                    "id": 1,
                    "username": "pothepanda",
                    "email": "po@jade.edu",
                    "location": "China",
                    "name": "Po",
                    "surname": "Ping",
                    "about": """The foretold Dragon Warrior of legend, a master of the Panda Style of Kung Fu, noodle lover and an art enthusiast.""",
                    "profile_path": "avatar/default.png",
                    "is_level2": False,
                    "followers": 3,
                    "followings": 2
                }]
                
            }
        )
    }
)
@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def search_users_fulltext(request):    # ?search=message+goes+here
    if (request.method == "GET"):
        try:
            param = request.query_params['search'].replace("+", " ")
        except:
            return Response({"Please provide the search items as query parameters."}, status=status.HTTP_400_BAD_REQUEST)
        vector = SearchVector('username', 'name', 'surname')
        query = SearchQuery(param, search_type='phrase')
        res = User.objects.annotate(rank=SearchRank(vector, query)).order_by('-rank')
        return Response(UserSerializer(res, many=True).data, status=status.HTTP_200_OK)

