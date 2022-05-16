import imp
from unicodedata import name
from django.http import HttpResponse, JsonResponse
from ..models import ArtItem, Tag #do I need Tag
from ..serializers import ArtItemSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status





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
