from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.generics import ListAPIView
from knox.auth import TokenAuthentication, AuthToken
from rest_framework.filters import SearchFilter, OrderingFilter

from ..models.artitem import ArtItem
from ..models.user import User
from ..serializers.serializers import ArtItemSerializer

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
    queryset = ArtItem.objects.all()
    serializer_class = ArtItemSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', 'description', 'owner__name', 'owner__surname', 'tags__tagname')
