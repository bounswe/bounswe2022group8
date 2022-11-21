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
from ..models.models import Comment, ArtItem
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
@api_view(['GET', 'PUT', 'DELETE'])
def TagView(request, artitemid, id):
    pass