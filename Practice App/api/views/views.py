from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse 
from django.forms.models import model_to_dict

from ..models import myUser, Follow, ArtItem, Comment, Tag
from ..serializers import myUserSerializer, ArtItemSerializer, CommentSerializer, TagSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


# Create your views here.

# Using HttpResponse for debug, we should use JsonResponse
# since this is a REST API project.

@api_view(["GET"])
def home(request):
    return render(request, 'index/index.html')
#    return HttpResponse("<h1>Practice App Home</h1>") # returns a Http page

@api_view(["GET"])
def about(request):
    return HttpResponse("<h1>About Section</h1>")

@api_view(["GET"])
def api(request): 
    model_data = myUser.objects.all().order_by("?").first()
    data = {}
    if model_data:
        serializer = myUserSerializer(model_data)

    # pure JSON format 
    JSON = JSONRenderer().render(serializer.data)

    # we need to give serializer.data to the Response
    return Response(serializer.data)

