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

# user having id in db can view, delete or edit his/her own comment with commentid
# id is not the same as user_id stated in database. This is important to prevent confusion.
@api_view(['GET','DELETE','PUT'])
def editComment(request,commentid,id):
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
    
    elif request.method == 'PUT':  # edit comment with commentid
        data = request.data
        data['commented_by'] = id   
        data['commented_on'] = comment.commented_on.id
        # 3 lines up to here is to run put funtion without giving value for 'commented_by' and 'commented_on' while editing.
        # Giving body is enough for testing.
        # This also provides to prevent user to change 'commented_by' and 'commented_on', which causes problem.
        serializer = CommentSerializer(comment,data)
        if(serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
