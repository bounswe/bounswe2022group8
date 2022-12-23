from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from ..models.user import User, UserInterest
from django.core import serializers
from django.contrib.auth.models import AnonymousUser
import datetime
from django.utils.timezone import make_aware
from dateutil import parser

from history.models import History
from ..models.artitem import ArtItem

from django.contrib.contenttypes.models import ContentType
from ..serializers.serializers import ArtItemSerializer


@swagger_auto_schema(
    method='GET',
    operation_description="This endpoint with GET request returns a list of 15 art items that have been curated for users interests and that the user has never seen before. This is ofcourse the case if such items exist in the database. Authentication is required.",
    operation_summary="Get recommended art items for user.",
    tags=['recommendation'],
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Successfully received recommended art.",
            examples={
                "application/json": {
                    "artitems": [
                        {
                            "id": 5,
                            "owner": {
                                "id": 2,
                                "username": "string",
                                "name": "st",
                                "surname": "ring",
                                "profile_path": "avatar/default.png"
                            },
                            "title": "vvmvc",
                            "description": "scerc",
                            "category": "PH",
                            "tags": [],
                            "artitem_path": "artitem/defaultart.jpg",
                            "likes": 0,
                            "number_of_views": 0,
                            "created_at": "23-12-2022 20:43:55"
                        },
                        {
                            "id": 7,
                            "owner": {
                                "id": 2,
                                "username": "string",
                                "name": "st",
                                "surname": "ring",
                                "profile_path": "avatar/default.png"
                            },
                            "title": "fervc",
                            "description": "vdfv",
                            "category": "PW",
                            "tags": [],
                            "artitem_path": "artitem/defaultart.jpg",
                            "likes": 0,
                            "number_of_views": 0,
                            "created_at": "23-12-2022 20:44:30"
                        },
                        {
                            "id": 6,
                            "owner": {
                                "id": 2,
                                "username": "string",
                                "name": "st",
                                "surname": "ring",
                                "profile_path": "avatar/default.png"
                            },
                            "title": "dwefv",
                            "description": "vdf",
                            "category": "PT",
                            "tags": [],
                            "artitem_path": "artitem/defaultart.jpg",
                            "likes": 0,
                            "number_of_views": 0,
                            "created_at": "23-12-2022 20:44:14"
                        }
                    ]
                }
            }
        ),
        status.HTTP_400_BAD_REQUEST: openapi.Response(
            description="No bids on art item.",
            examples={
                "application/json": {
                    "detail": "Invalid token."
                },
            }
        ),
    }
)
@api_view(['GET'])
def RecommendArtItemView(request):
    if request.user.is_authenticated:
        user = request.user
        if (request.method == "GET"):
            userinterest = UserInterest.objects.get(user=user)
            category1 = userinterest.first
            category2 = userinterest.second
            category3 = userinterest.third

            artitems = []

            firstcategory = ArtItem.objects.filter(category = category1)
            for item in firstcategory:
                histories = History.objects.filter(user=user, is_art=True, art_id=item.id)
                if(len(histories) == 0):
                    artitems.append(item)
                if(len(artitems)>=5):
                    break
            #print(artitems)
            secondcategory = ArtItem.objects.filter(category = category2)
            for item in secondcategory:
                histories = History.objects.filter(user=user, is_art=True, art_id=item.id)
                if(len(histories) == 0):
                    artitems.append(item)
                if(len(artitems)>=5):
                    break
            #print(artitems)
            thirdcategory = ArtItem.objects.filter(category = category3)
            for item in thirdcategory:
                histories = History.objects.filter(user=user, is_art=True, art_id=item.id)
                if(len(histories) == 0):
                    artitems.append(item)
                if(len(artitems)>=5):
                    break
            #print(artitems)
            if(len(artitems)<15):   
                #Django querysets are lazy. That means a query will hit the database only when you specifically ask for the result.         
                items = ArtItem.objects.all()
                for item in items:
                    histories = History.objects.filter(user=user, is_art=True, art_id=item.id)
                    if(len(histories)==0):
                        artitems.append(item)
                    if(len(artitems)>=15):
                        break

            #print(artitems)
            serializer = ArtItemSerializer(artitems, many=True)
            message = {'artitems': serializer.data}
            return Response(message, status=status.HTTP_200_OK)        
    else:
        message = {'detail': 'Invalid token.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)