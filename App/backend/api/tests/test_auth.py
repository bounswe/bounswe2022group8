from django.test import TestCase, RequestFactory
from faker import Faker

from ..models.user import User
from ..serializers.auth import RegisterSerializer
from ..views.auth import RegisterView, LoginView
from knox import views as knox_views
"""
setUp() function is like a constructor for our test. It creates some mock data.
Thanks to the django.test, mock data is deleted automatically after the test, you do not have to worry about your database.
tearDown() function is like a destructor, it deletes the objects.
"""

class RegistrationTest(TestCase):
    # preparing to test
    def setUp(self):
        # setting up for the test
        print("TestRegister:setUp_:begin")
        self.faker = Faker()
        self.serializer = RegisterSerializer()
        self.factory = RequestFactory()

        # do something
        print("TestRegister:setUp_:end")

    def test_username_syntax(self):
        """
        Check the following rules for a username:
        1) First character must be a letter
        2) Last character cannot be an underscore
        3) It can consist of letters, numbers and underscore (alphanum + underscore)
        4) It must have at least 6 characters
        """

        username1 = self.faker.pystr(min_chars = 10)
        username2 = self.faker.pystr(min_chars = 10)
        username3 = self.faker.pystr(min_chars = 10)
        username4 = self.faker.pystr(max_chars = 5)
        username5 = self.faker.pystr(min_chars = 10)

        username1 = "1" + username1
        username2 = username2 + "_"
        username3 = username3[0: 5] + "*" + username3[5:]

        expected1 = (False, self.serializer.START_ERROR)
        expected2 = (False, self.serializer.END_ERROR)
        expected3 = (False, self.serializer.ALPHANUM_ERROR)
        expected4 = (False, self.serializer.MIN_LENGTH_ERROR)
        expected5 = (True, self.serializer.SUCCESS)

        self.assertEqual(self.serializer.is_valid_username(username1), expected1)
        self.assertEqual(self.serializer.is_valid_username(username2), expected2)
        self.assertEqual(self.serializer.is_valid_username(username3), expected3)
        self.assertEqual(self.serializer.is_valid_username(username4), expected4)
        self.assertEqual(self.serializer.is_valid_username(username5), expected5)
    

    # registration test (1)
    def test_register_1(self):  
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
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['user']['email'], email)
        self.assertEqual(response.data['user']['username'], username)
    
    # registration test (2) invalid attempts
    def test_register_2(self):  
        password =  self.faker.pystr(min_chars = 10)
        email = f"{self.faker.first_name()}.{self.faker.last_name()}@{self.faker.domain_name()}"
        data = {
            "email": email,
            "username": "",
            "password":password,
            "password_confirm": password
            }
        invalid_usernames = ["1invalidusername", "invalidusername_", "invalid@??username", "user"]
        for iusername in invalid_usernames:
            data["username"] = iusername
            request = self.factory.post('/auth/register/', data, content_type='application/json')
            response = RegisterView().as_view()(request)
            self.assertEqual(response.status_code, 400)
   
    # attempt to login without registration (23)
    def test_login_1(self):
        email = f"{self.faker.first_name()}.{self.faker.last_name()}@{self.faker.domain_name()}"
        password =  self.faker.pystr(min_chars = 10)

        login_data = {
            "credential": email,
            "password":password
            }
        request = self.factory.post('/auth/login/', login_data, content_type='application/json')
        response = LoginView().as_view()(request)

        self.assertEqual(response.status_code, 400) # attempt to login without registration

    # login with valid credentials (4)
    def test_login_2(self):
        email = f"{self.faker.first_name()}.{self.faker.last_name()}@{self.faker.domain_name()}"
        password =  self.faker.pystr(min_chars = 10)
        username = self.faker.pystr(min_chars = 10)
        register_data = {
            "email": email,
            "username": username,
            "password":password,
            "password_confirm": password
            }
        login_data = {
            "credential": email,
            "password":password
            }
        request = self.factory.post('/auth/register/', register_data, content_type='application/json')
        response = RegisterView().as_view()(request)
        request = self.factory.post('/auth/login/', login_data, content_type='application/json')
        response = LoginView().as_view()(request)
        
        self.assertEqual(response.status_code, 200)

    # logout failure (5)
    def test_logout_failure(self):
        request = self.factory.post('/auth/logout/')
        response = knox_views.LogoutView.as_view()(request)
        self.assertEqual(response.status_code, 401)

    # logout success (6)
    def test_logout_success(self):
        email = f"{self.faker.first_name()}.{self.faker.last_name()}@{self.faker.domain_name()}"
        password =  self.faker.pystr(min_chars = 10)
        username = self.faker.pystr(min_chars = 10)
        register_data = {
            "email": email,
            "username": username,
            "password":password,
            "password_confirm": password
            }
        login_data = {
            "credential": email,
            "password":password
            }
        request = self.factory.post('/auth/register/', register_data, content_type='application/json')
        RegisterView().as_view()(request)

        request = self.factory.post('/auth/login/', login_data, content_type='application/json')
        response = LoginView().as_view()(request)
  
        my_header = {"HTTP_AUTHORIZATION": "Token " + response.data["token"]}
        request = self.factory.post('/auth/logout/', **my_header)
        response = knox_views.LogoutView.as_view()(request)

        self.assertEqual(response.status_code, 204)

    def tearDown(self):
        # cleaning up after the test
        print("TestArtItem:tearDown_:begin")

        # do something
        print("TestArtItem:tearDown_:end")
