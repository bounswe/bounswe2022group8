from django.http import response
from django.test import TestCase, Client

class EpisodesTestCase(TestCase):

    def test_get_episodes(self):
        c = Client()

        response = c.get('/api/episodes/hüsnü komiser')
        self.assertEqual(response.status_code, 404)

        response = c.get('/api/episodes/arka sokaklar')
        self.assertEqual(response.status_code, 200)

        response = c.get('/api/episodes/wayward pines')
        self.assertEqual(response.status_code, 200)