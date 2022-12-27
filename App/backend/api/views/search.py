from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.generics import ListAPIView
from knox.auth import TokenAuthentication, AuthToken
from rest_framework.filters import SearchFilter, OrderingFilter

from ..models.artitem import ArtItem
from ..models.user import User
from ..models.exhibition import OfflineExhibition
from ..models.exhibition import VirtualExhibition
from ..serializers.serializers import ArtItemSerializer, SimpleUserSerializer
from ..serializers.exhibition import OfflineExhibitionSerializer, VirtualExhibitionSerializer

from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth.models import AnonymousUser

from drf_yasg import openapi
import base64

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
    queryset = ArtItem.objects.all().exclude(virtualExhibition__isnull = False)
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
    # method='get',
    operation_description= "Searchs for offline exhibitions by their titles and descriptions.",
    operation_summary="Get all the offline exhibitions according to their titles and descriptions.",
    tags=['search'],
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Successfully retrieved all the offline exhibitions according to the search params.",
            examples={
                "application/json": [
                    {
                    "owner":
                    [
                    {
                        "id": 1,
                        "owner": {
                            "id": 1,
                            "username": "denemes",
                            "name": "",
                            "surname": "",
                            "profile_path": "avatar/default.png"
                        },
                        "title": "My Offline Exhibition",
                        "description": "Art exhibition at street 123.",
                        "poster": {
                            "id": 1,
                            "owner": 1,
                            "title": "My Offline Exhibition",
                            "description": "Art exhibition at street 123.",
                            "category": "PT",
                            "tags": [],
                            "artitem_path": "artitem/artitem-1.png",
                            "created_at": "08-12-2022 23:31:44"
                        },
                        "collaborators": [],
                        "start_date": "08-12-2022 16:00:00",
                        "end_date": "10-12-2020 16:00:00",
                        "created_at": "08-12-2022 23:31:44",
                        "updated_at": "08-12-2022 23:31:44",
                        "city": "İstanbul",
                        "country": "Türkiye",
                        "address": "Beyoglu",
                        "latitude": 41.40338,
                        "longitude": 28.97835,
                        "status": "Ongoing"
                    }
                    ],
                    "collaborator": []
                }
                ]
            }
        )
    }

)

class search_offline_exhibitions_lexical(ListAPIView):
    queryset = OfflineExhibition.objects.all()
    serializer_class = OfflineExhibitionSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', 'description')


@swagger_auto_schema(
    # method='get',
    operation_description= "Searchs for virtual exhibitions by their titles and descriptions.",
    operation_summary="Get all the virtual exhibitions according to their titles and descriptions.",
    tags=['search'],
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Successfully retrieved all the virtual exhibitions according to the search params.",
            examples={
                "application/json": [
                    {
                    "owner":
                     [
                    {
                        "id": 1,
                        "owner": {
                            "id": 1,
                            "username": "denemes",
                            "name": "",
                            "surname": "",
                            "profile_path": "avatar/default.png"
                        },
                        "title": "My Offline Exhibition",
                        "description": "Art exhibition at street 123.",
                        "poster": {
                            "id": 4,
                            "owner": 1,
                            "title": "My Offline Exhibition",
                            "description": "Art exhibition at street 123.",
                            "category": "PT",
                            "tags": [],
                            "artitem_path": "artitem/artitem-4.png",
                            "created_at": "08-12-2022 23:32:34"
                        },
                        "collaborators": [],
                        "artitems_gallery": [
                            {
                                "id": 3,
                                "owner": 1,
                                "title": "Portrait of Joel Miller",
                                "description": "Joel Miller from TLOU universe.",
                                "category": "OT",
                                "tags": [],
                                "artitem_path": "artitem/artitem-3.png",
                                "created_at": "08-12-2022 23:32:18"
                            }
                        ],
                        "start_date": "08-12-2022 16:00:00",
                        "end_date": "10-12-2020 16:00:00",
                        "created_at": "08-12-2022 23:32:34",
                        "updated_at": "08-12-2022 23:32:34",
                        "status": "Ongoing"
                    }
                ],
                "collaborator": []
                }
                ]
            }
        )
    }

)

class search_virtual_exhibitions_lexical(ListAPIView):
    queryset = VirtualExhibition.objects.all()
    serializer_class = VirtualExhibitionSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', 'description')