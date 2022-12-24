from django.test import TestCase, RequestFactory
from faker import Faker

from ..models.user import User
from ..models.artitem import ArtItem, Tag
from ..serializers.serializers import ArtItem, ArtItemSerializer
from django.contrib.auth.models import AnonymousUser, User
from ..views.artitem import *
from ..views.auth import *
from ..views.profile import profile_me_api, profile_api
from ..views.user import users_api
from .utils import utils
from ..serializers.profile import UserProfileSerializer

class TestProfile(TestCase):
    # preparing to test
    def setUp(self):
        # setting up for the test
        print("TestProfile:setUp_:begin")
        self.faker = Faker()
        self.factory = RequestFactory()
        self.user = utils.register()
        # do something
        print("TestProfile:setUp_:end")

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

    # POST profile
    def test_update_profile(self):
        name =  self.faker.pystr(min_chars = 10)
        about = self.faker.paragraph(nb_sentences = 3)
        surname = self.faker.pystr(min_chars = 10)
        location = self.faker.pystr(min_chars = 10)

        data = {
            'name': name,
            'about': about,
            'surname': surname,
            'location': location
        }

        header = {"HTTP_AUTHORIZATION": "Token " + self.user["token"]}
        request = self.factory.put('/users/profile/me/', data, **header, content_type='application/json')
        response = profile_me_api(request)
        data = response.data

        expected = {
            "id": self.user['user']['id'],
            "name": name,
            "surname": surname,
            "about": about,
            "location": location
            }

        actual = {
            "id": data['id'],
            "name": data['name'],
            'surname': data['surname'],
            'about': data['about'],
            'location': data['location']
        }
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(actual, expected)
    
    # GET all users
    def test_get_all_users(self):
        request = self.factory.get('/users/profile/users/', content_type='application/json')
        response = users_api(request)

        user = User.objects.get(pk=self.user['user']['id'])
        expected = UserProfileSerializer(user).data
        actual = response.data[0]

        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.data, list))
        self.assertEqual(expected, actual)
    
    # GET user by id
    def test_get_user_by_id(self):
        request = self.factory.get('/users/profile/', content_type='application/json')
        response = profile_api(request, self.user['user']['id'])

        user = User.objects.get(pk=self.user['user']['id'])
        expected = UserProfileSerializer(user).data
        actual = response.data
        expected["isFollowed"] = False

        self.assertEqual(response.status_code, 200)
        self.assertEqual(expected, actual)
        

    def tearDown(self):
        # cleaning up after the test
        print("TestProfile:tearDown_:begin")

        # do something
        print("TestProfile:tearDown_:end")
