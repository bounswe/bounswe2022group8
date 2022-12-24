from django.test import TestCase, RequestFactory
from faker import Faker

from ..models.user import User
from ..models.artitem import ArtItem
from ..serializers.serializers import ArtItem, ArtItemSerializer, SimpleUserSerializer
from ..views.exhibition import validate_ids, fetch_image, create_offline_exhibition
from ..utils import ArtItemStorage
from django.core.files.base import ContentFile
from .utils import utils
"""
setUp() function is like a constructor for our test. It creates some mock data.
Thanks to the django.test, mock data is deleted automatically after the test, you do not have to worry about your database.
tearDown() function is like a destructor, it deletes the objects.
"""
class ArtItemTest(TestCase):
    # preparing to test
    def setUp(self):
        # setting up for the test
        print("TestExhibition:setUp_:begin")
        self.faker = Faker()
        self.factory = RequestFactory()
        self.user1 = utils.register()
        self.user2 = utils.register()
        # do something
        print("TestExhibition:setUp_:end")

    def test_id_validation(self):
        # test the helper function that checks if given IDs (artitem_gallery) are valid.
        user1 = User.objects.create(username = self.faker.unique.word(), password = self.faker.password(), email = f"{self.faker.first_name()}.{self.faker.last_name()}@{self.faker.domain_name()}")
        user2 = User.objects.create(username = self.faker.unique.word(), password = self.faker.password(), email = f"{self.faker.first_name()}.{self.faker.last_name()}@{self.faker.domain_name()}")

        artitem1 = ArtItem.objects.create(title= self.faker.word(), description = self.faker.paragraph(nb_sentences=3), owner = user1) # id = 4
        artitem2 = ArtItem.objects.create(title= self.faker.word(), description = self.faker.paragraph(nb_sentences=3), owner = user1) # id = 5
        artitem3 = ArtItem.objects.create(title= self.faker.word(), description = self.faker.paragraph(nb_sentences=3), owner = user1) # id = 6
        artitem4 = ArtItem.objects.create(title= self.faker.word(), description = self.faker.paragraph(nb_sentences=3), owner = user2) # id = 7
        artitem5 = ArtItem.objects.create(title= self.faker.word(), description = self.faker.paragraph(nb_sentences=3), owner = user2) # id = 8

        self.assertTrue(validate_ids([artitem1.id], user1.id))
        self.assertTrue(validate_ids([artitem1.id, artitem2.id], user1.id))
        self.assertTrue(validate_ids([artitem4.id, artitem5.id], user2.id))
        self.assertFalse(validate_ids([artitem3.id, artitem4.id], user1.id))
        self.assertFalse(validate_ids([artitem2.id], user2.id))
        self.assertFalse(validate_ids([artitem5.id], user1.id))

    def test_fetch_image(self):
        # test fetch_image function
        user = User.objects.create(username = self.faker.unique.word(), password = self.faker.password(), email = f"{self.faker.first_name()}.{self.faker.last_name()}@{self.faker.domain_name()}")
        artitem_image_storage = ArtItemStorage()
        artitemdata = {}
        artitem_data = fetch_image(artitemdata, artitem_image_storage, utils.BASE64, user)

        self.assertEqual(artitem_data["artitem_path"], "artitem/artitem-1.png")
        self.assertTrue(isinstance(artitem_data["artitem_image"], ContentFile))

    # POST offline exhibition
    def test_create_offline_exhibition(self):
        data = {
            "title": self.faker.pystr(min_chars = 10),
            "description": self.faker.paragraph(nb_sentences=3),
            "start_date": "2020-12-08T13:00:00.000Z",
            "end_date": "2020-12-10T13:00:00.000Z",
            "poster": utils.BASE64,
            "collaborators": [self.user2['user']['id']],
            "city": self.faker.city(),
            "country": self.faker.country(),
            "address": self.faker.address(),
            "longitude": self.faker.longitude(),
            "latitude": self.faker.latitude()
        }

        header = {"HTTP_AUTHORIZATION": "Token " + self.user1["token"]}
        request = self.factory.post('exhibitions/me/offline/', data, **header, content_type='application/json')
        response = create_offline_exhibition(request) 
        actual = response.data
        self.assertEqual(response.status_code, 201)

        user = User.objects.get(pk=self.user1['user']['id'])
        expected_user = SimpleUserSerializer(user).data
        actual_user = actual['owner']
        self.assertEqual(actual_user, expected_user)

        collaborator = User.objects.get(pk=self.user2['user']['id'])
        expected_collaborator = SimpleUserSerializer(collaborator).data
        actual_collaborator = actual['collaborators'][0]
        self.assertEqual(actual_collaborator, expected_collaborator)

        actual_data = {
            "title": actual['title'],
            "description": actual['description'],
            "city": actual['city'],
            "country": actual['country'],
            "address": actual['address'],
            "longitude": actual['longitude'],
            "latitude": actual['latitude'],
            "status": actual['status'] 
        }
        data.pop('poster')
        data.pop('collaborators')
        data.pop('start_date')
        data.pop('end_date')
        data['status'] = "Finished"
        data['longitude'] = float (data['longitude'])
        data['latitude'] = float (data['latitude'])
    

        self.assertEqual(actual_data, data)

    # POST online exhibition
    def test_create_offline_exhibition_invalid(self):
        data = {
            "title": self.faker.pystr(min_chars = 10),
            "description": self.faker.paragraph(nb_sentences=3),
            "start_date": "2022-12-08T13:00:00.000Z",
            "end_date": "2020-12-10T13:00:00.000Z",
            "poster": utils.BASE64,
            "collaborators": [self.user2['user']['id']],
            "city": self.faker.city(),
            "country": self.faker.country(),
            "address": self.faker.address(),
            "longitude": self.faker.longitude(),
            "latitude": self.faker.latitude()
        }

        header = {"HTTP_AUTHORIZATION": "Token " + self.user1["token"]}
        request = self.factory.post('exhibitions/me/offline/', data, **header, content_type='application/json')
        response = create_offline_exhibition(request) 
        actual = response.data
        self.assertEqual(response.status_code, 400)


    def tearDown(self):
        # cleaning up after the test
        print("TestExhibition:setUp_:begin")

        # do something
        print("TestExhibition:setUp_:end")
