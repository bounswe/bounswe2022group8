from django.test import TestCase
from faker import Faker

from ..models.user import User
"""
setUp() function is like a constructor for our test. It creates some mock data.
Thanks to the django.test, mock data is deleted automatically after the test, you do not have to worry about your database.
tearDown() function is like a destructor, it deletes the objects.
"""

class RegistrationTest(TestCase):
    # preparing to test
    def setUp(self):
        # setting up for the test
        print("TestArtItem:setUp_:begin")
        self.fake = Faker()

        # do something
        print("TestArtItem:setUp_:end")

    def test_username_validation(self):
        pass


    def tearDown(self):
        # cleaning up after the test
        print("TestArtItem:setUp_:begin")

        # do something
        print("TestArtItem:setUp_:end")
