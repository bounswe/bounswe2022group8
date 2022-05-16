# Don't create your views here. We decided to use urls.py in api folder. 

import urllib.parse
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import TagForm
import urllib.parse
import requests
import json

#@api_view(['GET', 'POST'])
def formview(request): #should it get tag
    if request.POST:
        form = TagForm(request.POST)
        print(request.POST)
        tag=request.POST["tag"]
        #print("here")
        #print(tag)
        if form.is_valid():        
            #encoded = urllib.parse.quote(str(tag))
            #print(encoded)
            #print(encoded)
            return redirect('search_by_tag', tag=tag) #Redirect to search_by_tag page
            #response = request.get('http://127.0.0.1:8000/api/searchbytag/{encoded}')


    return render(request, 'tagform/tagform.html', {'form':TagForm()}) #import render
    #return HttpResponse("why though")

# http://127.0.0.1:8000
def home(request):
    return render(request, 'index/index.html')    

def about(request):
    return HttpResponse("<h1>About Section</h1>")    
