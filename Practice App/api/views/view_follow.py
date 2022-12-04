import re
from django.http import HttpResponse, JsonResponse
from ..models import myUser, Follow 
from ..serializers import FollowSerializer, myUserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def follow_user(request):
    serializer = FollowSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_followers(request, id):
    try:
        user = myUser.objects.get(pk=id)
    except myUser.DoesNotExist:
        return Response({"Not Found:", "Any user with the given ID doesn't exist."}, status=status.HTTP_404_NOT_FOUND)
    followers = myUserSerializer(user.follower.all(), many=True)
    return Response(data=followers.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_followings(request, id):
    try:
        user = myUser.objects.get(pk=id)
    except myUser.DoesNotExist:
        return Response({"Not Found:", "Any user with the given ID doesn't exist."}, status=status.HTTP_404_NOT_FOUND)
    
    all_users = myUser.objects.all()
    following_users = [x for x in all_users if user in x.follower.all()]
    followings = myUserSerializer(following_users, many=True)
    return Response(data=followings.data, status=status.HTTP_200_OK)



