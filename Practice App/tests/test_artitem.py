from email.mime import multipart
from django.test import TestCase, Client
from api.views.view_artitems import *
from api.serializers import myUserSerializer, ArtItemSerializer, CommentSerializer, TagSerializer
from api.models import myUser, Follow, ArtItem, Comment, Tag
from django.contrib.auth.models import User
import io
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile

"""
Let me explain what's going on here.
setUp() function is like a constructor for our test. It creates some mock data.
Thanks to the django.test, mock data is deleted automatically after the test, you do not have to worry about your database.
tearDown() function is like a destructor, it deletes the objects. 

Please notice that test uses its own database, meaning: when we create a user, it's id is 1. It ignores all the other users 
stored in our database beforehand. So, do not try to test "already existing" data. Create your own data using objects.create() functions and
Faker.

I've used Faker to generate some random data, please examine them carefully. I used 'unique' for generating usernames so that there doesn't
occur any collision (although extremely unlikely, let's take precaution).

Each function tests one API endpoint, they test both the content of the response and the status code.
Please don't forget to check content of the response in your tests. Only checking the status code is not enough.

Client is used to consume our REST API. And that's all actually for client.
Output is generated in xml format and saved into tests/ folder. You can delete the xml files using "rm test-output/*" command if you are using command line.

Thank you for reading. Godspeed.
"""

from faker import Faker

class TestArtItem(TestCase):
    # preparing to test
    def setUp(self):
        # setting up for the test
        print("TestArtItem:setUp_:begin")
        
        ##### Mock up data #####

        self.client = Client()
        faker = Faker()

        tag1 = Tag.objects.create(tagname = faker.word(), description = faker.paragraph(nb_sentences=3))
        tag2 = Tag.objects.create(tagname = faker.word(), description = faker.paragraph(nb_sentences=3))
        tag3 = Tag.objects.create(tagname = faker.word(), description = faker.paragraph(nb_sentences=3))
        tag4 = Tag.objects.create(tagname = faker.word(), description = faker.paragraph(nb_sentences=3))
        
        self.usernames = [ ".".join([faker.unique.first_name(), faker.unique.last_name()]) for i in range(5)]
        passwords = [faker.unique.password() for i in range(4)]
        
        user1 = User.objects.create(username = self.usernames[0], password=passwords[0])
        user2 = User.objects.create(username = self.usernames[1], password=passwords[1])
        user3 = User.objects.create(username = self.usernames[2], password=passwords[2])
        user4 = User.objects.create(username = self.usernames[3], password=passwords[3])


        myUser1 = myUser.objects.create(user=user1, name= faker.first_name(), surname = faker.last_name(), email = faker.email())
        myUser2 = myUser.objects.create(user=user2, name= faker.first_name(), surname = faker.last_name(), email = faker.email())
        myUser3 = myUser.objects.create(user=user3, name= faker.first_name(), surname = faker.last_name(), email = faker.email())
        myUser4 = myUser.objects.create(user=user4, name= faker.first_name(), surname = faker.last_name(), email = faker.email())


        artitem1 = ArtItem.objects.create(title= faker.word(), description = faker.paragraph(nb_sentences=3), owner = myUser1, artitem_image = faker.file_path(depth=1, category='image', extension='png'))
        artitem2 = ArtItem.objects.create(title= faker.word(), description = faker.paragraph(nb_sentences=3), owner = myUser2, artitem_image = faker.file_path(depth=1, category='image', extension='png'))
        artitem3 = ArtItem.objects.create(title= faker.word(), description = faker.paragraph(nb_sentences=3), owner = myUser2, artitem_image = faker.file_path(depth=1, category='image', extension='png'))
        artitem4 = ArtItem.objects.create(title= faker.word(), description = faker.paragraph(nb_sentences=3), owner = myUser3, artitem_image = faker.file_path(depth=1, category='image', extension='png'))

        artitem1.tags.add(tag1)

        artitem2.tags.add(tag1)
        artitem2.tags.add(tag2)

        # no tag for artitem3

        artitem4.tags.add(tag3)
        artitem4.tags.add(tag4)

        # do something
        print("TestArtItem:setUp_:end")


    def tearDown(self):
        # cleaning up after the test
        print("TestArtItem:setUp_:begin")

        # do something
        print("TestArtItem:setUp_:end")


    def test_artitems_by_username(self):
        for username in self.usernames[:4]:
            response = self.client.get('/api/v1/artitems/users/username/{}'.format(username))
            self.assertEqual(response.status_code, 200)  # check status code
            
            users = myUser.objects.all()
            user = [x for x in users if x.username == username]
            serializer = ArtItemSerializer(ArtItem.objects.filter(owner=user[0].id), many=True)

            expected = serializer.data
            self.assertEqual(response.json(), expected)

        response = self.client.get('/api/v1/artitems/users/username/{}'.format(self.usernames[4]))
        self.assertEqual(response.status_code, 404)  # check status code

    def test_artitems_by_id(self):
        for id in range(1, 5):
            response = self.client.get('/api/v1/artitems/{}'.format(id))
            self.assertEqual(response.status_code, 200)  # check status code
            
            serializer = ArtItemSerializer(ArtItem.objects.get(pk=id))

            expected = serializer.data
            self.assertEqual(response.json(), expected)
        
        response = self.client.get('/api/v1/artitems/{}'.format(5))
        self.assertEqual(response.status_code, 404)  # check status code

    def test_artitems_by_userid(self):
        for id in range(1, 5):
            response = self.client.get('/api/v1/artitems/users/{}'.format(id))
            self.assertEqual(response.status_code, 200)  # check status code
            
            serializer = ArtItemSerializer(ArtItem.objects.filter(owner=id), many=True)

            expected = serializer.data
            self.assertEqual(response.json(), expected)
        
        response = self.client.get('/api/v1/artitems/users/{}'.format(5))
        self.assertEqual(response.status_code, 404)  # check status code

    def test_artitems_get(self):
        response = self.client.get('/api/v1/artitems/')
        self.assertEqual(response.status_code, 200)  # check status code

        serializer = ArtItemSerializer(ArtItem.objects.all(), many=True)
        expected = serializer.data
        self.assertEqual(response.json(), expected)


    def test_artitems_post(self):
        faker = Faker()
        title= faker.word() 
        description = faker.paragraph(nb_sentences=3)
    
        data = {"title" : title,
        "description" : description,
        "owner": 1,
        "tags": 1,
        "artitem_image": 
        "data:image/jpeg;base64,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"}
        # base64 encoded version of a tiny image

        response = self.client.post('/api/v1/artitems/', content_type='application/json', data=data)
        self.assertEqual(response.status_code, 201)  # check status code

        serializer = ArtItemSerializer(ArtItem.objects.get(pk=5)) # lastly added
        expected = serializer.data
        self.assertEqual(response.json(), expected)
        
            
    def test_artitems_post_400(self):

        data1 = { "description" :"--", "owner": 1, "tags": 1}  # title is missing
        response = self.client.post('/api/v1/artitems/', content_type='application/json', data = data1)
        self.assertEqual(response.status_code, 400)

        data2 = { "title" :"--", "owner": 1, "tags": 1}  # description is missing
        response = self.client.post('/api/v1/artitems/', content_type='application/json', data = data2)
        self.assertEqual(response.status_code, 400)

        data3 = { "description" :"--", "title": "--", "tags": 1}  # owner is missing
        response = self.client.post('/api/v1/artitems/', content_type='application/json', data = data3)
        self.assertEqual(response.status_code, 400)
