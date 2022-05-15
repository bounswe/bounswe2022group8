from django.http import response
from django.test import TestCase, Client
import json
import time
from bs4 import BeautifulSoup
import requests
import random

"""
Unittest for Episodes API.
1) test_basic: Calls the API using some random TV series fetched from IMDB. Tests the status code
2) test_get_episodes_1: Makes a call to API using TV Series "11.22.63". Expected output is prepared beforehand and it is cross-checked with the actual result.
3) test_get_episodes_2: Makes a call to API using TV Series "Defending Jacob". Expected output is prepared beforehand and it is cross-checked with the actual result.
"""
class TestEpisodes(TestCase):


    def setUp(self):
        print("TestArtItem:setUp_:begin")

        self.c = Client()

        print("TestArtItem:setUp_:end")


    """
    A simple script to get top 100 TV series from website of imdb.
    Please notice that it doesn't use any API. It just makes a request and gets a page in HTML format.
    Then gives this page to BeautfiulSoup object so that it is parsed. 
    It looks for all "td.titleColumn a" elements and then creates a list called 'series'.
    List will consist of 100 elements (names of the TV series).
    """
    def get_top_TVSeries(self):
        req = requests.get('https://www.imdb.com/chart/tvmeter?sort=ir,desc&mode=simple&page=1')
        if(req.status_code == 500):
            # there is a server error (not related to us), let's just return our own mock data
            return ["arka sokaklar", "adanali", "prison break", "breaking bad", "lost"]  # efsane dizilerdi be 
        
        soup = BeautifulSoup(req.content, 'html.parser')
        shows = soup.select("td.titleColumn a")

        unique_shows = []
        for link in shows:
            if(link.text) not in unique_shows:
                unique_shows.append(link.text)

        series = []
        for name in unique_shows:
            # NCIS can be one of the TV series we can fetch. However, in tvmaze/api it doesn't have any correspondence with this long name. We should replace it with simply 'NCIS'.
            if(name == "NCIS: Naval Criminal Investigative Service"): 
                name = "NCIS"
            series.append(name)
        return series
        

    def tearDown(self):
        # cleaning up after the test
        print("TestArtItem:tearDown_:begin")

        # do something
        print("TestArtItem:tearDown_:end") 

    
    def test_basic(self):
        self.series = self.get_top_TVSeries()
        
        for _ in range(20):
            series = random.choice(self.series)
            response = self.c.get('/api/v1/episodes/{}'.format(series))
            print(series)
            self.assertEqual(response.status_code, 200)

        response = self.c.get('/api/v1/episodes/hüsnü komiser')  # no such TV series
        self.assertEqual(response.status_code, 404)



    def test_get_episodes_1(self):

        expected = {"name": "11.22.63", "language": "English", "genre": ["Drama", "Science-Fiction", "Mystery"],
         "rating": {"average": 7.8}, "number of seasons": 1, 
        "episodes": [
        {"name": "The Rabbit Hole", "season": 1, "rating": {"average": 8.4}}, 
        {"name": "The Kill Floor", "season": 1, "rating": {"average": 7.8}}, 
        {"name": "Other Voices, Other Rooms", "season": 1, "rating": {"average": 7.6}}, 
        {"name": "The Eyes of Texas", "season": 1, "rating": {"average": 7.3}}, 
        {"name": "The Truth", "season": 1, "rating": {"average": 7.8}}, 
        {"name": "Happy Birthday, Lee Harvey Oswald", "season": 1, "rating": {"average": 8}}, 
        {"name": "Soldier Boy", "season": 1, "rating": {"average": 7.7}}, 
        {"name": "The Day in Question", "season": 1, "rating": {"average": 8.5}} ]}

        ### 11/22/63 is a mini-TV Series. It's a MUST watch.

        response = self.c.get('/api/v1/episodes/11.22.63')
        self.assertEqual(response.status_code, 200)
        returned = response.json()

        conditions = []
        conditions.append(expected['name'] == returned['name'])
        conditions.append(expected['language'] == returned['language'])
        conditions.append(expected['genre'] == returned['genre'])
        conditions.append(expected['number of seasons'] == returned['number of seasons'])
        conditions.append(all(a['name'] == b['name'] for a, b in zip(expected['episodes'], returned['episodes'])))
        conditions.append(all(a['season'] == b['season'] for a, b in zip(expected['episodes'], returned['episodes'])))


        self.assertTrue(all(conditions))

    def test_get_episodes_2(self):

        expected = {"name": "Defending Jacob", "language": "English", "genre": ["Drama","Thriller","Legal"],
        "rating": {"average":7.8}, "number of seasons": 1, 
        "episodes": [
        {"name": "Pilot", "season": 1, "rating": {"average": 7.8}}, 
        {"name": "Everything Is Cool", "season":1, "rating": {"average": 8.2}},
        {"name": "Poker Faces", "season": 1, "rating": {"average": 8.2}}, 
        {"name": "Damage Control", "season": 1, "rating": {"average": 8.1}}, 
        {"name": "Visitors", "season": 1, "rating": {"average": 8.1}}, 
        {"name": "Wishful Thinking", "season": 1, "rating": {"average": 8}}, 
        {"name": "Job", "season": 1, "rating": {"average": 8.3}}, 
        {"name": "After", "season": 1, "rating": {"average": 7.7}} ]}

        ### Defending Jacob is another mini-TV Series. That's also great.

        response = self.c.get('/api/v1/episodes/Defending Jacob')
        
        self.assertEqual(response.status_code, 200)
        returned = response.json()

        conditions = []
        conditions.append(expected['name'] == returned['name'])
        conditions.append(expected['language'] == returned['language'])
        conditions.append(expected['genre'] == returned['genre'])
        conditions.append(expected['number of seasons'] == returned['number of seasons'])
        conditions.append(all(a['name'] == b['name'] for a, b in zip(expected['episodes'], returned['episodes'])))
        conditions.append(all(a['season'] == b['season'] for a, b in zip(expected['episodes'], returned['episodes'])))


        self.assertTrue(all(conditions))
