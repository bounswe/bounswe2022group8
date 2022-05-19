from urllib import response
from django.shortcuts import render
import requests
import json
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# this view uses the stackexchange api (given below) to get unanswered questions (with answercount 0) and depending on the given keyword tag 
#either returns all the unanswered questions if tag == "all"
# or returns unanswered questions tagged with the given tag
#the Response uses default django html template, extend the url with <?format=json> to get pure json


@api_view(['GET'])
def getquestions(request, tag, format=None ):
    response = requests.get('http://api.stackexchange.com/2.3/questions/unanswered?order=desc&sort=activity&site=stackoverflow')

    unansweredquestions = {}
    #unansweredquestions['allquestions']=[]
    allquestions = []

    if tag == "all": 
        for question in response.json()['items']:
            if question['answer_count']==0 : 
                questiondata = {}
                questiondata['title'] = question['title']
                questiondata['link'] = question['link']
                questiondata['tags'] = question['tags']
                allquestions.append(questiondata)

                #print(question['title'])
                #print(question['link'])
            #else:
            #    print("skipped")    
            #print()

        if allquestions == []:
            unansweredquestions["message"] = "Sorry there are no unanswered questions at the moment, please try again later."
            return Response(unansweredquestions, status= status.HTTP_404_NOT_FOUND)     

        unansweredquestions['allquestions']= allquestions

        #return JsonResponse(unansweredquestions)
        return Response(unansweredquestions, status= status.HTTP_200_OK)        



    for question in response.json()['items']:
        if question['answer_count']==0 and tag in question['tags']: #and "shell" in question['tags']
            questiondata = {}
            questiondata['title'] = question['title']
            questiondata['link'] = question['link']
            questiondata['tags'] = question['tags']
            allquestions.append(questiondata)

            #print(question['title'])
            #print(question['link'])
        #else:
         #   print("skipped")    
        #print()

    if allquestions == []:
            unansweredquestions["message"] = "Sorry there are no unanswered questions with the given tag at the moment, please try again later."
            return Response(unansweredquestions, status= status.HTTP_404_NOT_FOUND)     

    unansweredquestions['allquestions']= allquestions

    #return JsonResponse(unansweredquestions)
    return Response(unansweredquestions, status= status.HTTP_200_OK)
    #return HttpResponse("Bravo!")
