from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

from ..serializers.profile import UserProfileSerializer

from ..models.user import User
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view, permission_classes
from drf_yasg import openapi


# http://${host}:8000/api/v1/profile/users  : Return all the users in the system   

@ swagger_auto_schema(
    method='get',
    operation_description="Returns all the users in the system with their profile information",
    operation_summary="Get all users in the system.",
    tags=['profile'],
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Successfully retrieved the users.",
            examples={
                "application/json": [{
                    "username": "pothepanda",
                    "email": "po@jade.edu",
                    "location": "China",
                    "name": "Po",
                    "surname": "Ping",
                    "about": """The foretold Dragon Warrior of legend, a master of the Panda Style of Kung Fu, noodle lover and an art enthusiast.""",
                    "profile_path": "avatar/default.png",
                    "is_level2": False,
                    "followers": 3,
                    "followings": 2
                }]
            }
        )
    }
)
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def users_api(request):
    if (request.method == "GET"):
        user = User.objects.all()
        serializer = UserProfileSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({"detail": "Method \"{}\" not allowed.".format(request.method)})
