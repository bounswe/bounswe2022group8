import imp
from unicodedata import name
from django.http import HttpResponse, JsonResponse
from ..models import ArtItem, Tag #do I need Tag
from ..serializers import ArtItemSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status





@api_view(['GET'])
def search_by_tag_keyword(request, tag, format=None):

    tagObjects = Tag.objects.filter(tagname__contains=tag)

    if not tagObjects:
        return Response({"Not Found:", "No such tag exists."}, status=status.HTTP_404_NOT_FOUND) 
    elif request.method == 'GET':
        artitems = set()
        for tag in tagObjects:
            myset = tag.artitem_set.all()
            for element in myset:
                artitems.add(element)

        if not artitems:
            return Response({"Not Found:", "There is no art item associated with the tag you are looking for."}, status=status.HTTP_204_NO_CONTENT) 
        
        serializer = ArtItemSerializer(list(artitems), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def search_by_tag(request, tag, format=None):

    try:
        tagObject = Tag.objects.get(tagname=tag)
    except Tag.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)    


    if request.method == 'GET':
        items= tagObject.artitem_set.all()
        # items = ArtItem.objects.all()
        serializer = ArtItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
