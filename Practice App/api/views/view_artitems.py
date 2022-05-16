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


##### List of routes / method / action:
#
#  http://127.0.0.1:8000/api/v1/artitems                   / GET  / Return all of the art items in the system in JSON format 
#  http://127.0.0.1:8000/api/v1/artitems/<id>              / GET  / Return an art item with the given id
#  http://127.0.0.1:8000/api/v1/artitems                   / POST / create an art item
#  http://127.0.0.1:8000/api/v1/artitems/users/<id>        / GET  / get all of the art items of the specific user (by id)
#  http://127.0.0.1:8000/api/v1/artitems/users/<username>  / GET  / get all of the art items of the specific user (by username)
#  



@api_view(["GET", "POST"])
@parser_classes((MultiPartParser, ))
def artitems(request):

    if(request.method == "GET"):
        artitems = ArtItem.objects.all()
        serializer = ArtItemSerializer(artitems, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    # multipart/form-data
    elif(request.method == "POST"):
        if('data' not in request.data or 'artitem_image' not in request.FILES):
             return Response({"error": "Please rename the multipart form-data. Key of the image must be named as 'artitem_image' and key of the json data must be named as 'data'."}, status=status.HTTP_400_BAD_REQUEST)
        data = json.loads(request.data['data'])   # raw data
        file = request.FILES['artitem_image']     # file

        if('tags' in data and not isinstance(data['tags'], list)): # tags must be a list
            data['tags'] = [data['tags']]
        
        data['artitem_image'] = file
        print(data)
        serializer = ArtItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PATCH", "DELETE"])
def artitems_by_id(request, id):
    try:
        artitem = ArtItem.objects.get(pk=id)
    except ArtItem.DoesNotExist:
        return Response({"Not Found:", "Any art item with the given ID doesn't exist."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ArtItemSerializer(artitem)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PATCH":
        serializer = ArtItemSerializer(artitem, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(["GET"])
def artitems_by_userid(request, id):
    try:
        myUser.objects.get(pk=id)
        artitems = ArtItem.objects.filter(owner=id)
        serializer = ArtItemSerializer(artitems, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except myUser.DoesNotExist:
        return Response({"Not Found:", "Any user with the given ID doesn't exist."}, status=status.HTTP_404_NOT_FOUND)
    

@api_view(["GET"])
def artitems_by_username(request, username):

    users = myUser.objects.all()
    user = [x for x in users if x.username == username]
    if(not user):
        return Response({"Not Found:", "Any user with the given username doesn't exist."}, status=status.HTTP_404_NOT_FOUND)
    else:
        artitems = ArtItem.objects.filter(owner=user[0].id)  #we know that length of user must be 1 since username is a unique field
        serializer = ArtItemSerializer(artitems, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    

  
    
