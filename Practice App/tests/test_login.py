from urllib import response
from rest_framework import status
from rest_framework.test import APITestCase
from django.test import TestCase, Client
from api.serializers import myUserSerializer, ArtItemSerializer, CommentSerializer, TagSerializer
from api.models import ArtItem, Tag, myUser,Comment
from django.contrib.auth.models import User
import json
from faker import Faker
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.http import JsonResponse 


class TestLogin(APITestCase):
  
    def setUp(self):  

        # setting up for the test
        print("TestLogin:setUp_:begin")
        
        ##### Mock up data #####

        faker = Faker()
        self.client = Client()
       

        self.username = faker.unique.first_name() 
        self.password = faker.unique.password() 
        self.users = []
        user1 = User.objects.create(username = self.username, password=self.password)
        myUser1 = myUser.objects.create ( user = user1,name= faker.first_name(), surname = faker.last_name(), email = faker.email())
        self.users.append(user1)
        print(self.username, self.password,user1.username, user1.password )

        print("TestLogin:setUp_:end")


    def tearDown(self):
        # cleaning up after the test
        print("TestLogin:setUp_:begin")

        # do something
        print("TestLogin:setUp_:end")


    def test_login_get(self):

        for i in range(1):
            response = self.client.get('/api/v1/user/{}/{}'.format(self.username,self.password))
            print(response)
            self.assertEqual(response.status_code, 200)  # check status code

            serializer = myUserSerializer(myUser.objects.get(user=self.users[0]))
            expected = serializer.data
            self.assertEqual(response.json(), expected)
        

        