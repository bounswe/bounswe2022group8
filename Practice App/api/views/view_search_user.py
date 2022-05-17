from ..models import myUser
from ..serializers import myUserSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def search_user(request, username, pk=None):
    try:
        user = myUser.objects.get(user__username=username)
    except myUser.DoesNotExist:
        return Response({"Error"}, status=status.HTTP_404_NOT_FOUND)

    serializer = myUserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)