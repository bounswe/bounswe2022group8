from django.test import TestCase
from faker import Faker

from ..models.user import User
from ..models.models import Comment
from ..models.artitem import ArtItem
"""
setUp() function is like a constructor for our test. It creates some mock data.
Thanks to the django.test, mock data is deleted automatically after the test, you do not have to worry about your database.
tearDown() function is like a destructor, it deletes the objects.
"""


class CommentTest(TestCase):
    # preparing to test
    def setUp(self):
        # setting up for the test
        print("TestComment:setUp_:begin")
        self.faker = Faker()

        # do something
        print("TestComment:setUp_:end")

    def test_comment_creation(self):
        user = User.objects.create(username = self.faker.unique.word(), password = self.faker.password(), email = f"{self.faker.first_name()}.{self.faker.last_name()}@{self.faker.domain_name()}")
        artitem = ArtItem.objects.create(title= self.faker.word(), description = self.faker.paragraph(nb_sentences=3), owner = user)

        comment = Comment.objects.create(commented_by=user, commented_on=artitem, body=self.faker.paragraph(nb_sentences=3))


        self.assertTrue(isinstance(comment, Comment))
        self.assertEqual(comment.__str__(), "A comment made by " + str(user) + " on " + str(artitem))
        

    def test_comment_deletion_cascaded(self):
        user = User.objects.create(username = self.faker.unique.word(), password = self.faker.password(), email = f"{self.faker.first_name()}.{self.faker.last_name()}@{self.faker.domain_name()}")
        artitem = ArtItem.objects.create(title= self.faker.word(), description = self.faker.paragraph(nb_sentences=3), owner = user)

        comment = Comment.objects.create(commented_by=user, commented_on=artitem, body=self.faker.paragraph(nb_sentences=3))

        comment.delete()
               
        self.assertFalse(Comment.objects.filter(id=comment.id))   # empty list is False



    def tearDown(self):
        # cleaning up after the test
        print("TestComment:tearDown_:begin")

        # do something
        print("TestComment:tearDown_:end")
