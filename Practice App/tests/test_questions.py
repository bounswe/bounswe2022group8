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

class TestQuestions(APITestCase):
  
    def setUp(self):  
        # setting up for the test
        print("TestQuestions:setUp_:begin")
        
        ##### Mock up data #####

        faker = Faker()
        self.tagname = faker.word()

        print("TestQuestions:setUp_:end")



    def tearDown(self):
        # cleaning up after the test
        print("TestQuestions:setUp_:begin")

        # do something
        print("TestQuestions:setUp_:end")


    def test_questions_all(self):
        response = self.client.get('/api/v1/questions/all')
        unansweredquestions = {}
        unansweredquestions["message"] = "Sorry there are no unanswered questions at the moment, please try again later."
        
        if response.status_code == 404:     
            self.assertEqual(response.json(), unansweredquestions )  # check if the error message is correct

        else:
            self.assertEqual(response.status_code, 200 ) 
            self.assertNotEqual(response.json(), {})
            self.assertNotEqual(response.json(), unansweredquestions)

    def test_questions_tag(self):
        response = self.client.get('/api/v1/questions/{}'.format(self.tagname))
        unansweredquestions = {}
        unansweredquestions["message"] = "Sorry there are no unanswered questions with the given tag at the moment, please try again later."
            
        if response.status_code == 404:   
            self.assertEqual(response.json(), unansweredquestions )  # check if the error message is correct

        else:
            self.assertEqual(response.status_code, 200 ) 
            self.assertNotEqual(response.json(), {})
            self.assertNotEqual(response.json(), unansweredquestions)
            