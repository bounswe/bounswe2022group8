from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..serializers.serializers import TagSerializer
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from ..models.user import User
from ..models.artitem import Tag
from django.contrib.auth.decorators import login_required
from django.core import serializers


@swagger_auto_schema(
    method='GET',
    operation_description="Tag API. This endpoint with GET request returns a specific tag. Authentication is not required.",
    operation_summary="Get single tag.",
    tags=['tags'],
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Successfully got the tag.",
            examples={
                "application/json": {
                    "id": 1,
                    "tagname": "ocean",
                    "description": "test",
                    "created_at": "2022-11-13T16:34:03.316236Z",
                    "updated_at": "2022-11-13T16:34:03.316236Z"
                }
            }
        ),
        status.HTTP_404_NOT_FOUND: openapi.Response(
            description="Wrong tag id.",
            examples={
                "application/json": {
                    "detail": "Tag with given id does not exist."
                },
            }
        ),
    }
)
@api_view(['GET', 'DELETE'])
def TagView(request, id):
    data = request.data
    if (request.method == "GET"):
        try:
            tag = Tag.objects.get(id=id)
            serializer = TagSerializer(tag)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Tag.DoesNotExist:
            message = {
                'detail': 'Tag with given id does not exist.'}
            return Response(message, status=status.HTTP_404_NOT_FOUND)
    elif(request.method == "DELETE"):
        if request.user.is_superuser:
            try:
                tag = Tag.objects.get(id=id)
            except Tag.DoesNotExist:
                message = {
                    'detail': 'Tag with given id does not exist.'}
                return Response(message, status=status.HTTP_404_NOT_FOUND)
            tag.delete()
            message = {
                'detail': 'Tag deleted!'}
            return Response(message, status=status.HTTP_200_OK)
        else:
            message = {'detail': 'Invalid token.'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def TagsView(request):
    data = request.data
    if (request.method == "POST"):
        if request.user.is_superuser:
            serializer = TagSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            message = {'detail': 'Invalid token.'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
    