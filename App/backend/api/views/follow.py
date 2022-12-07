from django.shortcuts import render
from rest_framework.decorators import api_view
from ..serializers.follow import FollowSerializer
from ..serializers.serializers import UserSerializer
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from ..models.user import User
from ..models.user import Follow
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
    operation_description="Follow API. This endpoint with POST request follows a user with the given ID. Authentication is required.",
    operation_summary="Follow a user.",
    tags=['follow'],
    responses={
        status.HTTP_201_CREATED: openapi.Response(
            description="Successfully started following the given user.",
            examples={
                "application/json": {
                    "id": 5,
                    "from_user": 2,
                    "to_user": 3,
                    "created_at": "2022-11-18T12:02:29.414752Z"
                }
            }
        ),
        status.HTTP_404_NOT_FOUND: openapi.Response(
            description="User with the given id is not found.",
            examples={
                "application/json": {"Not Found": "Any user with the given ID doesn't exist."},
            }
        ),
        status.HTTP_400_BAD_REQUEST: openapi.Response(
            description="Bad Request is raised when a user attempts to follow himself or attempts to follow someone whom he's already following.",
            examples={
                "application/json": {"Invalid request": "A user cannot follow himself."}
            }
        ),
    }
)
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
@authentication_classes([TokenAuthentication])
def follow_user(request, id):
    current_user = request.user
    try:
        user = User.objects.get(pk=id)
        if (current_user.id != user.id):
            try:
                follow = Follow.objects.create(
                    from_user=current_user, to_user=user)
                serializer = FollowSerializer(follow)
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response({"Invalid request": "Current user already follows the given user."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Invalid request": "A user cannot follow himself."}, status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        return Response({"Not Found": "Any user with the given ID doesn't exist."}, status=status.HTTP_404_NOT_FOUND)


@swagger_auto_schema(
    method='DELETE',
    operation_description="Follow API. This endpoint with DELETE request unfollows a user with the given ID. Authentication is required.",
    operation_summary="Unfollow a user.",
    tags=['follow'],
    responses={
        status.HTTP_204_NO_CONTENT: openapi.Response(
            description="Successfully unfollowed the given user.",
        ),
        status.HTTP_404_NOT_FOUND: openapi.Response(
            description="User with the given id is not found.",
            examples={
                "application/json": {"Not Found": "Any user with the given ID doesn't exist."},
            }
        ),
        status.HTTP_400_BAD_REQUEST: openapi.Response(
            description="Bad Request is raised when a user attempts to unfollow himself or attempts to unfollow someone whom he's not following.",
            examples={
                "application/json": {"Invalid request": "A user cannot unfollow himself."}
            }
        ),
    }
)
@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
@authentication_classes([TokenAuthentication])
def unfollow_user(request, id):
    current_user = request.user
    try:
        user = User.objects.get(pk=id)
        if (current_user.id != user.id):
            try:
                follow = Follow.objects.get(
                    from_user=current_user, to_user=user)
                follow.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Follow.DoesNotExist:
                return Response({"Invalid request": "Current user doesn't follow the given user."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Invalid request": "A user cannot unfollow himself."}, status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        return Response({"Not Found": "Any user with the given ID doesn't exist."}, status=status.HTTP_404_NOT_FOUND)


@swagger_auto_schema(
    method='GET',
    operation_description="Follow API. This endpoint with GET request fetches the followers of the currently logged-in user. Authentication is required.",
    operation_summary="Get the followers.",
    tags=['follow'],
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Successfully returns the list of followers.",
                        examples={
                            "application/json": [
                                {
                                    "id": 6,
                                    "username": "HowShallASparrowFly",
                                    "is_level2": False,
                                    "name": "",
                                    "surname": "",
                                    "email": "ryan@outlook.com",
                                    "profile_path": "avatar/default.png",
                                    "created_at": "08-12-2022 00:38:25",
                                    "updated_at": "08-12-2022 00:38:25"
                                },
                                {
                                    "id": 5,
                                    "username": "Hallelujah",
                                    "is_level2": False,
                                    "name": "",
                                    "surname": "",
                                    "email": "cohen@hotmail.com",
                                    "profile_path": "avatar/default.png",
                                    "created_at": "08-12-2022 00:38:25",
                                    "updated_at": "08-12-2022 00:38:25"
                                }
                            ],
                        }
        ),
    }
)
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
@authentication_classes([TokenAuthentication])
def get_my_followers(request):
    current_user = request.user
    followers = [follow.from_user for follow in Follow.objects.filter(
        to_user=current_user)]
    users = UserSerializer(followers, many=True)
    return Response(users.data, status=status.HTTP_200_OK)


@swagger_auto_schema(
    method='GET',
    operation_description="Follow API. This endpoint with GET request fetches the users followed by the currently logged-in user. Authentication is required.",
    operation_summary="Get the followed users.",
    tags=['follow'],
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Successfully returns the list of followers.",
                        examples={
                            "application/json": [
                                {
                                    "id": 9,
                                    "username": "till_i_collapse",
                                    "is_level2": False,
                                    "name": "",
                                    "surname": "",
                                    "email": "till@outlook.com",
                                    "profile_path": "avatar/default.png",
                                    "created_at": "08-12-2022 00:38:25",
                                    "updated_at": "08-12-2022 00:38:25"
                                },
                                {
                                    "id": 10,
                                    "username": "lose_yourself",
                                    "is_level2": False,
                                    "name": "",
                                    "surname": "",
                                    "email": "lostButWon@princeton.edu",
                                    "profile_path": "avatar/default.png",
                                    "created_at": "08-12-2022 00:38:25",
                                    "updated_at": "08-12-2022 00:38:25"
                                },
                                {
                                    "id": 5,
                                    "username": "Hallelujah",
                                    "is_level2": False,
                                    "name": "",
                                    "surname": "",
                                    "email": "cohen@hotmail.com",
                                    "profile_path": "avatar/default.png",
                                    "created_at": "08-12-2022 00:38:25",
                                    "updated_at": "08-12-2022 00:38:25"
                                }
                            ],
                        }
        ),
    }
)
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
@authentication_classes([TokenAuthentication])
def get_my_followings(request):
    current_user = request.user
    followings = [follow.to_user for follow in Follow.objects.filter(
        from_user=current_user)]
    users = UserSerializer(followings, many=True)
    return Response(users.data, status=status.HTTP_200_OK)


@swagger_auto_schema(
    method='GET',
    operation_description="Follow API. This endpoint with GET request fetches the followers of the user with the given ID.",
    operation_summary="Get the followers of the given user.",
    tags=['follow'],
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Successfully returns the list of followers.",
                        examples={
                            "application/json": [
                                {
                                    "id": 6,
                                    "username": "HowShallASparrowFly",
                                    "is_level2": False,
                                    "name": "",
                                    "surname": "",
                                    "email": "ryan@outlook.com",
                                    "profile_path": "avatar/default.png",
                                    "created_at": "08-12-2022 00:38:25",
                                    "updated_at": "08-12-2022 00:38:25"
                                },
                                {
                                    "id": 5,
                                    "username": "Hallelujah",
                                    "is_level2": False,
                                    "name": "",
                                    "surname": "",
                                    "email": "cohen@hotmail.com",
                                    "profile_path": "avatar/default.png",
                                    "created_at": "08-12-2022 00:38:25",
                                    "updated_at": "08-12-2022 00:38:25"
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
def get_followers(request, id):
    try:
        to_user = User.objects.get(pk=id)
        followers = [follow.from_user for follow in Follow.objects.filter(
            to_user=to_user)]
        users = UserSerializer(followers, many=True)
        return Response(users.data, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({"Not Found": "Any user with the given ID doesn't exist."}, status=status.HTTP_404_NOT_FOUND)


@swagger_auto_schema(
    method='GET',
    operation_description="Follow API. This endpoint with GET request fetches the users followed by the user with the given ID.",
    operation_summary="Get the users followed by the given user.",
    tags=['follow'],
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Successfully returns the list of followers.",
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
                                    "created_at": "08-12-2022 00:38:25",
                                    "updated_at": "08-12-2022 00:38:25"
                                },
                                {
                                    "id": 6,
                                    "username": "HowShallASparrowFly",
                                    "is_level2": False,
                                    "name": "",
                                    "surname": "",
                                    "email": "ryan@outlook.com",
                                    "profile_path": "avatar/default.png",
                                    "created_at": "08-12-2022 00:38:25",
                                    "updated_at": "08-12-2022 00:38:25"
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
def get_followings(request, id):
    try:
        from_user = User.objects.get(pk=id)
        followings = [follow.to_user for follow in Follow.objects.filter(
            from_user=from_user)]
        users = UserSerializer(followings, many=True)
        return Response(users.data, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({"Not Found": "Any user with the given ID doesn't exist."}, status=status.HTTP_404_NOT_FOUND)
