from urllib import response
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import ArtItem, Tag, myUser
from django.contrib.auth.models import User
import json

class TestTagSearch(APITestCase):
  
    def test_get_tagged_artitems(self):

        test_user = User.objects.create(username='Jane', password='111111')
        test_myuser = myUser.objects.create(user=test_user, name='Jane', surname='Doe', email='jane@gmail.com')
        test_tag = Tag.objects.create(tagname='watercolour', description='Nice pastel watercolours.')
        test_artitem = ArtItem.objects.create(title='Flowers', description='A field full of flowers.', owner_id='1') #can I define tags like that
        test_artitem.tags.add(test_tag)


        url = reverse('search_by_tag', args=[test_tag.tagname])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        test_data = { "id":1, "title":"Flowers", "description": "A field full of flowers.", "owner": 1, "tags": [ 1 ], "artitem_image": "/media/artitem/defaultart.jpg"}
        #test_data = { 'id':1, 'title':'Flowers', 'description': 'A field full of flowers.', 'owner': 1, 'tags': [ 1 ], 'artitem_image': '/media/artitem/defaultart.jpg'}

        #print("Response is:")
        #print(json.dumps(response.data))
        #print("Test data is:")
        #print([test_data])

        #self.assertEqual(json.dumps(response.data), [test_data])
        self.assertEqual(response.data, [test_data])
