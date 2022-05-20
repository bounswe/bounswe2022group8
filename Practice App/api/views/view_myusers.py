from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse 
from django.forms.models import model_to_dict

from django.contrib.auth.models import User
from ..models import myUser, Follow, ArtItem, Comment, Tag
from ..serializers import myUserSerializer, ArtItemSerializer, CommentSerializer, TagSerializer
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.core.validators import validate_email



from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import parser_classes
import json

import base64
from django.core.files.base import ContentFile
from django.contrib.auth import authenticate



##### List of routes / method / action:
#
#  http://127.0.0.1:8000/api/v1/users                   /  GET    / Return all of the non-admin users in the system in JSON format 
#  http://127.0.0.1:8000/api/v1/users                   /  POST   / Create a user
#  http://127.0.0.1:8000/api/v1/users/<id>              /  GET    / Return a user with the given id
#  http://127.0.0.1:8000/api/v1/users/<id>              /  DELETE / Delete a user with the given id
#

@api_view(["GET", "POST"])
def users(request):
    if request.method=="GET":
        myusers = myUser.objects.all()
        serializer = myUserSerializer(myusers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method=="POST":
        data = request.data.copy()

        user = None

        try:
            user = User.objects.create_user(username=data["username"], password=data["password"])
        except:
            if('password' not in data): return Response({"Please provide a password for the user."}, status=status.HTTP_400_BAD_REQUEST)
            elif('username' not in data): return Response({"Please provide a username for the user."}, status=status.HTTP_400_BAD_REQUEST)
            else: return Response({"Invalid username or username is already taken"}, status=status.HTTP_400_BAD_REQUEST)

    
        if 'name' not in data:
            user.delete()
            return Response({"Name must be set."}, status=status.HTTP_400_BAD_REQUEST)
        if 'surname' not in data:
            user.delete()
            return Response({"Surname must be set."}, status=status.HTTP_400_BAD_REQUEST)
        if 'email' not in data:
            user.delete()
            return Response({"Email must be set."}, status=status.HTTP_400_BAD_REQUEST)

        
        ### BASE64 DECODING
        # Check if profile_image is provided. If not, default to profiledef.png. If provided, it's in base64 format. Decode it.
        if('profile_image' in data):
            image_data= data['profile_image'].split("base64,")[1]
            decoded = base64.b64decode(image_data)
            data['profile_image'] = ContentFile(decoded , name='decode.png')


        if('profile_image' in data):
            with open("media/avatar/decode.png", "wb") as fh:
                try:
                    validate_email(data["email"])
                    myuser = myUser.objects.create(user=user,
                                                name=data["name"],
                                                surname = data["surname"],
                                                email = data["email"],
                                                profile_image = data["profile_image"])
                except:
                    user.delete()
                    return Response({"Invalid input: Please provide a valid email."}, status=status.HTTP_400_BAD_REQUEST)
                    
                fh.write(decoded)
                serializer = myUserSerializer(myuser)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
               
        else:
            try:
                validate_email(data["email"])
                myuser = myUser.objects.create(user=user,
                                             name=data["name"],
                                             surname = data["surname"],
                                             email = data["email"])
            except:
                user.delete()
                return Response({"Invalid input: Please provide a valid email."}, status=status.HTTP_400_BAD_REQUEST)
                
            serializer = myUserSerializer(myuser)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PATCH", "DELETE"])
def users_by_id(request, id):
    try:
        user = myUser.objects.get(pk=id)
    except myUser.DoesNotExist:
        return Response({"Not Found:", "Any user with the given ID doesn't exist."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = myUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PATCH":
        serializer = myUserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
@api_view(['GET'])
def users_by_credentials(request, username,password):
    user = authenticate(username=username , password=password)
    if user is None:
        user = User.objects.get(username=username)
        if user is None:
            return Response( {"Any user with the given credentials doesn't exist."}, status=status.HTTP_404_NOT_FOUND)
        if user.password != password:
            return Response( {"Any user with the given credentials doesn't exist."}, status=status.HTTP_400_BAD_REQUEST)
    serializer = myUserSerializer(myUser.objects.get(user=user))
    return Response(serializer.data, status=status.HTTP_200_OK)