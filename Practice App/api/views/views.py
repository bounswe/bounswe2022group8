from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse 

# Create your views here.

# Using HttpResponse for debug, we should use JsonResponse
# since this is a REST API project.

def home(request):
    return HttpResponse("<h1>Practice App Home</h1>")

def about(request):
    return HttpResponse("<h1>About Section</h1>")

def api_home(request): 
    data = {}
    data['params'] = dict(request.GET)  # query parameters
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)