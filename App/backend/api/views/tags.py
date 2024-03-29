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
from django.contrib.auth.models import AnonymousUser


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
                    "created_at": "08-12-2022 00:38:25",
                    "updated_at": "08-12-2022 00:38:25"
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
@swagger_auto_schema(
    method='DELETE',
    operation_description="Tag delete API.",
    operation_summary="Delete tag.",
    tags=['tags'],
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Successfully deleted the tag.",
            examples={
                "application/json": {
                    "detail": "Tag deleted!"
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
        status.HTTP_400_BAD_REQUEST: openapi.Response(
            description="User not authorized.",
            examples={
                "application/json": {
                    "detail": "Invalid token."
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
            message = {'detail': 'You do not have the permission to delete an existing tag.'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='POST',
    operation_description="Tag API. This endpoint with POST request creates a tag. Moderator is required.",
    operation_summary="Create a new tag.",
    tags=['tags'],
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Successfully created a tag.",
            examples={
                "application/json": {
                    "id": 1,
                    "tagname": "ocean",
                    "description": "test",
                    "created_at": "08-12-2022 00:38:25",
                    "updated_at": "08-12-2022 00:38:25"
                }
            }
        ),
        status.HTTP_400_BAD_REQUEST: openapi.Response(
            description="Invalid parameters or token.",
            examples={
                "application/json": {
                    
                },
            }
        ),
    }
)
@swagger_auto_schema(
    method='GET',
    operation_description="Tag API. This endpoint with GET request returns all tags in the db. Authentication is not required.",
    operation_summary="Get all tags",
    tags=['tags'],
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Successfully got all tags.",
            examples={
                "application/json": {
                    "id": 1,
                    "tagname": "ocean",
                    "description": "test",
                    "created_at": "08-12-2022 00:38:25",
                    "updated_at": "08-12-2022 00:38:25"
                }
            }
        ),
        status.HTTP_400_BAD_REQUEST: openapi.Response(
            description="Bad request.",
            examples={
                "application/json": {
                    "detail": "Bad request."
                },
            }
        ),
    }
)
@api_view(['POST', 'GET'])
def TagsView(request):
    data = request.data
    if (request.method == "POST"):
        if(isinstance(request.user, AnonymousUser)):
            message = {'Invalid request': 'Guest users cannot create tags.'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        if request.user.is_level2 or request.user.is_superuser:
            serializer = TagSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            message = {'detail': 'Invalid token.'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
    elif(request.method == "GET"):
        try:
            tags = Tag.objects.all()
            serializer = TagSerializer(tags, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Tag.DoesNotExist:
            message = {
                'detail': 'Bad request.'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)