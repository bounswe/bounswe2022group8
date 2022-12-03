from django.shortcuts import render
from rest_framework.decorators import api_view
from ..serializers.like import LikeArtItemSerializer, LikeCommentSerializer
from ..serializers.serializers import UserSerializer
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from ..models.user import User
from ..models.artitem import ArtItem, LikeArtItem
from ..models.models import Comment, LikeComment
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from knox.auth import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.db import IntegrityError

@swagger_auto_schema(
    method='POST',
    operation_description="LikeArtItem API. This endpoint with POST request like an art item with the given ID. Authentication is required.",
    operation_summary="Like an art item.",
    tags=['Like'],
    responses={
        status.HTTP_201_CREATED: openapi.Response(
            description="Successfully liked the given art item.",
            examples={
                "application/json": {
                    "id": 5,
                    "user": 2,
                    "artitem": 3,
                    "liked_at": "2022-12-02T12:02:29.414752Z"
                }
            }
        ),
        status.HTTP_404_NOT_FOUND: openapi.Response(
            description="Art item with the given id is not found.",
            examples={
                "application/json": {"Not Found": "Any art item with the given ID doesn't exist."},
            }
        ),
    }
)
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
@authentication_classes([TokenAuthentication])
def like_artitem(request, id):
    current_user = request.user
    try:
        artitem = ArtItem.objects.get(pk=id)
        like = LikeArtItem.objects.create(user=current_user, artitem=artitem)
        serializer = LikeArtItemSerializer(like)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    except ArtItem.DoesNotExist:
        return Response({"Not Found": "Any art item with the given ID doesn't exist."}, status=status.HTTP_404_NOT_FOUND)


@swagger_auto_schema(
    method='DELETE',
    operation_description="LikeArtItem API. This endpoint with DELETE request unlikes an art item with the given ID. Authentication is required.",
    operation_summary="Unlike an art item.",
    tags=['Like'],
    responses={
        status.HTTP_204_NO_CONTENT: openapi.Response(
            description="Successfully unliked the given art item.",
        ),
        status.HTTP_404_NOT_FOUND: openapi.Response(
            description="Art item with the given id is not found.",
            examples={
                "application/json": {"Not Found": "Any art item with the given ID doesn't exist."},
            }
        ),
        status.HTTP_400_BAD_REQUEST: openapi.Response(
            description="Current user have tried to unlike an art item which already is not liked by the current user.",
            examples={
                "application/json": {"Invalid request": "A user cannot unlike an art item which is not liked before."}
            }
        ),
    }
)
@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
@authentication_classes([TokenAuthentication])
def unlike_artitem(request, id):
    current_user = request.user
    try:
        artitem = ArtItem.objects.get(pk=id)
        try:
            like = LikeArtItem.objects.get(user=current_user, artitem=artitem)
            like.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except LikeArtItem.DoesNotExist:
            return Response({"Invalid request": "A user cannot unlike an art item which is not liked before."}, status=status.HTTP_400_BAD_REQUEST)
    except ArtItem.DoesNotExist:
        return Response({"Not Found": "Any art item with the given ID doesn't exist."}, status=status.HTTP_404_NOT_FOUND)

@swagger_auto_schema(
    method='GET',
    operation_description="LikeArtItem API. This endpoint with GET request fetches the art items which the user with the given ID has liked.",
    operation_summary="Get the art items which the given user has liked.",
    tags=['like'],
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Successfully returns the list of the liked art items.",
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
                        "type": "sketch",
                        "tags": [],
                        "artitem_path": "artitem/docker.jpg"
                    }
                ],
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
def get_liked_artitems_of_user(request, id):
    try:
        user = User.objects.get(pk=id)
        liked_artitems = [liked.artitem for liked in LikeArtItem.objects.filter(user=user)]
        artitems = LikeArtItemSerializer(liked_artitems, many=True)
        return Response(artitems.data, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({"Not Found": "Any user with the given ID doesn't exist."}, status=status.HTTP_404_NOT_FOUND)


@swagger_auto_schema(
    method='GET',
    operation_description="LikeArtItem API. This endpoint with GET request fetches the users who liked the art item with the given ID.",
    operation_summary="Get the users who likes the art item.",
    tags=['like'],
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Successfully returns the list of users liked the art item.",
                        examples={
                            "application/json": [
                                {
                                    "id": 2,
                                    "username": "MasmaviDeniz",
                                    "is_level2": False,
                                    "name": "",
                                    "surname": "",
                                    "email": "greg@gmail.com",
                                    "profile_path": "avatar/default.png",
                                    "created_at": "2022-11-18T11:30:11.383870Z",
                                    "updated_at": "2022-11-18T11:30:11.383870Z"
                                },
                                {
                                    "id": 6,
                                    "username": "HowShallASparrowFly",
                                    "is_level2": False,
                                    "name": "",
                                    "surname": "",
                                    "email": "ryan@outlook.com",
                                    "profile_path": "avatar/default.png",
                                    "created_at": "2022-11-18T12:37:44.598661Z",
                                    "updated_at": "2022-11-18T12:37:44.598661Z"
                                }
                            ],
                        }
        ),
        status.HTTP_404_NOT_FOUND: openapi.Response(
            description="Art item cannot be found.",
            examples={
                "application/json": {
                    "Not Found": "Any art item with the given ID does not exist."
                }
            }
        ),
    }
)
@api_view(['GET'])
def get_users_who_liked_artitem(request, id):
    try:
        artitem = ArtItem.objects.get(pk=id)
        liker_users = [liked.user for liked in LikeArtItem.objects.filter(artitem=artitem)]
        users = UserSerializer(liker_users, many=True)
        return Response(users.data, status=status.HTTP_200_OK)
    except ArtItem.DoesNotExist:
        return Response({"Not Found": "Any art item with the given ID does not exist."}, status=status.HTTP_404_NOT_FOUND)


@swagger_auto_schema(
    method='POST',
    operation_description="LikeComment API. This endpoint with POST request like a comment with the given ID. Authentication is required.",
    operation_summary="Like a comment.",
    tags=['Like'],
    responses={
        status.HTTP_201_CREATED: openapi.Response(
            description="Successfully liked the given comment.",
            examples={
                "application/json": {
                    "id": 5,
                    "user": 2,
                    "comment": 3,
                    "liked_at": "2022-12-02T12:02:29.414752Z"
                }
            }
        ),
        status.HTTP_404_NOT_FOUND: openapi.Response(
            description="Comment with the given id is not found.",
            examples={
                "application/json": {"Not Found": "Any comment with the given ID doesn't exist."},
            }
        ),
    }
)
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
@authentication_classes([TokenAuthentication])
def like_comment(request, id):
    current_user = request.user
    try:
        comment = Comment.objects.get(pk=id)
        like = LikeComment.objects.create(user=current_user, comment=comment)
        serializer = LikeCommentSerializer(like)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    except Comment.DoesNotExist:
        return Response({"Not Found": "Any comment with the given ID doesn't exist."}, status=status.HTTP_404_NOT_FOUND)


@swagger_auto_schema(
    method='DELETE',
    operation_description="LikeComment API. This endpoint with DELETE request unlikes a comment with the given ID. Authentication is required.",
    operation_summary="Unlike a comment which is liked before by the user.",
    tags=['Like'],
    responses={
        status.HTTP_204_NO_CONTENT: openapi.Response(
            description="Successfully unliked the given comment.",
        ),
        status.HTTP_404_NOT_FOUND: openapi.Response(
            description="Comment with the given id is not found.",
            examples={
                "application/json": {"Not Found": "Any comment with the given ID does not exist."},
            }
        ),
        status.HTTP_400_BAD_REQUEST: openapi.Response(
            description="Current user have tried to unlike a comment which already is not liked by the current user.",
            examples={
                "application/json": {"Invalid request": "A user cannot unlike a comment which is not liked before."}
            }
        ),
    }
)
@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
@authentication_classes([TokenAuthentication])
def unlike_comment(request, id):
    current_user = request.user
    try:
        comment = Comment.objects.get(pk=id)
        try:
            like = LikeComment.objects.get(user=current_user, comment=comment)
            like.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except LikeComment.DoesNotExist:
            return Response({"Invalid request": "A user cannot unlike a comment which is not liked before by the user."}, status=status.HTTP_400_BAD_REQUEST)
    except Comment.DoesNotExist:
        return Response({"Not Found": "Any comment with the given ID doesn't exist."}, status=status.HTTP_404_NOT_FOUND)


@swagger_auto_schema(
    method='GET',
    operation_description="LikeComment API. This endpoint with GET request fetches the users who liked the comment with the given ID.",
    operation_summary="Get the users who likes the comment.",
    tags=['like'],
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Successfully returns the list of users liked the comment.",
                        examples={
                            "application/json": [
                                {
                                    "id": 2,
                                    "username": "MasmaviDeniz",
                                    "is_level2": False,
                                    "name": "",
                                    "surname": "",
                                    "email": "greg@gmail.com",
                                    "profile_path": "avatar/default.png",
                                    "created_at": "2022-11-18T11:30:11.383870Z",
                                    "updated_at": "2022-11-18T11:30:11.383870Z"
                                },
                                {
                                    "id": 6,
                                    "username": "HowShallASparrowFly",
                                    "is_level2": False,
                                    "name": "",
                                    "surname": "",
                                    "email": "ryan@outlook.com",
                                    "profile_path": "avatar/default.png",
                                    "created_at": "2022-11-18T12:37:44.598661Z",
                                    "updated_at": "2022-11-18T12:37:44.598661Z"
                                }
                            ],
                        }
        ),
        status.HTTP_404_NOT_FOUND: openapi.Response(
            description="Comment cannot be found.",
            examples={
                "application/json": {
                    "Not Found": "Any comment with the given ID does not exist."
                }
            }
        ),
    }
)
@api_view(['GET'])
def get_users_who_liked_comment(request, id):
    try:
        comment = Comment.objects.get(pk=id)
        liker_users = [liked.user for liked in LikeComment.objects.filter(comment=comment)]
        users = UserSerializer(liker_users, many=True)
        return Response(users.data, status=status.HTTP_200_OK)
    except Comment.DoesNotExist:
        return Response({"Not Found": "Any comment with the given ID does not exist."}, status=status.HTTP_404_NOT_FOUND)