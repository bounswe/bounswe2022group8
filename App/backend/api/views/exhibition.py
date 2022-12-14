from rest_framework import generics, status
from rest_framework.response import Response
from knox.models import AuthToken

from ..models.user import User
from ..models.artitem import ArtItem
from ..models.exhibition import AbstractExhibition, OfflineExhibition, VirtualExhibition, ExhibitionArtItem
from ..serializers.serializers import ArtItemSerializer
from ..serializers.auth import RegisterSerializer, LoginSerializer
from ..serializers.exhibition import OfflineExhibitionSerializer, VirtualExhibitionSerializer, ExhibitionArtItemSerializer, SimpleExhibitionArtItemSerializer
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from knox.auth import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from drf_yasg import openapi
import base64
import boto3
from django.core.files.base import ContentFile
from ..utils import ArtItemStorage
from django.db import IntegrityError

from drf_yasg import openapi

#  http://${host}:8000/api/v1/exhibitions/                        / GET    / Return all of the exhibitions in the system
#  http://${host}:8000/api/v1/exhibitions/online/<id>             / GET    / Return an online exhibition with the given id
#  http://${host}:8000/api/v1/exhibitions/offline/<id>            / GET    / Return an offline exhibition with the given id
#  http://${host}:8000/api/v1/exhibitions/me/offline/<id>         / DELETE / Delete an offline exhibition you opened              [REQUIRES AUTHENTICATION]
#  http://${host}:8000/api/v1/exhibitions/me/offline              / POST   / create an exhibition                         [REQUIRES AUTHENTICATION]
#  http://${host}:8000/api/v1/exhibitions/me/online               / POST   / create an exhibition                         [REQUIRES AUTHENTICATION]
#  http://${host}:8000/api/v1/exhibitions/users/<id>/offline/     / GET    / get all of the offline exhibitions of the specific user (by id)
#  http://${host}:8000/api/v1/exhibitions/users/<id>/online/      / GET    / get all of the virtual exhibitions of the specific user (by id)

@ swagger_auto_schema(
    method='get',
    operation_description="Exhibitions API. Returns all the exhibitions in the system. This API can be used to populate the feed with different exhibitions.",
    operation_summary="Get all the exhibitions in the system.",
    tags=['exhibitions'],
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Successfully retrieved all the exhibitions in the system.",
            examples={
                "application/json": {
                "Offline Exhibitions": [
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
                            "type": "poster",
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
                        "status": "On Going"
                    }
                ],
                "Virtual Exhibitions": [
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
                            "type": "poster",
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
                                "type": "sketch",
                                "tags": [],
                                "artitem_path": "artitem/artitem-3.png",
                                "created_at": "08-12-2022 23:32:18"
                            }
                        ],
                        "start_date": "08-12-2022 16:00:00",
                        "end_date": "10-12-2020 16:00:00",
                        "created_at": "08-12-2022 23:32:34",
                        "updated_at": "08-12-2022 23:32:34",
                        "status": "On Going"
                    }
                ]
            }
            }
        )
    }
)
@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def get_exhibitions(request):
    if (request.method == "GET"):
        offline_exhibitions = OfflineExhibition.objects.all()
        online_exhibitions = VirtualExhibition.objects.all()
        offline_serializer = OfflineExhibitionSerializer(offline_exhibitions, many=True)
        online_serializer = VirtualExhibitionSerializer(online_exhibitions, many=True)
        return Response({
            "Offline Exhibitions": offline_serializer.data,
            "Virtual Exhibitions": online_serializer.data
        }, status=status.HTTP_200_OK)


@ swagger_auto_schema(
    method='get',
    operation_description="Exhibitions API. Returns the virtual exhibition with the given id.",
    operation_summary="Get a virtual exhibition with ID.",
    tags=['exhibitions'],
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Successfully retrieved the requested online exhibition.",
            examples={
                "application/json": {
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
                    "type": "poster",
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
                        "type": "sketch",
                        "tags": [],
                        "artitem_path": "artitem/artitem-3.png",
                        "created_at": "08-12-2022 23:32:18"
                    }
                ],
                "start_date": "08-12-2022 16:00:00",
                "end_date": "10-12-2020 16:00:00",
                "created_at": "08-12-2022 23:32:34",
                "updated_at": "08-12-2022 23:32:34",
                "status": "On Going"
                }
            }
        ),
        status.HTTP_404_NOT_FOUND: openapi.Response(
            description="Exhibition cannot be found.",
            examples={
                "application/json": {
                    "Not Found": "Any virtual exhibition with the given ID doesn't exist."
                }
            }
        ),
    }
)
@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def get_online_exhibitions_by_id(request, id):
    if request.method == "GET":
        try:
            virtualExhibition = VirtualExhibition.objects.get(pk=id)
            serializer = VirtualExhibitionSerializer(virtualExhibition)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except VirtualExhibition.DoesNotExist:
            return Response({"Not Found": "Any virtual exhibition with the given ID doesn't exist."}, status=status.HTTP_404_NOT_FOUND)




@ swagger_auto_schema(
    method='get',
    operation_description="Exhibitions API. Returns the offline exhibition with the given id.",
    operation_summary="Get a offline exhibition with ID.",
    tags=['exhibitions'],
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Successfully retrieved the requested offline exhibition.",
            examples={
                "application/json": {
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
                        "type": "poster",
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
                    "status": "On Going"
                }
            }
        ),
        status.HTTP_404_NOT_FOUND: openapi.Response(
            description="Exhibition cannot be found.",
            examples={
                "application/json": {
                    "Not Found": "Any offline exhibition with the given ID doesn't exist."
                }
            }
        ),
    }
)
@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def get_offline_exhibitions_by_id(request, id):
    if request.method == "GET":
        try:
            virtualExhibition = OfflineExhibition.objects.get(pk=id)
            serializer = OfflineExhibitionSerializer(virtualExhibition)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except OfflineExhibition.DoesNotExist:
            return Response({"Not Found": "Any offline exhibition with the given ID doesn't exist."}, status=status.HTTP_404_NOT_FOUND)




@ swagger_auto_schema(
    method='get',
    operation_description="Exhibitions API. Returns the offline exhibitions of a user with the given id.",
    operation_summary="Get offline exhibitions of a specific user.",
    tags=['exhibitions'],
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Successfully retrieved the requested offline exhibition.",
            examples={
                "application/json":[
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
                                "type": "poster",
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
                            "status": "On Going"
                        }
                    ]
            }
        ),
        status.HTTP_404_NOT_FOUND: openapi.Response(
            description="User cannot be found.",
            examples={
                "application/json": {
                    "Not Found": "Any user with the given ID doesn't exist."
                }
            }
        ),
    }
)
@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def get_offline_exhibitions_by_userid(request, id):
    if request.method == "GET":
        try:
            User.objects.get(pk=id)
            offlineExhibitions = OfflineExhibition.objects.filter(owner=id)
            serializer = OfflineExhibitionSerializer(offlineExhibitions, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"Not Found": "Any offline exhibition with the given ID doesn't exist."}, status=status.HTTP_404_NOT_FOUND)


@ swagger_auto_schema(
    method='get',
    operation_description="Exhibitions API. Returns the offline exhibitions of a user with the given id.",
    operation_summary="Get offline exhibitions of a specific user.",
    tags=['exhibitions'],
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Successfully retrieved the requested offline exhibition.",
            examples={
                "application/json":[
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
                                "type": "poster",
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
                                    "type": "sketch",
                                    "tags": [],
                                    "artitem_path": "artitem/artitem-3.png",
                                    "created_at": "08-12-2022 23:32:18"
                                }
                            ],
                            "start_date": "08-12-2022 16:00:00",
                            "end_date": "10-12-2020 16:00:00",
                            "created_at": "08-12-2022 23:32:34",
                            "updated_at": "08-12-2022 23:32:34",
                            "status": "On Going"
                        }
                    ]
            }
        ),
        status.HTTP_404_NOT_FOUND: openapi.Response(
            description="User cannot be found.",
            examples={
                "application/json": {
                    "Not Found": "Any user with the given ID doesn't exist."
                }
            }
        ),
    }
)
@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def get_online_exhibitions_by_userid(request, id):
    if request.method == "GET":
        try:
            User.objects.get(pk=id)
            virtualExhibitions = VirtualExhibition.objects.filter(owner=id)
            serializer = VirtualExhibitionSerializer(virtualExhibitions, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"Not Found": "Any virtual exhibition with the given ID doesn't exist."}, status=status.HTTP_404_NOT_FOUND)




@ swagger_auto_schema(
    method='post',
    operation_description="Exhibitions API. Creates an offline exhibition in the system. For offline exhibitions, organize should provide a location information.",
    operation_summary="Creates a offline exhibition in the system.",
    tags=['exhibitions'],
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "title": openapi.Schema(type=openapi.TYPE_STRING, description='title of the exhibition', default="Art Online"),
            "description": openapi.Schema(type=openapi.TYPE_STRING, description='description of the exhibition', default="A collection of beautiful paintings."),
            "start_date": openapi.Schema(type=openapi.TYPE_STRING, description='start date of the exhibition', default="2022-12-08T13:00:00.000Z"),
            "end_date": openapi.Schema(type=openapi.TYPE_STRING, description='end date of the exhibition', default="2020-12-10T13:00:00.000Z"),
            "collaborators": openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_INTEGER), description='IDs of the collaborators', default=[2]),
            "poster": openapi.Schema(type=openapi.TYPE_STRING, description='base64 encoded version of the poster', default="base64 string"),
            "city": openapi.Schema(type=openapi.TYPE_STRING, description='[ONLY FOR OFFLINE EXHIBITIONS] city where the exhibition is held', default="İstanbul"),
            "country": openapi.Schema(type=openapi.TYPE_STRING, description='[ONLY FOR OFFLINE EXHIBITIONS] country where the exhibition is held', default="Türkiye"),
            "address": openapi.Schema(type=openapi.TYPE_STRING, description='[ONLY FOR OFFLINE EXHIBITIONS] address where the exhibition is held', default="Pera Palace Hotel - Beyoglu"),
            "longitude": openapi.Schema(type=openapi.TYPE_NUMBER, description='[ONLY FOR OFFLINE EXHIBITIONS] Longitude of the location', default=41.40338),
            "latitude": openapi.Schema(type=openapi.TYPE_NUMBER, description='[ONLY FOR OFFLINE EXHIBITIONS] Lattitude of the location', default=28.978359),
        }),
    responses={
        status.HTTP_201_CREATED: openapi.Response(
            description="Successfully created an exhibition.",
            examples={
                "application/json": {
                    "id": 1,
                    "owner": {
                        "id": 1,
                        "username": "deneme",
                        "name": "",
                        "surname": "",
                        "profile_path": "avatar/default.png"
                    },
                    "title": "My Offline Exhibition",
                    "description": "Art exhibition at street 123.",
                    "poster": {
                        "id": 2,
                        "owner": 1,
                        "title": "My Offline Exhibition",
                        "description": "Art exhibition at street 123.",
                        "type": "poster",
                        "tags": [],
                        "artitem_path": "artitem/artitem-2.png",
                        "created_at": "08-12-2022 19:42:06"
                    },
                    "collaborators": [],
                    "start_date": "08-12-2022 16:00:00",
                    "end_date": "10-12-2020 16:00:00",
                    "created_at": "08-12-2022 19:42:06",
                    "updated_at": "08-12-2022 19:42:06",
                    "city": "İstanbul",
                    "country": "Türkiye",
                    "address": "Beyoglu",
                    "latitude": 41.40338,
                    "longitude": 28.97835,
                    "status": "On Going"
                }
            }
        ),
        status.HTTP_401_UNAUTHORIZED: openapi.Response(
            description="Invalid token.",
            examples={
                "application/json": {
                    "detail": "Invalid token."
                }
            }
        ),
        status.HTTP_400_BAD_REQUEST: openapi.Response(
            description="Bad Request is raised when the given data is not enough to be serialized as an art item object.",
            examples={
                "application/json": {"poster": ["This field is required."]},
                "application/json": {"collaborators": ["Invalid pk \"2\" - object does not exist."]}
            }
        ),
    }
)
@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
@authentication_classes([TokenAuthentication])
def create_offline_exhibition(request):
    if (request.method == "POST"):
        if('poster' not in request.data):
            return Response({"poster": ["This field is required."]}, status=status.HTTP_400_BAD_REQUEST)
        artitem_image_storage = ArtItemStorage()
        # Our poster will be an art item, let's create a dictionary that will hold the information of art item
        artitemdata = {}
        artitemdata['title'] = request.data['title']
        artitemdata['description'] = request.data['description']
        artitemdata['owner'] = request.user.id
        artitemdata['type'] = 'poster'

        #### Create a ContentFile using the poster provided by the user
        try:
            artitemdata = fetch_image(artitemdata, artitem_image_storage, request.data["poster"])
        except:
            return Response({"Invalid Input": "Given poster image is not compatible with base64 format."}, status=status.HTTP_400_BAD_REQUEST)

        ## serialize the poster first:
        poster_serializer = ArtItemSerializer(data=artitemdata)
        poster = None
        artitem_storage_tuple = None
        if poster_serializer.is_valid():
                filename = artitemdata['artitem_image'].name
                artitem_storage_tuple = (filename,  artitemdata['artitem_image'])
                poster = poster_serializer.save()
        else:
           return Response(poster_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

       
        request.data["owner"] = request.user.id
        request.data["poster"] = poster.id
        serializer = OfflineExhibitionSerializer(data=request.data)

        if serializer.is_valid():
            try:
                serializer.save()

                artitem_image_storage.save(artitem_storage_tuple[0], artitem_storage_tuple[1])
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response({"Invalid request": "Start date must be earlier than the end date."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@ swagger_auto_schema(
    method='post',
    operation_description="Exhibitions API. Creates an online exhibition in the system. Online exhibitions don't require a location.",
    operation_summary="Creates a virtual exhibition in the system.",
    tags=['exhibitions'],
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "title": openapi.Schema(type=openapi.TYPE_STRING, description='title of the exhibition', default="Art Online"),
            "description": openapi.Schema(type=openapi.TYPE_STRING, description='description of the exhibition', default="A collection of beautiful paintings."),
            "start_date": openapi.Schema(type=openapi.TYPE_STRING, description='start date of the exhibition', default="2022-12-08T13:00:00.000Z"),
            "end_date": openapi.Schema(type=openapi.TYPE_STRING, description='end date of the exhibition', default="2020-12-10T13:00:00.000Z"),
            "collaborators": openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_INTEGER), description='IDs of the collaborators', default=[2]),
            "poster": openapi.Schema(type=openapi.TYPE_STRING, description='base64 encoded version of the poster', default="base64 string"),
            "artitems_gallery": openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_INTEGER), description="[ONLY FOR ONLINE EXHIBITIONS] IDs of art items from organizer's gallery", default=[2]),
            "artitems_upload": openapi.Schema(type=openapi.TYPE_ARRAY,  items=openapi.Items(type=openapi.TYPE_STRING), description='[ONLY FOR ONLINE EXHIBITIONS] List of base64 encodings for uploaded images', default=["img1-base64", "img2-base64"])
        }),
    responses={
        status.HTTP_201_CREATED: openapi.Response(
            description="Successfully created an exhibition.",
            examples={
                "application/json": {
                    "id": 27,
                    "owner": {
                        "id": 1,
                        "username": "deneme",
                        "name": "",
                        "surname": "",
                        "profile_path": "avatar/default.png"
                    },
                    "title": "My Offline Exhibition",
                    "description": "Art exhibition at street 123.",
                    "poster": {
                        "id": 61,
                        "owner": 1,
                        "title": "My Offline Exhibition",
                        "description": "Art exhibition at street 123.",
                        "type": "poster",
                        "tags": [],
                        "artitem_path": "artitem/artitem-61.png",
                        "created_at": "08-12-2022 23:18:13"
                    },
                    "collaborators": [],
                    "artitems_gallery": [
                        {
                            "id": 57,
                            "owner": 1,
                            "title": "Portrait of Joel Miller",
                            "description": "Joel Miller from TLOU universe.",
                            "type": "sketch",
                            "tags": [],
                            "artitem_path": "artitem/artitem-57.png",
                            "created_at": "08-12-2022 23:15:21"
                        }
                    ],
                    "start_date": "08-12-2022 16:00:00",
                    "end_date": "10-12-2020 16:00:00",
                    "created_at": "08-12-2022 23:18:13",
                    "updated_at": "08-12-2022 23:18:13",
                    "status": "On Going",
                    "uploaded_images": [
                        {
                            "id": 62,
                            "virtualExhibition": 27,
                            "artitem_path": "artitem/artitem-62.png",
                            "created_at": "08-12-2022 23:18:16"
                        }
                    ]
                }
            }
        ),
        status.HTTP_401_UNAUTHORIZED: openapi.Response(
            description="Invalid token.",
            examples={
                "application/json": {
                    "detail": "Invalid token."
                }
            }
        ),
        status.HTTP_400_BAD_REQUEST: openapi.Response(
            description="Bad Request is raised when the given data is not enough to be serialized as an art item object.",
            examples={
                "application/json": {"poster": ["This field is required."]},
                "application/json": {"collaborators": ["Invalid pk \"2\" - object does not exist."]}
            }
        ),
    }
)
@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
@authentication_classes([TokenAuthentication])
def create_online_exhibition(request):
    if (request.method == "POST"):
        if('poster' not in request.data):
            return Response({"poster": ["This field is required."]}, status=status.HTTP_400_BAD_REQUEST)
        artitem_image_storage = ArtItemStorage()
        # Our poster will be an art item, let's create a dictionary that will hold the information of art item
        artitemdata = {}
        artitemdata['title'] = request.data['title']
        artitemdata['description'] = request.data['description']
        artitemdata['owner'] = request.user.id
        artitemdata['type'] = 'poster'

        #### Create a ContentFile using the poster provided by the user
        try:
            artitemdata = fetch_image(artitemdata, artitem_image_storage, request.data["poster"])
        except:
            return Response({"Invalid Input": "Given poster image is not compatible with base64 format."}, status=status.HTTP_400_BAD_REQUEST)

        ## serialize the poster first:
        poster_serializer = ArtItemSerializer(data=artitemdata)
        poster = None
        artitem_storage_tuple = None
        if poster_serializer.is_valid():
                filename = artitemdata['artitem_image'].name
                artitem_storage_tuple = (filename,  artitemdata['artitem_image'])
                poster = poster_serializer.save()
        else:
           return Response(poster_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        request.data["owner"] = request.user.id
        request.data["poster"] = poster.id
        # request.data['artitems_gallery'] holds IDs of art items.

        # now, we should upload the images
        artitemdata = {}
        artitemdata['owner'] = request.user.id
        objects = []
        if("artitems_upload" in request.data):
            for base64 in request.data["artitems_upload"]:
                try:
                    objects.append(fetch_image(artitemdata.copy(), artitem_image_storage, base64))
                except:
                    return Response({"Invalid Input": "Uploaded image is not compatible with base64 format."}, status=status.HTTP_400_BAD_REQUEST)
            
        if('artitems_gallery' in request.data and not validate_ids(request.data['artitems_gallery'], request.data["owner"])):
            return Response({"Invalid Input": "Given art items either do not exist or belong to someone else. A user cannot add an art item belonging to someone else to his exhibition."}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = VirtualExhibitionSerializer(data=request.data)

        # So, the main logic in the following code is this:
        # For all uploaded art items, first we have to decode them.
        # ExhibitionArtItem object has a foreign key to Exhibition.
        # First, I decode each base64 string to an object above. objects is an array of objects corresponding to images.
        # Then, I create the exhibition object. 
        # After creating the exhibition object, we have to create ExhibitionArtItem objects.
        # To do so, add the exhibition id to each dictionary (obj) first. Then check if the serializer is valid.
        # If it's valid, save the image object but do not upload it to S3 yet. Store the IDs of the saved image objects.
        # If any one of the serializers turn out to be invalid, delete all the images you created and return 400.
        # If not, upload each image to S3 afterwards.

        if serializer.is_valid():
            try:
                virtualexhibition = serializer.save()
            except IntegrityError:
                return Response({"Invalid request": "Start date must be earlier than the end date."}, status=status.HTTP_400_BAD_REQUEST)
            returndata = serializer.data
            images = []
            savedimgs = []
            for obj in objects:
                obj["virtualExhibition"] = virtualexhibition.id
                imgserializer = ExhibitionArtItemSerializer(data=obj)
                if imgserializer.is_valid():
                    filename = imgserializer.validated_data.get('artitem_image').name
                    images.append((filename, imgserializer.validated_data.get('artitem_image')))
                    img = imgserializer.save()
                    savedimgs.append(img)
                else:
                    for savedimg in savedimgs:
                        uas =  ExhibitionArtItem.objects.get(pk=savedimg.id)
                        uas.delete()            # delete the images
                    virtualexhibition.delete()  # delete the exhibition
                    return Response(imgserializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            for i in images:
                artitem_image_storage.save(i[0],  i[1])
            artitem_image_storage.save(artitem_storage_tuple[0], artitem_storage_tuple[1])
            
            returndata["uploaded_images"] = SimpleExhibitionArtItemSerializer(savedimgs, many=True).data
            return Response(returndata, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

@ swagger_auto_schema(
    method='delete',
    operation_description="Deletes an offline exhibition by its ID. This endpoint requires authentication.",
    operation_summary="Deletes an offline exhibition by its ID.",
    tags=['exhibitions'],
    responses={
        status.HTTP_204_NO_CONTENT: openapi.Response(
            description="Successfully deleted the exhibition.",
        ),
        status.HTTP_404_NOT_FOUND: openapi.Response(
            description="Exhibition cannot be found.",
            examples={
                "application/json": {"Not Found": "Any exhibition with the given ID doesn't exist."}
            }
        ),
        status.HTTP_403_FORBIDDEN: openapi.Response(
            description="User attempts to delete another user's exhibition.",
            examples={
                "application/json": {"Invalid Attempt": "Cannot delete exhibition of another user."}
            }
        ),
        status.HTTP_401_UNAUTHORIZED: openapi.Response(
            description="Invalid token.",
            examples={
                "application/json": {
                    "detail": "Invalid token."
                }
            }
        ),
    }
)
@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
@authentication_classes([TokenAuthentication])
def delete_offline_exhibition(request, id):
    if request.method == "DELETE":
        try:
            offlineExhibitions = OfflineExhibition.objects.get(owner=id)
            u = request.user
            if (offlineExhibitions.owner == u):
                client = boto3.client('s3') 
                client.delete_object(Bucket=ArtItemStorage().bucket_name, Key=offlineExhibitions.poster.artitem_path)
                offlineExhibitions.delete()
                            
            else:
                return Response({"Invalid Attempt": "Cannot delete art item of another user."}, status=status.HTTP_403_FORBIDDEN)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except OfflineExhibition.DoesNotExist:
            return Response({"Not Found": "Any art item with the given ID doesn't exist."}, status=status.HTTP_404_NOT_FOUND)




@ swagger_auto_schema(
    method='delete',
    operation_description="Deletes a virtual exhibition by its ID. This endpoint requires authentication.",
    operation_summary="Deletes a virtual exhibition by its ID.",
    tags=['exhibitions'],
    responses={
        status.HTTP_204_NO_CONTENT: openapi.Response(
            description="Successfully deleted the exhibition.",
        ),
        status.HTTP_404_NOT_FOUND: openapi.Response(
            description="Exhibition cannot be found.",
            examples={
                "application/json": {"Not Found": "Any exhibition with the given ID doesn't exist."}
            }
        ),
        status.HTTP_403_FORBIDDEN: openapi.Response(
            description="User attempts to delete another user's exhibition.",
            examples={
                "application/json": {"Invalid Attempt": "Cannot delete exhibition of another user."}
            }
        ),
        status.HTTP_401_UNAUTHORIZED: openapi.Response(
            description="Invalid token.",
            examples={
                "application/json": {
                    "detail": "Invalid token."
                }
            }
        ),
    }
)
@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
@authentication_classes([TokenAuthentication])
def delete_online_exhibition(request, id):
    if request.method == "DELETE":
        try:
            virtualexhibition = VirtualExhibition.objects.get(owner=id)
            u = request.user
            if (virtualexhibition.owner == u):
                client = boto3.client('s3') 
                client.delete_object(Bucket=ArtItemStorage().bucket_name, Key=virtualexhibition.poster.artitem_path)

                images = ExhibitionArtItem.objects.filter(virtualExhibition=virtualexhibition.id)
                for image in images:
                    client.delete_object(Bucket=ArtItemStorage().bucket_name, Key=image.artitem_path)
                virtualexhibition.delete()
                            
            else:
                return Response({"Invalid Attempt": "Cannot delete virtual exhibition of another user."}, status=status.HTTP_403_FORBIDDEN)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except VirtualExhibition.DoesNotExist:
            return Response({"Not Found": "Any virtual exhibition with the given ID doesn't exist."}, status=status.HTTP_404_NOT_FOUND)



### HELPER FUNCTIONS ####
def fetch_image(artitemdata, artitem_image_storage, base64s):
    image_data = base64s.split("base64,")[1]
    decoded = base64.b64decode(image_data)
    id_ = 1 if ArtItem.objects.count() == 0 else ArtItem.objects.latest('id').id + 1
    filename = 'artitem-{pk}.png'.format(pk=id_)

    artitemdata['artitem_image'] = ContentFile(decoded, filename)
    artitemdata['artitem_path'] = artitem_image_storage.location + \
        "/" + filename
    return artitemdata

def validate_ids(artitems, userid):
    owned_artitems = ArtItem.objects.filter(owner=userid)
    owned_artitem_ids = [i.id for i in owned_artitems]
    return all([True if artitemid in owned_artitem_ids else False for artitemid in artitems])  # all given art items should belong to the current user
        