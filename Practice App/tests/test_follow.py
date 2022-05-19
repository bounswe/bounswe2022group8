from email.mime import multipart
from django.test import TestCase, Client
from api.views.view_artitems import *
from api.serializers import myUserSerializer, ArtItemSerializer, FollowSerializer
from api.models import myUser, Follow, ArtItem, Comment, Tag
from django.contrib.auth.models import User
import io
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from random import randrange


"""
Each function tests one API endpoint, they test both the content of the response and the status code.
Please don't forget to check content of the response in your tests.
"""

from faker import Faker

class TestFollow(TestCase):
    # preparing to test
    def setUp(self):
        # setting up for the test
        print("TestFollow:setUp_:begin")
        
        ##### Mock up data #####

        self.client = Client()
        fake = Faker()
        
        user1 = User.objects.create(username = fake.unique.first_name(), password=fake.password())
        user2 = User.objects.create(username = fake.unique.first_name(), password=fake.password())
        user3 = User.objects.create(username = fake.unique.first_name(), password=fake.password())
        user4 = User.objects.create(username = fake.unique.first_name(), password=fake.password())
        user5 = User.objects.create(username = fake.unique.first_name(), password=fake.password())
        user6 = User.objects.create(username = fake.unique.first_name(), password=fake.password())

        myUser1 = myUser.objects.create(user=user1, name= fake.first_name(), surname = fake.last_name(), email = fake.email())
        myUser2 = myUser.objects.create(user=user2, name= fake.first_name(), surname = fake.last_name(), email = fake.email())
        myUser3 = myUser.objects.create(user=user3, name= fake.first_name(), surname = fake.last_name(), email = fake.email())
        myUser4 = myUser.objects.create(user=user4, name= fake.first_name(), surname = fake.last_name(), email = fake.email())
        myUser5 = myUser.objects.create(user=user5, name= fake.first_name(), surname = fake.last_name(), email = fake.email())
        myUser6 = myUser.objects.create(user=user6, name= fake.first_name(), surname = fake.last_name(), email = fake.email())

        follow1 = Follow.objects.create(from_user = myUser1, to_user = myUser2)
        follow2 = Follow.objects.create(from_user = myUser1, to_user = myUser3)
        follow3 = Follow.objects.create(from_user = myUser1, to_user = myUser4)
        follow4 = Follow.objects.create(from_user = myUser2, to_user = myUser1)
        follow5 = Follow.objects.create(from_user = myUser2, to_user = myUser4)
        follow6 = Follow.objects.create(from_user = myUser3, to_user = myUser1)
        follow7 = Follow.objects.create(from_user = myUser3, to_user = myUser2)
        follow8 = Follow.objects.create(from_user = myUser4, to_user = myUser6)
        follow9 = Follow.objects.create(from_user = myUser4, to_user = myUser5)
        follow10 = Follow.objects.create(from_user = myUser4, to_user = myUser1)
        follow11 = Follow.objects.create(from_user = myUser5, to_user = myUser1)
        follow12 = Follow.objects.create(from_user = myUser6, to_user = myUser1)
        follow12 = Follow.objects.create(from_user = myUser6, to_user = myUser3)

        print("TestFollow:setUp_:end")


    def tearDown(self):
        # cleaning up after the test
        print("TestFollow:setUp_:begin")

        # do something
        print("TestFollow:setUp_:end")

    def test_followers_by_userid(self):
        for id in range(1, 7):
            response = self.client.get('/api/v1/get_followers/{}'.format(id))
            self.assertEqual(response.status_code, 200)  # check status code
            
            user =  myUser.objects.get(pk=id)
            serializer = myUserSerializer(user.follower.all(), many=True)

            expected = serializer.data
            self.assertEqual(response.json(), expected)
        

    def test_followings_by_userid(self):
        for id in range(1, 7):
            response = self.client.get('/api/v1/get_followings/{}'.format(id))
            self.assertEqual(response.status_code, 200)  # check status code
            
            user = myUser.objects.get(pk=id)

            all_users = myUser.objects.all()
            following_users = [x for x in all_users if user in x.follower.all()]
            followings = myUserSerializer(following_users, many=True)

            expected = followings.data
            self.assertEqual(response.json(), expected)
        

    def test_followers_post(self):
        faker = Faker()
        follower = randrange(1,7)
        following = follower

        while(following == follower):
            following = randrange(1,7)

        data = {"from_user" : follower,
                "to_user" : following
                }
        
        response = self.client.post('/api/v1/follow_user/', content_type='application/json', data=data)
        self.assertEqual(response.status_code, 201)  # check status code

        serializer = FollowSerializer(Follow.objects.get(pk=7)) # lastly added
        expected = serializer.data
        self.assertEqual(response.json(), expected)
        