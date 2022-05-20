from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
import json

"""
This API endpoint uses a tvmaze.api which can be found here: https://www.tvmaze.com/api
It's a free to use API that doesn't require any authentication.
"""

"""
Input parameters: series (string)
Output JSON object:
    {name, language, genre, description, rating, number of seasons, episodes} 
episode is a list of JSON objects, each JSON object consisting of:
    {name, season, rating, summary}
"""
@api_view(['GET'])
def episodes(request, series):
    request = requests.get("https://api.tvmaze.com/singlesearch/shows?q={}&embed=episodes".format(series))
    
    if request.status_code == 200:
        response = request.json()
        data = {}
        data['name'] = response['name']
        data['language'] = response['language']
        data['genre'] = response['genres']
        data['description'] = response['summary']
        data['rating'] = response['rating']['average']
        episodes = []
        cnt = 1

        for episode in response['_embedded']["episodes"]:
            info = {}
            info['name'] = episode['name']
            info['season'] = episode['season']
            info['rating'] = episode['rating']['average']
            info['summary'] = episode['summary']
            cnt = info['season']
            episodes.append(info)

        data["number of seasons"] = cnt
        data["episodes"] = episodes
        return JsonResponse(data)
    elif(request.status_code == 404): # resource does not exist
        return JsonResponse({'status': 'TV Series with the specified name cannot be found.'}, status = 404)
    else:
        return JsonResponse({'status': 'An internal server error has occurred in the system. Please try again.'}, status = 503)




    
    
