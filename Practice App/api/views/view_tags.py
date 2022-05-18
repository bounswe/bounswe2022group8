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

@api_view(["GET", "POST"])
def tags(request):
    
    if(request.method == "GET"):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    