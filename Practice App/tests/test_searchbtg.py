from urllib import response
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.test import TestCase, Client
from api.serializers import myUserSerializer, ArtItemSerializer, CommentSerializer, TagSerializer
from api.models import ArtItem, Tag, myUser
from django.contrib.auth.models import User
import json
from faker import Faker

class TestTagSearch(APITestCase):
  
    def setUp(self):  


        # setting up for the test
        print("TestSearchbtg:setUp_:begin")
        
        ##### Mock up data #####

        faker = Faker()
        test_user = User.objects.create(username = faker.first_name(), password=faker.password())
        test_myUser = myUser.objects.create(user=test_user, name= faker.first_name(), surname = faker.last_name(), email = faker.email())
        self.tagname = faker.word()
        test_tag = Tag.objects.create(tagname = self.tagname, description = faker.paragraph(nb_sentences=3))
        test_artitem = ArtItem.objects.create(title= faker.word(), description = faker.paragraph(nb_sentences=3), owner = test_myUser, artitem_image = faker.file_path(depth=1, category='image', extension='png'))
        self.artitemId = test_artitem.id
        test_artitem.tags.add(test_tag)

        self.tagname2 = 'someweirdwordtnottobeusedelsewhere'
        test_tag2 = Tag.objects.create(tagname = self.tagname2, description = faker.paragraph(nb_sentences=3))

        print("TestSearchbtg:setUp_:end")



    def tearDown(self):
        # cleaning up after the test
        print("TestSearchbtg:setUp_:begin")

        # do something
        print("TestSearchbtg:setUp_:end")


    def test_get_tagged_artitems(self):
        response = self.client.get('/api/v1/searchbytag/{}'.format(self.tagname))
        self.assertEqual(response.status_code, 200)  # check status code
            
        serializer = ArtItemSerializer(ArtItem.objects.filter(pk=self.artitemId), many=True)

        expected = serializer.data
        self.assertEqual(response.json(), expected)

    def test_get_tagged_artitems_no_tag(self):
        response = self.client.get('/api/v1/searchbytag/someweirdname')
        self.assertEqual(response.status_code, 404)  # check status code
        resp = {}
        resp["message"]= "Sorry, the given tag does not exist. Perhaps try get all tags API to see what tags are available."
        self.assertEqual(response.json(), resp)

    def test_get_tagged_artitems_no_item_with_tag(self):
        response = self.client.get('/api/v1/searchbytag/{}'.format(self.tagname2))
        self.assertEqual(response.status_code, 204)  # check status code
        resp = {}
        resp["message"]= "Sorry, currently there are no art items tagged with the given tag. Perhaps try get all art items API to see what art items are available."
        #print("Response:")
        #print(response.data)
        #print(response.json())
        #print("Resp:")
        #print(resp)
        self.assertEqual(response.data, resp)


        
