from django.test import TestCase
from faker import Faker

from ..models.user import User
from ..serializers.auth import RegisterSerializer
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


    def tearDown(self):
        # cleaning up after the test
        print("TestArtItem:setUp_:begin")

        # do something
        print("TestArtItem:setUp_:end")
