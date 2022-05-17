from fileinput import filename
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse 
from django.forms.models import model_to_dict

from ..models import myUser, Follow, ArtItem, Comment, Tag
from ..serializers import myUserSerializer, ArtItemSerializer, CommentSerializer, TagSerializer
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import parser_classes
import json

import base64
from django.core.files.base import ContentFile

##### List of routes / method / action:
#
#  http://127.0.0.1:8000/api/v1/artitems                   / GET  / Return all of the art items in the system in JSON format 
#  http://127.0.0.1:8000/api/v1/artitems/<id>              / GET  / Return an art item with the given id
#  http://127.0.0.1:8000/api/v1/artitems                   / POST / create an art item
#  http://127.0.0.1:8000/api/v1/artitems/users/<id>        / GET  / get all of the art items of the specific user (by id)
#  http://127.0.0.1:8000/api/v1/artitems/users/username/<username>  / GET  / get all of the art items of the specific user (by username)
#  
import base64
from django.core.files.base import ContentFile




@api_view(["GET", "POST"])
def artitems(request):

    if(request.method == "GET"):
        artitems = ArtItem.objects.all()
        serializer = ArtItemSerializer(artitems, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    #
    # owner id must be provided.
    # list of tag ids or a single tag id must be provided.
    # So we assume that the person who consumes this API, knows necessary IDs. 
    #
    #
    # We take the input from frontend in base64 format.
    # We have to decode it and convert to a ContentFile object.
    # Then we have to assign this object to ImageField.
    #
    
    elif(request.method == "POST"):
        data = request.data.copy()

        if('tags' in data and not isinstance(data['tags'], list)): # tags must be a list
            # change 'mutable' property
            data['tags'] = [data['tags']]

        
        ### BASE64 DECODING
        # Check if artitem_image is provided. If not, default to defaultart.png. If provided, it's in base64 format. Decode it.
        if('artitem_image' in data):
            image_data= data['artitem_image'].split("base64,")[1]
            decoded = base64.b64decode(image_data)
            data['artitem_image'] = ContentFile(decoded , name='decode.png')
    
            
        ###
        serializer = ArtItemSerializer(data=data)
        if serializer.is_valid():
            if('artitem_image' in data):
                with open("media/artitem/decode.png", "wb") as fh:
                    fh.write(decoded)
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def artitems_by_id(request, id):
    try:
        artitem = ArtItem.objects.get(pk=id)
        serializer = ArtItemSerializer(artitem)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ArtItem.DoesNotExist:
        return Response({"Not Found": "Any art item with the given ID doesn't exist."}, status=status.HTTP_404_NOT_FOUND)

    

@api_view(["GET"])
def artitems_by_userid(request, id):
    try:
        myUser.objects.get(pk=id)
        artitems = ArtItem.objects.filter(owner=id)
        serializer = ArtItemSerializer(artitems, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except myUser.DoesNotExist:
        return Response({"Not Found": "Any user with the given ID doesn't exist."}, status=status.HTTP_404_NOT_FOUND)
    
# api/v1/artitems/users/username/<str:username>
@api_view(["GET"])
def artitems_by_username(request, username):

    users = myUser.objects.all()
    user = [x for x in users if x.username == username]
    if(not user):
        return Response({"Not Found": "Any user with the given username doesn't exist."}, status=status.HTTP_404_NOT_FOUND)
    else:
        artitems = ArtItem.objects.filter(owner=user[0].id)  #we know that length of user must be 1 since username is a unique field
        serializer = ArtItemSerializer(artitems, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    

  
    
