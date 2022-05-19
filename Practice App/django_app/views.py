# Don't create your views here. We decided to use urls.py in api folder. 

import urllib.parse
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import redirect, render
import urllib.parse

import json


def search_user(request):
    return render(request,'search_user/searchuser.html')

