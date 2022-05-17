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
            response = self.client.get('/api/v1/artitems/users/{}'.format(username))
            self.assertEqual(response.status_code, 200)  # check status code
            
            users = myUser.objects.all()
            user = [x for x in users if x.username == username]
            serializer = ArtItemSerializer(ArtItem.objects.filter(owner=user[0].id), many=True)

            expected = serializer.data
            self.assertEqual(response.json(), expected)

        response = self.client.get('/api/v1/artitems/users/{}'.format(self.usernames[4]))
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

    def generate_photo_file(self):
        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        return file
"""
    def test_artitems_post(self):

        faker = Faker()
        title= faker.word() 
        description = faker.paragraph(nb_sentences=3)
        
       
        image_file = self.generate_photo_file()
        
        data = {'title' : title,
        'description' :description,
        'owner': 1,
        'tags': 1}
        post_data = {'data': data, 'artitem_image' : image_file}

        print(post_data)
        response = self.client.post('/api/v1/artitems/', post_data,  headers = {'Content-Type': 'multipart/form-data'})
        print(response.json)
        self.assertEqual(response.status_code, 200)  # check status code

        serializer = ArtItemSerializer(ArtItem.objects.get(pk=5)) # lastly added
        expected = serializer.data
        self.assertEqual(response.json(), expected)
            
"""
