from django.test import TestCase, RequestFactory
from faker import Faker

from ..models.user import User
from ..models.artitem import ArtItem, Tag
from ..serializers.serializers import ArtItem, ArtItemSerializer
from django.contrib.auth.models import AnonymousUser, User
from ..views.artitem import *
from ..views.auth import *
from ..views.profile import profile_me_api
from .utils import utils

class CommentProfile(TestCase):
    # preparing to test
    def setUp(self):
        # setting up for the test
        print("TestArtItem:setUp_:begin")
        self.faker = Faker()
        self.factory = RequestFactory()
        self.user = utils.register()
        self.user2 = utils.register()
        # do something
        print("TestArtItem:setUp_:end")

    # GET my profile
    def test_get_my_profile(self):
        password =  self.faker.pystr(min_chars = 10)
        email = f"{self.faker.first_name()}.{self.faker.last_name()}@{self.faker.domain_name()}"
        username = self.faker.pystr(min_chars = 10)
        data = {
            "email": email,
            "username": username,
            "password":password,
            "password_confirm": password
            }
        request = self.factory.post('/auth/register/', data, content_type='application/json')
        response = RegisterView().as_view()(request)

        header = {"HTTP_AUTHORIZATION": "Token " + response.data["token"]}
        request = self.factory.get('/users/profile/me/', **header, content_type='application/json')
        response = profile_me_api(request)
    
        res = response.data
        self.assertEqual(response.status_code, 200)
        
        expected = {
            'username': username,
            'email': email,
            'is_level2': False,
            'followers': 0,
            'followings': 0,
            'name': '',
            'surname': '',
            'about': '',
            'location': '',
            'profile_path': 'avatar/default.png'
        }
        actual = {
            'username': res['username'],
            'email': res['email'],
            'is_level2': res['is_level2'],
            'followers': res['followers'],
            'followings': res['followings'],
            'name': res['name'],
            'surname': res['surname'],
            'about': res['about'],
            'location': res['location'],
            'profile_path': res['profile_path']
        }
        self.assertEqual(expected, actual)


    def tearDown(self):
        # cleaning up after the test
        print("TestComment:tearDown_:begin")

        # do something
        print("TestComment:tearDown_:end")
