from django.http import response
from django.test import TestCase, Client

"""
Unittest for Episodes API.
First it sends a request with an invalid TV Series name. It expects status code 404.
Then it sends another requests to 'arka sokaklar', 'wayward pines' and '11.22.63'.
For the first two of them, it checks if request was succesfull.
For the last one, it compares the content of the JSON response with some expected data prepared beforehand.
It doesn't compare ratings and summaries: Don't compare rating because they might change frequently,
don't compare summaries because it takes too much space.
"""
class EpisodesTestCase(TestCase):

    def test_get_episodes(self):
        c = Client()

        response = c.get('/api/episodes/hüsnü komiser')
        self.assertEqual(response.status_code, 404)

        response = c.get('/api/episodes/arka sokaklar')
        self.assertEqual(response.status_code, 200)

        response = c.get('/api/episodes/wayward pines')
        self.assertEqual(response.status_code, 200)

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

        response = c.get('/api/episodes/11.22.63')
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
