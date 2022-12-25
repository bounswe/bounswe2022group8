from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from knox.models import AuthToken

from ..models.user import User
from ..models.user import Follow
from ..models.artitem import ArtItem, LikeArtItem
from ..serializers.serializers import ArtItemSerializer, ArtItemByTagQuerySerializer
from ..serializers.auth import RegisterSerializer, LoginSerializer
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from knox.auth import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from drf_yasg import openapi
import base64
import boto3
from django.core.files.base import ContentFile
from ..utils import ArtItemStorage
from django.contrib.auth.models import AnonymousUser
from django.db.models import Q
from functools import reduce
import operator


from drf_yasg import openapi
from history.decorators import object_viewed_decorator
from history.signals import object_viewed_signal

# List of routes / method / action:
#
#  http://${host}:8000/api/v1/artitems                            / GET    / Return all of the art items in the system in JSON format
#  http://${host}:8000/api/v1/artitems/<id>                       / GET    / Return an art item with the given id
#  http://${host}:8000/api/v1/artitems/me/<id>                    / DELETE / Delete an art item                   [REQUIRES AUTHENTICATION]
#  http://${host}:8000/api/v1/artitems/me/                        / POST   / create an art item                   [REQUIRES AUTHENTICATION]
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
                            "surname": "Blocker",
                            "profile_path": "avatar/default.png"
                        },
                        "category": "DR",
                        "tags": [],
                        "likes": 5,
                        "artitem_path": "artitem/docker.jpg",
                        "number_of_views": 5,
                        "sale_status": "NS",
                        "minimum_price": 200,
                        "bought_by": None,
                    }
                ]
            }
        ),
        status.HTTP_401_UNAUTHORIZED: openapi.Response(
            description="User cannot be found.",
            examples={
                "application/json": {
                    "detail": "Invalid token."
                }
            }
        ),
    }
)
@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def get_artitems(request):
    if (request.method == "GET"):
        artitems = ArtItem.objects.all()
        serializer = ArtItemSerializer(artitems, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@ swagger_auto_schema(
    method='post',
    operation_description="Uploads an art item to the system.",
    operation_summary="Upload an art item to the system.",
    tags=['artitems'],
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "title": openapi.Schema(type=openapi.TYPE_STRING, description='title of the art item', default="Portrait of Joel Miller"),
            "description": openapi.Schema(type=openapi.TYPE_STRING, description='description of the art item', default="Joel Miller from TLOU universe."),
            "category": openapi.Schema(type=openapi.TYPE_STRING, description='category of the art item', default="OT"),
            "tags": openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_INTEGER), description='an array of tag IDs attached to the art item (can be empty)', default=[1]),
            "artitem_image": openapi.Schema(type=openapi.TYPE_STRING, description='base64 encoded version of the image', default="base64 string")
        }),
    responses={
        status.HTTP_201_CREATED: openapi.Response(
            description="Successfully created an art item.",
            examples={
                "application/json": 
                    {
                        "id": 2,
                        "title": "Docker",
                        "description": "From the perspective of a docker",
                        "owner": {
                            "id": 11,
                            "username": "JosephBlocker",
                            "name": "Captain Joseph",
                            "surname": "Blocker",
                            "profile_path": "avatar/default.png"
                        },
                        "category": "DR",
                        "tags": [1],
                        "likes": 0,
                        "artitem_path": "artitem/docker.jpg",
                        "number_of_views": 5,
                        "sale_status": "NS",
                        "minimum_price": 200,
                        "bought_by": None,
                    }
            }
        ),
        status.HTTP_401_UNAUTHORIZED: openapi.Response(
            description="Invalid token.",
            examples={
                "application/json": {"detail": "Invalid token."}
            }
        ),
        status.HTTP_400_BAD_REQUEST: openapi.Response(
            description="Bad Request is raised when the given data is not enough to be serialized as an art item object.",
            examples={
                "application/json": {"category": ["This field is required."]}
            }
        ),
    }
)
@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
@authentication_classes([TokenAuthentication])
def post_artitem(request):
    if (request.method == "POST"):

        # tags must be a list
        if ('tags' in request.data and not isinstance(request.data['tags'], list)):
            # change 'mutable' property
            request.data['tags'] = [request.data['tags']]

        artitem_image_storage = ArtItemStorage()
        # BASE64 DECODING
        # Check if artitem_image is provided. If not, default to defaultart.jpg. If provided, it's in base64 format. Decode it.
        if ('artitem_image' in request.data):
            try:
                image_data = request.data['artitem_image'].split("base64,")[1]
                decoded = base64.b64decode(image_data)
                # iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVQYV2NgYAAAAAMAAWgmWQ0AAAAASUVORK5CYII=
                id_ = 1 if ArtItem.objects.count() == 0 else ArtItem.objects.latest('id').id + 1
                filename = 'artitem-{pk}.png'.format(
                    pk=id_)
                request.data['artitem_image'] = ContentFile(decoded, filename)
                request.data['artitem_path'] = artitem_image_storage.location + \
                    "/" + filename
            except:
                return Response({"Invalid Input": "Given artitem image is not compatible with base64 format."}, status=status.HTTP_400_BAD_REQUEST)

        request.data["owner"] = request.user.id
        serializer = ArtItemSerializer(data=request.data)

        if serializer.is_valid():
            if ('artitem_image' in request.data):
                filename = request.data['artitem_image'].name
                artitem_image_storage.save(
                    filename,  request.data['artitem_image'])

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@ swagger_auto_schema(
    method='delete',
    operation_description="Deletes an art item by its ID. This endpoint requires authentication.",
    operation_summary="Deletes an art item by its ID.",
    tags=['artitems'],
    responses={
        status.HTTP_204_NO_CONTENT: openapi.Response(
            description="Successfully deleted the art item.",
        ),
        status.HTTP_404_NOT_FOUND: openapi.Response(
            description="Art item cannot be found.",
            examples={
                "application/json": {"Not Found": "Any art item with the given ID doesn't exist."}
            }
        ),
        status.HTTP_403_FORBIDDEN: openapi.Response(
            description="User attempts to delete another user's art item.",
            examples={
                "application/json": {"Invalid Attempt": "Cannot delete art item of another user."}
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
def delete_artitem(request, id):
    if request.method == "DELETE":
        try:
            artitem = ArtItem.objects.get(pk=id)
            u = request.user
            if (artitem.owner == u):
                client = boto3.client('s3') 
                client.delete_object(Bucket=ArtItemStorage().bucket_name, Key=artitem.artitem_path)
                artitem.delete()
                            
            else:
                return Response({"Invalid Attempt": "Cannot delete art item of another user."}, status=status.HTTP_403_FORBIDDEN)
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
                            "surname": "Blocker",
                            "profile_path": "avatar/default.png"
                        },
                        "category": "DR",
                        "tags": [],
                        "artitem_path": "artitem/docker.jpg",
                        "number_of_views": 5,
                        "sale_status": "FS",
                        "minimum_price": 50,
                        "bought_by": None,
                        "isLiked": "False"

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
#@object_viewed_decorator()
@api_view(["GET"])
def artitems_by_id(request, id):
    if request.method == "GET":
        try:
            artitem = ArtItem.objects.get(pk=id)
            data = ArtItemSerializer(artitem).data.copy()
            if(isinstance(request.user, AnonymousUser)):
                data["isLiked"] = False
                #print("anonymous")
            else:
                try:
                    LikeArtItem.objects.get(user=request.user, artitem=artitem)
                    data["isLiked"] = True
                except:
                    data["isLiked"] = False
                #print("not anonymous")
                instance = artitem
                object_viewed_signal.send(instance.__class__, instance=instance, request=request)
            return Response(data, status=status.HTTP_200_OK)
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
                            "surname": "Blocker",
                            "profile_path": "avatar/default.png"
                        },
                        "category": "DR",
                        "tags": [],
                        "likes": 5,
                        "artitem_path": "artitem/docker.jpg",
                        "number_of_views": 5,
                        "sale_status": "NS",
                        "minimum_price": 200,
                        "bought_by": None,
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
                            "surname": "Blocker",
                            "profile_path": "avatar/default.png"
                        },
                        "category": "DR",
                        "tags": [],
                        "likes": 5,
                        "artitem_path": "artitem/docker.jpg",
                        "number_of_views": 5,
                        "sale_status": "NS",
                        "minimum_price": 200,
                        "bought_by": None,
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


@ swagger_auto_schema(
    method='get',
    operation_description="Returns art items of the users followed by the currently logged-in user. This API can be handy especially for filling the feed of a user with art items.",
    operation_summary="Get art items of the followed users.",
    tags=['artitems'],
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Successfully retrieved all the art items belonging to the followed users.",
            examples={
                "application/json": [
                    {
                        "id": 2,
                        "owner": {
                            "id": 9,
                            "username": "till_i_collapse",
                            "name": "",
                            "surname": "",
                            "profile_path": "avatar/default.png"
                        },
                        "title": "Portrait of Joel Miller",
                        "description": "Joel Miller from TLOU universe.",
                        "category": "DR",
                        "tags": [],
                        "likes": 5,
                        "artitem_path": "artitem/artitem-0.png",
                        "created_at": "08-12-2022 00:38:25",
                        "number_of_views": 5,
                        "sale_status": "NS",
                        "minimum_price": 200,
                        "bought_by": None,
                    }
                ]
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
@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
@authentication_classes([TokenAuthentication])
def artitems_of_followings(request):

    current_user = request.user
    followings = [follow.to_user for follow in Follow.objects.filter(
        from_user=current_user)]

    artitems = ArtItem.objects.filter(owner__in=followings)
    serializer = ArtItemSerializer(artitems, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)




@ swagger_auto_schema(
    method='get',
    operation_description="Returns art items having all the tags provided the request body.",
    operation_summary="Get art items by tag.",
    query_serializer=ArtItemByTagQuerySerializer,
    tags=['artitems'],
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Successfully retrieved all the art items with the given tags.",
            examples={
                "application/json": [
                    {
                        "id": 2,
                        "owner": {
                            "id": 9,
                            "username": "till_i_collapse",
                            "name": "",
                            "surname": "",
                            "profile_path": "avatar/default.png"
                        },
                        "title": "Portrait of Joel Miller",
                        "description": "Joel Miller from TLOU universe.",
                        "category": "DR",
                        "tags": [],
                        "likes": 5,
                        "artitem_path": "artitem/artitem-0.png",
                        "created_at": "08-12-2022 00:38:25",
                        "number_of_views": 5,
                        "sale_status": "NS",
                        "minimum_price": 200,
                        "bought_by": None
                    }
                ]
            }
        ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
            description="Bad Request is raised when the request body doesn't comply with the expected body format.",
            examples={
                "application/json": {"tags": ["This field is required."]}
            }
        ),
    }
)
@api_view(["GET"])
def artitems_by_tags(request):
    if("tags" not in request.query_params):
        return Response({"tags": ["This field is required."]}, status=status.HTTP_400_BAD_REQUEST)
    
    splitted = request.query_params['tags'].split(",")
    # chained filters approach
    artitems = ArtItem.objects.all()
    for tag in splitted:
       artitems = artitems.filter(tags=int(tag))
    
    serializer = ArtItemSerializer(artitems, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
   