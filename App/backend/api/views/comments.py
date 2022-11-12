from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..serializers.serializers import CommentSerializer
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from ..models.user import User
from ..models.models import Comment, ArtItem
from django.contrib.auth.decorators import login_required
from django.core import serializers


@api_view(['GET','PUT','DELETE'])
@login_required
def CommentView(request, artitemid, id):
    data = request.data
    if (request.method == "GET"):
        try:
            comment = Comment.objects.get(id=id)
            serializer = CommentSerializer(comment)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Comment.DoesNotExist:
            message = {
                'detail': 'Comment with given id does not exist.'}
            return Response(message, status=status.HTTP_404_NOT_FOUND)
    elif(request.method == "PUT"):
        try:
            comment = Comment.objects.get(id=id)
        except Comment.DoesNotExist:
            message = {
                'detail': 'Comment with given id does not exist.'}
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        u = request.user
        if(comment.commented_by == u):
            mydata = {
                'body': data['body']
            }
            serializer = CommentSerializer(instance = comment, data=mydata, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            message = {
                'detail': 'This comment is not posted by you.'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
    elif(request.method == "DELETE"):
        try:
            comment = Comment.objects.get(id=id)
        except Comment.DoesNotExist:
            message = {
                'detail': 'Comment with given id does not exist.'}
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        u = request.user
        if(comment.commented_by == u):
            comment.delete()
            message = {
                'detail': 'Comment deleted!'}
            return Response(message, status=status.HTTP_200_OK)
        else:
            message = {
                'detail': 'This comment is not posted by you.'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

#do we want nonregistered users to see comments???
@api_view(['POST', 'GET'])
@login_required
def CommentsView(request, id):
    data = request.data
    if(request.method == "POST"):
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            #catch serializer integrity error 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if(request.method == "GET"):
        artitem = ArtItem.objects.get(id=id)
        comments = Comment.objects._mptt_filter(commented_on=artitem)
        #check
        comments_json = serializers.serialize('json', comments)
        serializer = CommentSerializer(comments, many=True)
        print(comments_json)
        return Response(serializer.data, status=status.HTTP_200_OK)
