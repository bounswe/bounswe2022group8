from django.test import TestCase
from faker import Faker

from ..models.user import User
from ..models.artitem import ArtItem
from ..models.exhibition import ExhibitionArtItem
from ..serializers.serializers import ArtItem, ArtItemSerializer
from ..views.exhibition import validate_ids, fetch_image
from ..utils import ArtItemStorage
from django.core.files.base import ContentFile
"""
setUp() function is like a constructor for our test. It creates some mock data.
Thanks to the django.test, mock data is deleted automatically after the test, you do not have to worry about your database.
tearDown() function is like a destructor, it deletes the objects.
"""
test_base64 = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVQYV2NgYAAAAAMAAWgmWQ0AAAAASUVORK5CYII="

class ArtItemTest(TestCase):
    # preparing to test
    def setUp(self):
        # setting up for the test
        print("TestExhibition:setUp_:begin")
        self.faker = Faker()

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

        self.assertTrue(validate_ids([4, 5], user1.id))
        self.assertTrue(validate_ids([6], user1.id))
        self.assertTrue(validate_ids([7, 8], user2.id))
        self.assertFalse(validate_ids([2, 4], user1.id))
        self.assertFalse(validate_ids([2, 4], user2.id))
        self.assertFalse(validate_ids([9], user2.id))

    def test_fetch_image(self):
        # test fetch_image function

        artitem_image_storage = ArtItemStorage()
        artitemdata = {}
        artitem_data = fetch_image(artitemdata, artitem_image_storage, test_base64)

        self.assertEqual(artitem_data["artitem_path"], "artitem/artitem-1.png")
        self.assertTrue(isinstance(artitem_data["artitem_image"], ContentFile))

    def tearDown(self):
        # cleaning up after the test
        print("TestExhibition:setUp_:begin")

        # do something
        print("TestExhibition:setUp_:end")
