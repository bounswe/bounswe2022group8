from django.test import TestCase, RequestFactory
from faker import Faker

from ..models.user import User
from ..models.artitem import ArtItem
from ..serializers.serializers import ArtItem, SimpleUserSerializer, SimpleArtItemSerializer
from ..serializers.exhibition import SimpleExhibitionArtItemSerializer
from ..views.exhibition import validate_ids, fetch_image, create_offline_exhibition, create_online_exhibition, get_exhibitions, get_online_exhibitions_by_id, get_offline_exhibitions_by_userid, get_offline_exhibitions_by_id, get_online_exhibitions_by_userid
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
    def test_create_online_exhibition(self):
        image_from_gallery = utils.upload_an_image(self.user1)
        data = {
            "title": self.faker.pystr(min_chars = 10),
            "description": self.faker.paragraph(nb_sentences=3),
            "start_date": "2020-12-08T13:00:00.000Z",
            "end_date": "2020-12-10T13:00:00.000Z",
            "poster": utils.BASE64,
            "collaborators": [self.user2['user']['id']],
            "artitems_gallery": [image_from_gallery['id']],
            "artitems_upload": [{
                "title": self.faker.pystr(min_chars = 10),
                "description": self.faker.paragraph(nb_sentences=3),
                "category": "PT",
                "artitem_image": utils.BASE64
            }]
        }

        header = {"HTTP_AUTHORIZATION": "Token " + self.user1["token"]}
        request = self.factory.post('exhibitions/me/online/', data, **header, content_type='application/json')
        response = create_online_exhibition(request) 
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
            "status": actual['status'] 
        }
        expected_data = {
            "title": data['title'],
            "description": data['description'],
            "status": "Finished"           
        }

        self.assertEqual(actual_data, expected_data)
        self.assertTrue(isinstance(actual['artitems_gallery'], list))
        self.assertTrue(isinstance(actual['artitems_upload'], list))
        actual_artitem = actual['artitems_gallery'][0]

        self.assertEqual(actual_artitem, SimpleArtItemSerializer(ArtItem.objects.get(pk=image_from_gallery['id'])).data)

        actual_uploaded = actual['artitems_upload'][0]
        self.assertEqual(actual_uploaded, SimpleExhibitionArtItemSerializer(ArtItem.objects.get(title=data['artitems_upload'][0]['title'])).data)


    # GET all exhibitions
    def test_get_all_exhibitions(self):
        offline_exhibition = utils.create_offline_exhibition(self.user1, self.user2)
        online_exhibition, image_from_gallery = utils.create_online_exhibition(self.user1, self.user2)

        request = self.factory.get('exhibitions/', content_type='application/json')
        response = get_exhibitions(request) 
        actual = response.data
        self.assertEqual(response.status_code, 200)
        offline_exhibition = actual['Offline Exhibitions'][0]
        online_exhibition = actual['Virtual Exhibitions'][0]

        user = User.objects.get(pk=self.user1['user']['id'])
        expected_user = SimpleUserSerializer(user).data

        actual_user = offline_exhibition['owner']
        self.assertEqual(actual_user, expected_user)

        collaborator = User.objects.get(pk=self.user2['user']['id'])
        expected_collaborator = SimpleUserSerializer(collaborator).data
        actual_collaborator = offline_exhibition['collaborators'][0]
        self.assertEqual(actual_collaborator, expected_collaborator)

        self.assertTrue(isinstance(online_exhibition['artitems_gallery'], list))
        self.assertTrue(isinstance(online_exhibition['artitems_upload'], list))
        actual_artitem = online_exhibition['artitems_gallery'][0]
        self.assertEqual(actual_artitem, SimpleArtItemSerializer(ArtItem.objects.get(pk=image_from_gallery['id'])).data)

    # PUT online exhibition
    def test_collaborator_upload(self):
        online_exhibition, image_from_gallery = utils.create_online_exhibition(self.user1, self.user2, enddate = "2024-12-10T13:00:00.000Z") # self.user2 is a collaborator
        new_image = utils.upload_an_image(self.user2)
        data = {
            "title": self.faker.pystr(min_chars = 10),
            "description": self.faker.pystr(min_chars = 10),
            "add_via_gallery": [
                new_image['id']
            ],
            "add_via_upload": [
                {
                "title": self.faker.pystr(min_chars = 10),
                "description": self.faker.pystr(min_chars = 10),
                "category": "PH",
                "artitem_image": utils.BASE64
                }
            ],
            "remove": [
            image_from_gallery['id']
            ]
        }

        # user2 attempts to update an virtual exhibition in which he is a collaborator
        header = {"HTTP_AUTHORIZATION": "Token " + self.user2["token"]}
        request = self.factory.put('exhibitions/online/', data, **header, content_type='application/json')
        response = get_online_exhibitions_by_id(request, online_exhibition['id'])
        actual = response.data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(actual['title'], data['title'])
        self.assertEqual(actual['description'], data['description'])
        self.assertEqual(actual['artitems_gallery'][0], SimpleArtItemSerializer(ArtItem.objects.get(pk=new_image['id'])).data)

    # DELETE online exhibition + GET online exhibition by id + GET online exhibition by userid
    def test_delete_online_exhibition(self):
        user3 = utils.register()
        exh, _ = utils.create_online_exhibition(user3, self.user1)

        header = {"HTTP_AUTHORIZATION": "Token " + self.user2["token"]}
        request = self.factory.delete('exhibitions/online/', **header, content_type='application/json')
        response = get_online_exhibitions_by_id(request, exh['id'])

        self.assertEqual(response.status_code, 403) # Cannot delete other user's exhibition

        request = self.factory.delete('exhibitions/online/', **header, content_type='application/json')
        response = get_online_exhibitions_by_id(request, -1)
        self.assertEqual(response.status_code, 404) # Cannot delete a nonexisting exhibition

        header = {"HTTP_AUTHORIZATION": "Token " + user3["token"]}
        request = self.factory.delete('exhibitions/online/', **header, content_type='application/json')
        response = get_online_exhibitions_by_id(request, exh['id'])
        
        self.assertEqual(response.status_code, 204) # delete his own exhibition
        # let's try to get that exhibition with id
        request = self.factory.get('exhibitions/online/', **header, content_type='application/json')
        response = get_online_exhibitions_by_id(request, exh['id'])

        self.assertEqual(response.status_code, 404)

        # let's try to get all exhibitions of user3
        request = self.factory.get('exhibitions/users/online/', **header, content_type='application/json')
        response = get_online_exhibitions_by_userid(request, user3['user']['id'])

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])


    # DELETE offline exhibition + GET offline exhibition by id + GET offline exhibition by userid
    def test_delete_offline_exhibition(self):
        user3 = utils.register()
        exh = utils.create_offline_exhibition(user3, self.user1)

        header = {"HTTP_AUTHORIZATION": "Token " + self.user2["token"]}
        request = self.factory.delete('exhibitions/ofline/', **header, content_type='application/json')
        response = get_offline_exhibitions_by_id(request, exh['id'])

        self.assertEqual(response.status_code, 403) # Cannot delete other user's exhibition

        request = self.factory.delete('exhibitions/ofline/', **header, content_type='application/json')
        response = get_offline_exhibitions_by_id(request, -1)
        self.assertEqual(response.status_code, 404) # Cannot delete a nonexisting exhibition

        header = {"HTTP_AUTHORIZATION": "Token " + user3["token"]}
        request = self.factory.delete('exhibitions/ofline/', **header, content_type='application/json')
        response = get_offline_exhibitions_by_id(request, exh['id'])
        
        self.assertEqual(response.status_code, 204) # delete his own exhibition
        # let's try to get that exhibition with id
        request = self.factory.get('exhibitions/ofline/', **header, content_type='application/json')
        response = get_offline_exhibitions_by_id(request, exh['id'])

        self.assertEqual(response.status_code, 404)

        # let's try to get all exhibitions of user3
        request = self.factory.get('exhibitions/users/ofline/', **header, content_type='application/json')
        response = get_offline_exhibitions_by_userid(request, user3['user']['id'])

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])

    def tearDown(self):
        # cleaning up after the test
        print("TestExhibition:tearDown_:begin")

        # do something
        print("TestExhibition:tearDown_:end")
