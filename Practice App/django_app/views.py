from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import JsonResponse 

# Don't create your views here. We decided to use urls.py in api folder. 

def index(request):
    return redirect('api/')