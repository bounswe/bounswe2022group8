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
#  http://127.0.0.1:8000/api/v1/users                   /  GET    / Return all of the non-admin users in the system in JSON format 
#  http://127.0.0.1:8000/api/v1/users/<id>              /  GET    / Return a user with the given id
#  http://127.0.0.1:8000/api/v1/users/<id>              /  PATCH  / Update a user with the given id
#  http://127.0.0.1:8000/api/v1/users/<id>              /  DELETE / Delete a user with the given id

@api_view(["GET"])
def users(request):
    myusers = myUser.objects.all()
    serializer = myUserSerializer(myusers, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



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





