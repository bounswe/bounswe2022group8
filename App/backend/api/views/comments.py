from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..serializers.serializers import CommentSerializer
from ..serializers.comments import commentsPostSerializer, commentUpdateSerializer
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from ..models.user import User
from ..models.models import Comment, ArtItem, LikeComment
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.contrib.auth.models import AnonymousUser



@swagger_auto_schema(
    method='GET',
    operation_description="Comment API. This endpoint with GET request returns a specific comment. Authentication is not required.",
    operation_summary="Get single comment.",
    tags=['comments'],
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Successfully got the comment.",
            examples={
                "application/json": {
                    "id": 3,
                    "body": "Third comment",
                    "parent": 2,
                    "commented_by": {
                        "id": 1,
                        "username": "zamasssnla",
                        "profile_path": "avatar/default.png"
                    },
                    "commented_on": 1,
                    "created_at": "08-12-2022 00:38:25",
                    "lft": 3,
                    "rght": 4,
                    "tree_id": 1,
                    "level": 2
                }
            }
        ),
        status.HTTP_404_NOT_FOUND: openapi.Response(
            description="Wrong comment id.",
            examples={
                "application/json": {
                    "detail": "Comment with given id does not exist."
                },
            }
        ),
    }
)
@swagger_auto_schema(
    method='PUT',
    request_body=commentUpdateSerializer,
    operation_description="Comment API. This endpoint with PUT request updates the body of a specific comment. Authentication is required.",
    operation_summary="Update comment.",
    tags=['comments'],
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Successfully updated the comment.",
            examples={
                "application/json": {
                    "id": 10,
                    "body": "comment update body",
                    "parent": 4,
                    "commented_by": {
                        "id": 1,
                        "username": "zamasssnla",
                        "profile_path": "avatar/default.png"
                    },
                    "commented_on": 1,
                    "created_at": "08-12-2022 00:38:25",
                    "lft": 6,
                    "rght": 7,
                    "tree_id": 1,
                    "level": 3
                }
            }
        ),
        status.HTTP_404_NOT_FOUND: openapi.Response(
            description="Wrong comment id.",
            examples={
                "application/json": {
                    "detail": "Comment with given id does not exist."
                },
            }
        ),
        status.HTTP_400_BAD_REQUEST: openapi.Response(
            description="User not authorized.",
            examples={
                "application/json": {
                    "detail": "This comment is not posted by you."
                },
            }
        ),
    }
)
@swagger_auto_schema(
    method='DELETE',
    operation_description="Comment API. This endpoint with DELETE request updates the body of a specific comment. Authentication is required.",
    operation_summary="Delete comment.",
    tags=['comments'],
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Successfully deleted the comment.",
            examples={
                "application/json": {
                    "detail": "Comment deleted!"
                }
            }
        ),
        status.HTTP_404_NOT_FOUND: openapi.Response(
            description="Wrong comment id.",
            examples={
                "application/json": {
                    "detail": "Comment with given id does not exist."
                },
            }
        ),
        status.HTTP_400_BAD_REQUEST: openapi.Response(
            description="User not authorized.",
            examples={
                "application/json": {
                    "detail": "This comment is not posted by you."
                },
            }
        ),
    }
)
@api_view(['GET', 'PUT', 'DELETE'])
def CommentView(request, artitemid, id):
    data = request.data
    if (request.method == "GET"):
        try:
            comment = Comment.objects.get(id=id)
            serializer = CommentSerializer(comment)
            return Response(serializer, status=status.HTTP_200_OK)
        except Comment.DoesNotExist:
            message = {
                'detail': 'Comment with given id does not exist.'}
            return Response(message, status=status.HTTP_404_NOT_FOUND)
    elif (request.method == "PUT"):
        if request.user.is_authenticated:
            try:
                comment = Comment.objects.get(id=id)
            except Comment.DoesNotExist:
                message = {
                    'detail': 'Comment with given id does not exist.'}
                return Response(message, status=status.HTTP_404_NOT_FOUND)
            u = request.user
            if (comment.commented_by == u):
                mydata = {
                    'body': data['body']
                }
                serializer = CommentSerializer(
                    instance=comment, data=mydata, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                message = {
                    'detail': 'This comment is not posted by you.'}
                return Response(message, status=status.HTTP_400_BAD_REQUEST)
        else:
            message = {'detail': 'Invalid token.'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

    elif (request.method == "DELETE"):
        if request.user.is_authenticated:
            try:
                comment = Comment.objects.get(id=id)
            except Comment.DoesNotExist:
                message = {
                    'detail': 'Comment with given id does not exist.'}
                return Response(message, status=status.HTTP_404_NOT_FOUND)
            u = request.user
            if (comment.commented_by == u):
                comment.delete()
                message = {
                    'detail': 'Comment deleted!'}
                return Response(message, status=status.HTTP_200_OK)
            else:
                message = {
                    'detail': 'This comment is not posted by you.'}
                return Response(message, status=status.HTTP_400_BAD_REQUEST)
        else:
            message = {'detail': 'Invalid token.'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
# do we want nonregistered users to see comments???
# Condition to keep parent ArtItem the same


@swagger_auto_schema(
    method='POST',
    request_body=commentsPostSerializer,
    operation_description="Comments API. This endpoint with POST request creates a comment on an art item. Authentication is required.",
    operation_summary="Post new comment.",
    tags=['comments'],
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Successfully posted a comment.",
            examples={
                "application/json": {
                    "id": 11,
                    "body": "comment body",
                    "parent": 4,
                    "commented_by": {
                        "id": 1,
                        "username": "zamasssnla",
                        "profile_path": "avatar/default.png"
                    },
                    "commented_on": 1,
                    "created_at": "08-12-2022 00:38:25",
                    "lft": 1,
                    "rght": 2,
                    "tree_id": 6,
                    "level": 0
                }
            }
        ),
        status.HTTP_400_BAD_REQUEST: openapi.Response(
            description="Invalid parameters.",
            examples={
                "application/json": {
                    "parent": [
                        "Invalid pk \"100\" - object does not exist."
                    ]
                },
            }
        ),
    }
)
@swagger_auto_schema(
    method='GET',
    operation_description="Comments API. This endpoint with GET request return all of the comments on an art item. Authentication is not required.",
    operation_summary="Get Art Item comments.",
    tags=['comments'],
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Successfully got the comments.",
            examples={
                "application/json": {
                    "data": [
                        {
                            "id": 1,
                            "body": "first comment",
                            # "parent": null,
                            "commented_by": {
                                "id": 1,
                                "username": "zamasssnla",
                                "profile_path": "avatar/default.png"
                            },
                            "commented_on": 1,
                            "created_at": "08-12-2022 00:38:25",
                            "lft": 1,
                            "rght": 10,
                            "tree_id": 1,
                            "level": 0
                        },
                        {
                            "id": 2,
                            "body": "first reply",
                            "parent": 1,
                            "commented_by": {
                                "id": 1,
                                "username": "zamasssnla",
                                "profile_path": "avatar/default.png"
                            },
                            "commented_on": 1,
                            "created_at": "08-12-2022 00:38:25",
                            "lft": 2,
                            "rght": 9,
                            "tree_id": 1,
                            "level": 1
                        },
                        {
                            "id": 3,
                            "body": "Third comment",
                            "parent": 2,
                            "commented_by": {
                                "id": 1,
                                "username": "zamasssnla",
                                "profile_path": "avatar/default.png"
                            },
                            "commented_on": 1,
                            "created_at": "08-12-2022 00:38:25",
                            "lft": 3,
                            "rght": 4,
                            "tree_id": 1,
                            "level": 2
                        }
                    ]
                },
            }
        ),
        status.HTTP_404_NOT_FOUND: openapi.Response(
            description="Artitem ID is not found.",
            examples={
                "application/json": {
                    "Not Found": "Requested art item with the given ID is not found."
                },
            }
        ),
    }
)
@api_view(['POST', 'GET'])
def CommentsView(request, artitemid):
    data = request.data
    if (request.method == "POST"):
        if request.user.is_authenticated:
            data["commented_by"] = request.user.id
            data["commented_on"] = artitemid
            serializer = CommentSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                # catch serializer integrity error
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            message = {'detail': 'Invalid token.'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
    if (request.method == "GET"):
        try:
            artitem = ArtItem.objects.get(id=artitemid)
        except:
            return Response({"Not Found": "Requested art item with the given ID is not found."}, status=status.HTTP_404_NOT_FOUND)

        comments = Comment.objects._mptt_filter(commented_on=artitem)
        # check
        comments_json = serializers.serialize('json', comments)
        serializer = CommentSerializer(comments, many=True)
        resp = {"data": serializer.data}
        return Response(resp, status=status.HTTP_200_OK)
