from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from ..models.user import User, UserInterest, Follow
from django.core import serializers
from django.contrib.auth.models import AnonymousUser
import datetime
from django.utils.timezone import make_aware
from dateutil import parser

from history.models import History
from ..models.artitem import ArtItem
from ..models.exhibition import OfflineExhibition, VirtualExhibition

from django.contrib.contenttypes.models import ContentType
from ..serializers.serializers import ArtItemSerializer, UserSerializer
from ..serializers.exhibition import OfflineExhibitionSerializer, VirtualExhibitionSerializer


@swagger_auto_schema(
    method='GET',
    operation_description="This endpoint with GET request does one of two things depending on whether the user is authenticated or not. If user is logged in, it returns a list of 15 art items that have been curated for user's interests, are popular and that the user has never seen before. If the user is anonymous, it returns a list of 25 art items that are popular. This is ofcourse the case if such items exist in the database.",
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
        status.HTTP_401_UNAUTHORIZED: openapi.Response(
            description="Authentication required.",
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
        if (request.method == "GET"):
            artitems = []

            items = ArtItem.objects.all()
            for item in items:
                artitems.append(item)
                if (len(artitems) >= 25):
                    break

            #print(artitems)
            serializer = ArtItemSerializer(artitems, many=True)
            message = {'artitems': serializer.data}
            return Response(message, status=status.HTTP_200_OK)


@swagger_auto_schema(
    method='GET',
    operation_description="This endpoint with GET request does one of two things depending on whether the user is authenticated or not. If user is logged in, it returns a list of 16 exhibitions (11 virtual + 5 offline) that are popular and that the user has never seen before. If the user is anonymous it just returns a list of 16 exhibitions (11 virtual + 5 offline) that are popular. This is ofcourse the case if such items exist in the database.",
    operation_summary="Get recommended exhibitions for user.",
    tags=['recommendation'],
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Successfully received recommended exhibitions.",
            examples={
                "application/json": {
                    "exhibitions": [
                        {
                            "id": 2,
                            "owner": {
                                "id": 2,
                                "username": "string",
                                "name": "st",
                                "surname": "ring",
                                "profile_path": "avatar/default.png"
                            },
                            "title": "Art Online",
                            "description": "A collection of beautiful paintings.",
                            "poster": {
                                "id": 2,
                                "owner": 2,
                                "title": "Art Online",
                                "description": "A collection of beautiful paintings.",
                                "category": "PT",
                                "tags": [],
                                "artitem_path": "artitem/artitem-2.png",
                                "created_at": "23-12-2022 19:15:22"
                            },
                            "collaborators": [
                                {
                                    "id": 2,
                                    "username": "string",
                                    "name": "st",
                                    "surname": "ring",
                                    "profile_path": "avatar/default.png"
                                }
                            ],
                            "start_date": "08-12-2022 16:00:00",
                            "end_date": "25-12-2022 16:00:00",
                            "created_at": "23-12-2022 19:15:22",
                            "updated_at": "23-12-2022 21:02:11",
                            "city": "İstanbul",
                            "country": "Türkiye",
                            "address": "Pera Palace Hotel - Beyoglu",
                            "latitude": 28.978359,
                            "longitude": 41.40338,
                            "status": "Ongoing"
                        },
                        {
                            "id": 1,
                            "owner": {
                                "id": 2,
                                "username": "string",
                                "name": "st",
                                "surname": "ring",
                                "profile_path": "avatar/default.png"
                            },
                            "title": "virt exh",
                            "description": "nförö",
                            "poster": {
                                "id": 3,
                                "owner": 2,
                                "title": "mldm",
                                "description": "cöşd",
                                "category": "PH",
                                "tags": [],
                                "artitem_path": "artitem/defaultart.jpg",
                                "created_at": "23-12-2022 20:08:29"
                            },
                            "collaborators": [],
                            "artitems_gallery": [
                                {
                                    "id": 6,
                                    "owner": 2,
                                    "title": "dwefv",
                                    "description": "vdf",
                                    "category": "PT",
                                    "tags": [],
                                    "artitem_path": "artitem/defaultart.jpg",
                                    "created_at": "23-12-2022 20:44:14"
                                },
                                {
                                    "id": 5,
                                    "owner": 2,
                                    "title": "vvmvc",
                                    "description": "scerc",
                                    "category": "PH",
                                    "tags": [],
                                    "artitem_path": "artitem/defaultart.jpg",
                                    "created_at": "23-12-2022 20:43:55"
                                }
                            ],
                            "start_date": "23-12-2022 22:12:54",
                            "end_date": "26-12-2022 22:12:58",
                            "created_at": "23-12-2022 22:13:09",
                            "updated_at": "23-12-2022 22:13:09",
                            "status": "Ongoing",
                            "artitems_upload": []
                        }
                    ]
                }
            }
        ),
        status.HTTP_401_UNAUTHORIZED: openapi.Response(
            description="Authentication required.",
            examples={
                "application/json": {
                    "detail": "Invalid token."
                },
            }
        ),
    }
)
@api_view(['GET'])
def RecommendExhibitionView(request):
    if request.user.is_authenticated:
        user = request.user
        if (request.method == "GET"):
            offline = OfflineExhibition.objects.filter(start_date__lte=datetime.datetime.now(), end_date__gte=datetime.datetime.now()).order_by('-popularity')
            #print(offline)
            online = VirtualExhibition.objects.filter(start_date__lte=datetime.datetime.now(), end_date__gte=datetime.datetime.now()).order_by('-popularity')
            
            exhibitions1 = []
            for item in offline:
                histories = History.objects.filter(user=user, is_exhibition_off=True, exhibition_id=item.id)
                if(len(histories) == 0):
                    exhibitions1.append(item)
                if(len(exhibitions1)>=5):
                    break
            #print(exhibitions1)
            exhibitions2 = []
            for item in online:
                histories = History.objects.filter(user=user, is_exhibition_on=True, exhibition_id=item.id)
                if(len(histories) == 0):
                    exhibitions2.append(item)
                if(len(exhibitions2)>=16):
                    break
            #print(exhibitions2)
            
            #not returning exhibitions that have already been viewed, can add if found fitting

            serializer1 = OfflineExhibitionSerializer(exhibitions1, many=True)
            serializer2 = VirtualExhibitionSerializer(exhibitions2, many=True)
            #can separate if it is easier for the frontend
            message = {'exhibitions': serializer1.data + serializer2.data}
            return Response(message, status=status.HTTP_200_OK)        
    else:
        if (request.method == "GET"):
            offline = OfflineExhibition.objects.filter(start_date__lte=datetime.datetime.now(), end_date__gte=datetime.datetime.now()).order_by('-popularity')
            online = VirtualExhibition.objects.filter(start_date__lte=datetime.datetime.now(), end_date__gte=datetime.datetime.now()).order_by('-popularity')
            
            exhibitions1 = []
            for item in offline:
                exhibitions1.append(item)
                if(len(exhibitions1)>=5):
                    break
            exhibitions2 = []
            for item in online:
                exhibitions2.append(item)
                if(len(exhibitions2)>=16):
                    break

            serializer1 = OfflineExhibitionSerializer(exhibitions1, many=True)
            serializer2 = VirtualExhibitionSerializer(exhibitions2, many=True)
            #can separate if it is easier for the frontend
            message = {'exhibitions': serializer1.data + serializer2.data}
            return Response(message, status=status.HTTP_200_OK)


@swagger_auto_schema(
    method='GET',
    operation_description="This endpoint with GET request does one of two things depending on whether the user is authenticated or not. If user is logged in, it returns a list of 16 users that are popular, have similar interest to the user and that the user is not following. If the user is anonymous it just returns a list of 25 users that are popular. This is ofcourse the case if such items(users) exist in the database. Authentication is required. If no users with similar interest found, just popular users are returned.",
    operation_summary="Get recommended users for the user.",
    tags=['recommendation'],
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Successfully received recommended users.",
            examples={
                "application/json": {
                    "users": [
                        {
                            "id": 2,
                            "username": "string",
                            "is_level2": "false",
                            "name": "st",
                            "surname": "ring",
                            "email": "user@example.com",
                            "profile_path": "avatar/default.png",
                            "created_at": "23-12-2022 19:12:57",
                            "updated_at": "23-12-2022 20:03:35"
                        }
                    ]
                }
            }
        ),
        status.HTTP_401_UNAUTHORIZED: openapi.Response(
            description="Authentication required.",
            examples={
                "application/json": {
                    "detail": "Invalid token."
                },
            }
        ),
    }
)
@api_view(['GET'])
def RecommendUserView(request):
    if request.user.is_authenticated:
        user = request.user
        if (request.method == "GET"):

            userinterest = UserInterest.objects.get(user=user)

            myusers = []

            users = User.objects.all().order_by('-popularity').exclude(id=user.id).exclude(is_superuser=True)

            for item in users:
                try:
                    Follow.objects.get(from_user=user, to_user=item)
                except Follow.DoesNotExist:
                    iteminterest=UserInterest.objects.get(user=item)
                    if((iteminterest.first or iteminterest.second or iteminterest.third) == (userinterest.first or userinterest.second or userinterest.third)):
                        myusers.append(item)
                    
                if(len(myusers)>=16):
                    break
            if(len(myusers)<16):
                for item in users:
                    try:
                        Follow.objects.get(from_user=user, to_user=item)
                    except Follow.DoesNotExist:
                        myusers.append(item)

                    if(len(myusers)>=16):
                        break           
            serializer = UserSerializer(myusers, many=True)
            message = {'users': serializer.data}
            return Response(message, status=status.HTTP_200_OK)        
    else:
        if (request.method == "GET"):

            myusers = []

            users = User.objects.all().order_by('-popularity').exclude(is_superuser=True)

            for item in users:
                myusers.append(item)
                    
                if(len(myusers)>=25):
                    break

            serializer = UserSerializer(myusers, many=True)
            message = {'users': serializer.data}
            return Response(message, status=status.HTTP_200_OK) 

