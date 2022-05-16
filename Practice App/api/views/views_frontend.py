from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse 
from django.forms.models import model_to_dict
from urllib3 import HTTPResponse


from .view_artitems import *

# Using HttpResponse for debug, we should use JsonResponse
# since this is a REST API project.

#  http://127.0.0.1:8000  = homepage
#  http://127.0.0.1:8000/gallery  = gallery
#
#
#


# http://127.0.0.1:8000
def home(request):
    return render(request, "index.html")


# http://127.0.0.1:8000/gallery
def gallery(request):
    return render(request, "artitems.html")