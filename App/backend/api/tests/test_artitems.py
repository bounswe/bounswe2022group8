from django.test import TestCase, RequestFactory
from faker import Faker

from ..models.user import User
from ..models.artitem import ArtItem, Tag
from ..serializers.serializers import ArtItem, ArtItemSerializer
from django.contrib.auth.models import AnonymousUser, User
from ..views.artitem import *
from ..views.auth import *
from .utils import utils
"""
setUp() function is like a constructor for our test. It creates some mock data.
Thanks to the django.test, mock data is deleted automatically after the test, you do not have to worry about your database.
tearDown() function is like a destructor, it deletes the objects.
"""
BASE64 = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVQYV2NgYAAAAAMAAWgmWQ0AAAAASUVORK5CYII="

class ArtItemTest(TestCase):
    # preparing to test
    def setUp(self):
        # setting up for the test
        print("TestArtItem:setUp_:begin")
        self.faker = Faker()
        self.serializer = ArtItemSerializer()
        self.factory = RequestFactory()
        self.user = utils.register()
        self.user2 = utils.register()
        # do something
        print("TestArtItem:setUp_:end")

    def test_artitem_creation(self):
        user = User.objects.create(username = self.faker.unique.word(), password = self.faker.password(), email = f"{self.faker.first_name()}.{self.faker.last_name()}@{self.faker.domain_name()}")
        artitem = ArtItem.objects.create(title= self.faker.word(), description = self.faker.paragraph(nb_sentences=3), owner = user)

        self.assertTrue(isinstance(artitem, ArtItem))
        self.assertEqual(artitem.__str__(), "Art item: " + artitem.title)
        self.assertEqual(artitem.artitem_image, 'artitem/defaultart.jpg')

    def test_artitem_deletion_cascaded(self):
        user = User.objects.create(username = self.faker.unique.word(), password = self.faker.password(), email = f"{self.faker.first_name()}.{self.faker.last_name()}@{self.faker.domain_name()}")
        artitem = ArtItem.objects.create(title= self.faker.word(), description = self.faker.paragraph(nb_sentences=3), owner = user)
        id = artitem.id

        user.delete()
        self.assertFalse(ArtItem.objects.filter(id=id))   # empty list is False   

    def test_artitem_deletion(self):
        user = User.objects.create(username = self.faker.unique.word(), password = self.faker.password(), email = f"{self.faker.first_name()}.{self.faker.last_name()}@{self.faker.domain_name()}")
        artitem = ArtItem.objects.create(title= self.faker.word(), description = self.faker.paragraph(nb_sentences=3), owner = user)
        title = artitem.title


        artitem.delete()
        self.assertFalse(ArtItem.objects.filter(title=title))   # empty list is False   
    

    # POST Test
    def test_artitem_post(self):
        tag = Tag.objects.create(tagname=self.faker.pystr(min_chars = 10), description=self.faker.paragraph(nb_sentences=3))
        user = utils.register()

        title = self.faker.pystr(min_chars = 10)
        description  = self.faker.paragraph(nb_sentences=3)
        category = ArtItem.Category.DRAWING.value
        artitem_image = BASE64

        data = {
            "title": title,
            "description": description,
            "category": category,
            "artitem_image": artitem_image,
            "tags": [tag.id]
        }

        header = {"HTTP_AUTHORIZATION": "Token " + user["token"]}
        request = self.factory.post('/artitems/me/upload/', data, **header, content_type='application/json')
        response = post_artitem(request)
        
        actual = response.data
        expected = {
            "title": title,
            "description": description,
            "username": user["user"]["username"],
            "category": category,
            "likes": 0,
            "number_of_views": 0,
            "tags": [tag.id]
        }
        actual = {
            "title": actual["title"],
            "description": actual["description"],
            "username": actual["owner"]["username"],
            "category": actual["category"],
            "likes": actual["likes"],
            "number_of_views": actual["number_of_views"],
            "tags": [t["id"] for t in actual["tags"]]   
        }

        self.assertEqual(response.status_code, 201)
        self.assertEqual(actual, expected)

    # GET all art items - test
    def test_get_all_artitems(self):
        created = utils.upload_an_image(self.user)

        request = self.factory.get('/artitems/', content_type='application/json')
        response = get_artitems(request)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.data, list))
        artitem = response.data[0]
        self.compare_equality(created, artitem)
    
    # get artitem by id
    def test_get_artitem_by_id(self):
        created = utils.upload_an_image(self.user)
        id = created['id']

        request = self.factory.get('/artitems/', content_type='application/json')
        response = artitems_by_id(request, id)

        self.assertEqual(response.status_code, 200)
        artitem = response.data
        self.compare_equality(created, artitem)
    
    # get artitem by user id
    def test_get_artitem_by_userid(self):
        created = utils.upload_an_image(self.user)
        userid = created['owner']['id']

        request = self.factory.get('/artitems/users/', content_type='application/json')
        response = artitems_by_userid(request, userid)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.data, list))
        artitem = response.data[0]
        self.compare_equality(created, artitem)

    # get artitem by username (multiple images)
    def test_get_artitem_by_username(self):
        created1 = utils.upload_an_image(self.user)
        created2 = utils.upload_an_image(self.user)
        username = created1['owner']['username']

        request = self.factory.get('/artitems/users/username/', content_type='application/json')
        response = artitems_by_username(request, username)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.data, list))
        artitem1 = response.data[1] 
        artitem2 = response.data[0]
        self.compare_equality(created1, artitem1)
        self.compare_equality(created2, artitem2)


    # delete artitem
    def test_delete_artitem(self):
        created = utils.upload_an_image(self.user)
        id = created['id']
        userid = created['owner']['id']

        header = {"HTTP_AUTHORIZATION": "Token " + self.user["token"]}
        request = self.factory.delete('/artitems/me/remove/', **header, content_type='application/json')
        response = delete_artitem(request, id)
        self.assertEqual(response.status_code, 204)

        request = self.factory.get('/artitems/users/', content_type='application/json')
        response = artitems_by_userid(request, userid)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])

# delete artitem of another user
    def test_invalid_delete_artitem(self):
        created = utils.upload_an_image(self.user)
        id = created['id']
        userid = created['owner']['id']

        header = {"HTTP_AUTHORIZATION": "Token " + self.user2["token"]}
        request = self.factory.delete('/artitems/me/remove/', **header, content_type='application/json')
        response = delete_artitem(request, id)
        self.assertEqual(response.status_code, 403)

    # test - artitems of followed users
    def test_artitems_of_followeds(self):
        utils.create_follow(self.user, self.user2) # self.user follows self.user2
        created = utils.upload_an_image(self.user2)

        header = {"HTTP_AUTHORIZATION": "Token " + self.user["token"]}
        request = self.factory.get('/artitems/me/followings/', **header, content_type='application/json')
        response = artitems_of_followings(request)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.data, list))
        artitem = response.data[0]
        self.compare_equality(created, artitem)



    def compare_equality(self, created, artitem):
        expected = {
            "title": created["title"],
            "description": created["description"],
            "username": created["owner"]["username"],
            "category": created["category"],
            "likes": created["likes"],
            "number_of_views": created["number_of_views"],
            "tags": [t["id"] for t in created["tags"]]   
        }
        actual = {
            "title": artitem["title"],
            "description": artitem["description"],
            "username": artitem["owner"]["username"],
            "category": artitem["category"],
            "likes": artitem["likes"],
            "number_of_views": artitem["number_of_views"],
            "tags": [t["id"] for t in artitem["tags"]]   
        }
        self.assertEqual(actual, expected)


    def tearDown(self):
        # cleaning up after the test
        print("TestArtItem:setUp_:begin")

        # do something
        print("TestArtItem:setUp_:end")