from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from knox.models import AuthToken

from ..models.user import User
from ..models.artitem import ArtItem
from ..serializers.serializers import ArtItemSerializer
from ..serializers.auth import RegisterSerializer, LoginSerializer
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from knox.auth import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from drf_yasg import openapi
import base64
from django.core.files.base import ContentFile
from ..utils import ProfileImageStorage

from drf_yasg import openapi

# List of routes / method / action:
#
#  http://${host}:8000/api/v1/artitems                            / GET    / Return all of the art items in the system in JSON format
#  http://${host}:8000/api/v1/artitems/<id>                       / GET    / Return an art item with the given id
#  http://${host}:8000/api/v1/artitems/me/                           / DELETE / Delete an art item                   [REQUIRES AUTHENTICATION]
#  http://${host}:8000/api/v1/artitems/me/                            / POST   / create an art item                   [REQUIRES AUTHENTICATION]
#  http://${host}:8000/api/v1/artitems/users/<id>                 / GET    / get all of the art items of the specific user (by id)
#  http://${host}:8000/api/v1/artitems/users/username/<username>  / GET    / get all of the art items of the specific user (by username)
#
import base64
from django.core.files.base import ContentFile


@ swagger_auto_schema(
    method='get',
    operation_description="Returns all the art items in the system. It returns ID of the art item, title, description, (id, username, name, surname) of the owner, tags and URL of the image in AWS S3 bucket.",
    operation_summary="Get all the art items in the system.",
    tags=['artitems'],
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Successfully retrieved all the art items in the system.",
            examples={
                "application/json": [
                    {
                        "id": 2,
                        "title": "Docker",
                        "description": "From the perspective of a docker",
                        "owner": {
                            "id": 11,
                            "username": "JosephBlocker",
                            "name": "Captain Joseph",
                            "surname": "Blocker"
                        },
                        "tags": [],
                        "artitem_image": "https://cmpe451-development.s3.amazonaws.com/artitem/docker.jpg"
                    }
                ]
            }
        )
    }
)
@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def get_artitems(request):
    if (request.method == "GET"):
        artitems = ArtItem.objects.all()
        serializer = ArtItemSerializer(artitems, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST", "DELETE"])
@permission_classes([permissions.IsAuthenticated])
@authentication_classes([TokenAuthentication])
def post_artitem(request):
    # owner id must be provided.
    # list of tag ids or a single tag id must be provided.
    # So we assume that the person who consumes this API, knows necessary IDs.
    #
    #
    # We take the input from frontend in base64 format.
    # We have to decode it and convert to a ContentFile object.
    # Then we store it in S3 bucket.

    if (request.method == "POST"):
        data = request.data.copy()

        # tags must be a list
        if ('tags' in data and not isinstance(data['tags'], list)):
            # change 'mutable' property
            data['tags'] = [data['tags']]

        # BASE64 DECODING
        # Check if artitem_image is provided. If not, default to defaultart.jpg. If provided, it's in base64 format. Decode it.
        if ('artitem_image' in data):
            image_data = data['artitem_image'].split("base64,")[1]
            decoded = base64.b64decode(image_data)
            data['artitem_image'] = ContentFile(decoded, name='decode.png')

        ###
        serializer = ArtItemSerializer(data=data)
        if serializer.is_valid():
            if ('artitem_image' in data):
                with open("media/artitem/decode.png", "wb") as fh:
                    fh.write(decoded)
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        try:
            artitem = ArtItem.objects.get(pk=id)
            artitem.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ArtItem.DoesNotExist:
            return Response({"Not Found": "Any art item with the given ID doesn't exist."}, status=status.HTTP_404_NOT_FOUND)


@ swagger_auto_schema(
    method='get',
    operation_description="Return an art item based on ID.",
    operation_summary="Get an art item with unique ID.",
    tags=['artitems'],
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Successfully retrieved all the art items in the system.",
            examples={
                "application/json": [
                    {
                        "id": 2,
                        "title": "Docker",
                        "description": "From the perspective of a docker",
                        "owner": {
                            "id": 11,
                            "username": "JosephBlocker",
                            "name": "Captain Joseph",
                            "surname": "Blocker"
                        },
                        "tags": [],
                        "artitem_image": "https://cmpe451-development.s3.amazonaws.com/artitem/docker.jpg"
                    }
                ]
            }
        ),
        status.HTTP_404_NOT_FOUND: openapi.Response(
            description="User cannot be found.",
            examples={
                "application/json": {
                    "Not Found": "Any art item with the given ID doesn't exist."
                }
            }
        ),
    }
)
@api_view(["GET"])
def artitems_by_id(request, id):
    if request.method == "GET":
        try:
            artitem = ArtItem.objects.get(pk=id)
            serializer = ArtItemSerializer(artitem)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ArtItem.DoesNotExist:
            return Response({"Not Found": "Any art item with the given ID doesn't exist."}, status=status.HTTP_404_NOT_FOUND)


@ swagger_auto_schema(
    method='get',
    operation_description="Returns art items of a specific user. You should provide the ID of the user.",
    operation_summary="Get art items of a user with ID.",
    tags=['artitems'],
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Successfully retrieved all the art items in the system.",
            examples={
                "application/json": [
                    {
                        "id": 2,
                        "title": "Docker",
                        "description": "From the perspective of a docker",
                        "owner": {
                            "id": 11,
                            "username": "JosephBlocker",
                            "name": "Captain Joseph",
                            "surname": "Blocker"
                        },
                        "tags": [],
                        "artitem_image": "https://cmpe451-development.s3.amazonaws.com/artitem/docker.jpg"
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
def artitems_by_userid(request, id):
    try:
        User.objects.get(pk=id)
        artitems = ArtItem.objects.filter(owner=id)
        serializer = ArtItemSerializer(artitems, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({"Not Found": "Any user with the given ID doesn't exist."}, status=status.HTTP_404_NOT_FOUND)

# api/v1/artitems/users/username/<str:username>


@ swagger_auto_schema(
    method='get',
    operation_description="Returns art items of a specific user. You should provide the username of the user.",
    operation_summary="Get art items of a user with username.",
    tags=['artitems'],
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Successfully retrieved all the art items in the system.",
            examples={
                "application/json": [
                    {
                        "id": 2,
                        "title": "Docker",
                        "description": "From the perspective of a docker",
                        "owner": {
                            "id": 11,
                            "username": "JosephBlocker",
                            "name": "Captain Joseph",
                            "surname": "Blocker"
                        },
                        "tags": [],
                        "artitem_image": "https://cmpe451-development.s3.amazonaws.com/artitem/docker.jpg"
                    }
                ]
            }
        ),
        status.HTTP_404_NOT_FOUND: openapi.Response(
            description="User cannot be found.",
            examples={
                "application/json": {
                    "Not Found": "Any user with the given username doesn't exist."
                }
            }
        ),
    }
)
@api_view(["GET"])
def artitems_by_username(request, username):

    users = User.objects.all()
    user = [x for x in users if x.username == username]
    if (not user):
        return Response({"Not Found": "Any user with the given username doesn't exist."}, status=status.HTTP_404_NOT_FOUND)
    else:
        # we know that length of user must be 1 since username is a unique field
        artitems = ArtItem.objects.filter(owner=user[0].id)
        serializer = ArtItemSerializer(artitems, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
