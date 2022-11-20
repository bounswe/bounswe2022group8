from django.test import TestCase
from faker import Faker

from ..models.user import User
from ..models.artitem import ArtItem
from ..serializers.serializers import ArtItem, ArtItemSerializer
"""
setUp() function is like a constructor for our test. It creates some mock data.
Thanks to the django.test, mock data is deleted automatically after the test, you do not have to worry about your database.
tearDown() function is like a destructor, it deletes the objects.
"""

class ArtItemTest(TestCase):
    # preparing to test
    def setUp(self):
        # setting up for the test
        print("TestArtItem:setUp_:begin")
        self.faker = Faker()
        self.serializer = ArtItemSerializer()

        # do something
        print("TestArtItem:setUp_:end")

    def test_artitem_creation(self):
        user = User.objects.create(username = self.faker.unique.word(), password = self.faker.password())
        artitem = ArtItem.objects.create(title= self.faker.word(), description = self.faker.paragraph(nb_sentences=3), owner = user)

        self.assertTrue(isinstance(artitem, ArtItem))
        self.assertEqual(artitem.__str__(), "Art item: " + artitem.title)
        self.assertEqual(artitem.artitem_image, 'artitem/defaultart.jpg')

    def test_artitem_deletion_cascaded(self):
        user = User.objects.create(username = self.faker.unique.word(), password = self.faker.password())
        artitem = ArtItem.objects.create(title= self.faker.word(), description = self.faker.paragraph(nb_sentences=3), owner = user)
        id = artitem.id

        user.delete()
        self.assertFalse(ArtItem.objects.filter(id=id))   # empty list is False   

    def test_artitem_deletion(self):
        user = User.objects.create(username = self.faker.unique.word(), password = self.faker.password())
        artitem = ArtItem.objects.create(title= self.faker.word(), description = self.faker.paragraph(nb_sentences=3), owner = user)
        title = artitem.title


        artitem.delete()
        self.assertFalse(ArtItem.objects.filter(title=title))   # empty list is False   


    def tearDown(self):
        # cleaning up after the test
        print("TestArtItem:setUp_:begin")

        # do something
        print("TestArtItem:setUp_:end")
