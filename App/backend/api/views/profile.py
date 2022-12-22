from rest_framework import status
from rest_framework.response import Response
from ..models.user import User
from ..serializers.profile import UserProfileSerializer, UserUpdateProfileSerializer
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from knox.auth import TokenAuthentication, AuthToken
from django.contrib.auth.models import AnonymousUser

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from drf_yasg import openapi
import base64
from django.core.files.base import ContentFile
from ..utils import ProfileImageStorage
from ..models.user import Follow
import datetime

from ..models.models import Comment
from ..models.artitem import ArtItem
from history.models import History

from history.signals import object_viewed_signal

levelThreshold = 10

@ swagger_auto_schema(
    method='get',
    operation_description="Returns username, email, name, surname, about section, location and URL to the profile picture of the user with the given ID. isFollowed field returns True if currently logged-in user follows the given user. Defaults to False if user is a guest user.",
    operation_summary="Get profile information of a user by unique ID.",
    tags=['profile'],
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Successfully retrieved the profile information of a user.",
            examples={
                "application/json": {
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
                    "followings": 2,
                    "isFollowed": True
                }
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
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def profile_api(request, id):
    if (request.method == "GET"):
        try:
            user = User.objects.get(pk=id)
            data = UserProfileSerializer(user).data.copy()
            
            if(isinstance(request.user, AnonymousUser)):
                data["isFollowed"] = False
            else:
                try:
                    Follow.objects.get(from_user=request.user, to_user=user)
                    data["isFollowed"] = True
                except:
                    data["isFollowed"] = False

                instance = user
                object_viewed_signal.send(User, instance=instance, request=request)
            
            return Response(data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"Not Found": "Any user with the given ID doesn't exist."}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({"detail": "Method \"{}\" not allowed.".format(request.method)})


@ swagger_auto_schema(
    method='get',
    operation_description="Returns username, email, name, surname, about section, location and URL of the profile picture (Amazon S3 bucket) of the currently logged in user. It uses token to retrieve the relevant information.",
    operation_summary="Get profile information of the user in the session.",
    tags=['profile'],
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Successfully retrieved the profile information of the current user.",
            examples={
                "application/json": {
                    "id": 1,
                    "username": "budgie",
                    "email": "budgie@mit.edu",
                    "name": "Salvador",
                    "surname": "The Budgie",
                    "about": "Salvador the budgie who has a deep passion for paintings, especially budgie paintings.",
                    "location": "İstanbul",
                    "profile_path": "avatar/default.png",
                    "is_level2": False,
                    "followers": 3,
                    "followings": 2
                }
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
@ swagger_auto_schema(
    method='put',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "name": openapi.Schema(type=openapi.TYPE_STRING, description='name of the user', default="Captain Joseph"),
            "surname": openapi.Schema(type=openapi.TYPE_STRING, description='surname of the user', default="Blocker"),
            "about": openapi.Schema(type=openapi.TYPE_STRING, description='about section of a user', default="A veteran of the Indian Wars, who is deeply interested in impressionist art."),
            "location": openapi.Schema(type=openapi.TYPE_STRING, description='location of a user (text)', default="Santa Fe"),
            "profile_image": openapi.Schema(type=openapi.TYPE_STRING, description='base64 encoded version of an image (text)')
        }),
    operation_description="Updates profile information: name, surname, about section, location and profile image can be updated. If the user doesn't change one of the fields listed below, just return the same value you retrieved with GET. Sending empty string means that user removed the text from the related field. Please observe that this API requires authorization. You have to provide base64 encoded version of the image. You can encode your images from here: https://www.base64-image.de/",

    operation_summary="Update the profile information about the currently logged in user",
    tags=['profile'],
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Successfully updated the profile of the user, here are the updated values:",
            examples={
                "application/json": {
                    "id": 1,
                    "name": "Captain Joseph",
                    "surname": "Blocker",
                    "about": "A veteran of the Indian Wars, who is deeply interested in impressionist art.",
                    "location": "Santa Fe",
                    "profile_path": "avatar/295055.jpg"
                }
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
        status.HTTP_400_BAD_REQUEST: openapi.Response(
            description="Profile image is not in base64 format.",
            examples={
                "application/json": {
                    "Invalid Input": "Given profile image is not compatible with base64 format."
                }
            }
        ),
    }
)
@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticated])
@authentication_classes([TokenAuthentication])
def profile_me_api(request):
    if (request.method == "GET"):
        """
        In views where we require authentication, we can simply get the user from request.user. So practical!
        """
        user = request.user
        user.calculateLevel()
        serializer = UserProfileSerializer(user)
        mydata = serializer.data
        user.new_bid_flag = False
        user.save()
 
        return Response(mydata, status=status.HTTP_200_OK)
    elif (request.method == "PUT"):

        # BASE64 DECODING
        # Check if profile_image is provided. If not, don't change it. If provided, it's in base64 format. Decode it.

        profile_image_storage = ProfileImageStorage()
        if ('profile_image' in request.data):
            try:
                image_data = request.data['profile_image'].split("base64,")[1]
                decoded = base64.b64decode(image_data)
                filename = 'profile-{pk}.png'.format(pk=request.user.pk)
                request.data['profile_image'] = ContentFile(decoded, filename)
                request.data['profile_path'] = profile_image_storage.location + "/" + filename  
            except:
                return Response({"Invalid Input": "Given profile image is not compatible with base64 format."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserUpdateProfileSerializer(
            request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        if ('profile_image' in request.data):
            profile_image_storage.save(
                request.data['profile_image'].name,  request.data['profile_image'])

        serializer.updated_at =  datetime.datetime.now()  
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({"detail": "Method \"{}\" not allowed.".format(request.method)})

@swagger_auto_schema(
    method='GET',
    operation_description="Calculates  (+updates) and returns user is_level2 status.",
    operation_summary="Calculate user level.",
    tags=['level'],
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Successfully calculated user level.",
            examples={
                "application/json": {
                    "detail": "Congratulations! You are now a level 2 user."
                }
            }
        ),
        status.HTTP_400_BAD_REQUEST: openapi.Response(
            description='Invalid token.',
            examples={
                "application/json": {
                    "detail": "Invalid token."
                },
            }
        ),
    }
)
@api_view(['GET'])
def LevelView(request):
    data = request.data
    if (request.method == "GET"):
        if request.user.is_authenticated:
            user = request.user
            if(user.is_level2):
                message = {
                    'detail': 'User has already reached level 2.'}
                return Response(message, status=status.HTTP_200_OK)
            else:
                #level calculation is not dynamic, meaning even if levelThreshold is later raised, gained is_level2 status is not lost 
                comments = Comment.objects._mptt_filter(commented_by=user).count()
                print(comments)
                artitems = ArtItem.objects.filter(owner=user).count()
                print(artitems)
                visits = History.objects.filter(user=user).count()
                print(visits)
                result = 0.8*artitems + 0.1*comments + 0.02*visits
                print(result)
                if(result>levelThreshold and not user.is_level2):
                    user.is_level2 = True
                    user.save()
                    #save
                level = user.is_level2
                if(level):
                    message = {
                        'detail': 'Congratulations! You are now a level 2 user.'}
                    return Response(message, status=status.HTTP_200_OK)
                else:
                    message = {
                        'detail': 'Sorry, you do not qualify for level 2 yet. Do not give up, sharing and discovering more amazing content will definitely help.'}
                    return Response(message, status=status.HTTP_200_OK)
        else:
            message = {'detail': 'Invalid token.'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

    else:
        message = {'detail': 'Method not alllowed.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)