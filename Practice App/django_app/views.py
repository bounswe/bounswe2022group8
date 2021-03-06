# Don't create your views here. We decided to use urls.py in api folder. 

import urllib.parse
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import TagForm, QuestionTagForm
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
            #response = request.get('http://${host}:8000/api/searchbytag/{encoded}')


    return render(request, 'tag/tagform.html', {'form':TagForm()}) #import render
    #return HttpResponse("why though")

# http://${host}:8000
def home(request):
    return render(request, 'index/index.html')   

# http://${host}:8000/about
def about(request):
    return HttpResponse("<h1>About</h1>")

# http://${host}:8000/artitems/
def all_artitems(request):
    return render(request, 'artitems/list_all_artitems.html') 

# http://${host}:8000/artitems/id
def artitem_by_id(request):
    return render(request, 'artitems/list_artitems_by_id.html') 

# http://${host}:8000/artitems/id/delete
def artitem_by_id_delete(request):
    return render(request, 'artitems/delete_artitems_by_id.html')

# http://${host}:8000/artitems/users/id
def artitem_by_user_id(request):
    return render(request, 'artitems/list_artitems_by_user_id.html') 

# http://${host}:8000/artitems/users/username
def artitem_by_username(request):
    return render(request, 'artitems/list_artimes_by_username.html')

# http://${host}:8000/episodes
def episodes(request):
    return render(request, 'episodes/episodes.html')

# http://${host}:8000/artitems/new
def add_artitem(request):
    return render(request, 'artitems/add_art_item.html')

#  http://${host}:8000/login

def login(request):
    return render(request, 'users/login.html')

# # http://${host}:8000/signup

def signup(request):
    return render(request, 'users/signup.html')
# http://${host}:8000/users/new
def add_user(request):
    return render(request, 'users/add_user.html')

# http://${host}:8000/comments/artitem/id
def commentsOfArtItem(request):
    return render(request, 'comment/comments_of_artitem.html') 

# http://${host}:8000/comments/artitem/new
def commentOnArtItem(request):
    return render(request, 'comment/post_comment_on_artitem.html') 

# http://${host}:8000/user/id/comment/commentid
def deleteComment(request):
    return render(request, 'comment/delete_comment.html') 

# http://${host}:8000/tag/
def list_tags(request):
    return render(request, 'tag/get_all_tags.html')

# http://${host}:8000/tag/id
def delete_tag(request):
    return render(request, 'tag/delete_tag_byID.html')

def add_tags(request):
    return render(request, 'tag/add_tag.html')

# http://${host}:8000/users/
def all_users(request):
    return render(request, 'users/list_all_users.html')

# http://${host}:8000/users/id
def get_user_by_id(request):
    return render(request, 'users/get_user_by_id.html')

# http://${host}:8000/users/id/delete
def delete_user_by_id(request):
    return render(request, 'users/delete_user_by_id.html')
    

def search_user(request):
    return render(request,'search_user/searchuser.html')

def questions(request): 
    if request.POST:
        form = QuestionTagForm(request.POST)
        print(request.POST)
        tag=request.POST["tag"]
        #print("here")
        #print(tag)
        if form.is_valid():        
            #encoded = urllib.parse.quote(str(tag))
            #print(encoded)
            #print(encoded)
            return redirect('getquestions', tag=tag) #Redirect to search_by_tag page
            #response = request.get('http://${host}:8000/api/searchbytag/{encoded}')


    return render(request, 'questions/questions.html', {'form':QuestionTagForm()}) #import render
    #return HttpResponse("why though") 


# # http://${host}:8000/get_followers/
def followers_by_userid(request):
    return render(request, 'follows/list_followers_by_user_id.html')

# # http://${host}:8000/get_followings/
def followings_by_userid(request):
    return render(request, 'follows/list_followings_by_user_id.html')

    # # http://${host}:8000/searchbytag/keyword/
def get_item_by_keyword(request):
    return render(request, 'tag/get_item_by_keyword.html')
