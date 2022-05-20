from http import HTTPStatus
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse 
from rest_framework.decorators import api_view
from api.models import Comment,ArtItem,myUser
from api.serializers import CommentSerializer
from rest_framework.response import Response
from rest_framework import status

# To view comments of an art item and to comment on an art item
@api_view(['GET','POST'])
def commentsOfArtItem(request,id):    # id is art item's id
    try:
        artitem = ArtItem.objects.get(pk=id)
    except:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':    # view comments of art item with id
        comments = Comment.objects.filter(commented_on =id)
        serializer = CommentSerializer(comments, many=True)
        return JsonResponse(serializer.data,safe=False, status=status.HTTP_200_OK)

    elif request.method=='POST':   # comment on art item with id
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# user having id in db can view or delete his/her own comment with commentid
# id is not the same as user_id stated in database. This is important to prevent confusion.
@api_view(['GET','DELETE'])
def getDeleteComment(request,commentid,id):
    try:
        comments = Comment.objects.filter(commented_by = id)  # this prevents to change other users' comments.
        comment = comments.get(pk=commentid)
    except:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':    # view comment with commentid
        serializer = CommentSerializer(comment)
        return JsonResponse(serializer.data,safe=False, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':   # delete comment with commentid
        comment.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
