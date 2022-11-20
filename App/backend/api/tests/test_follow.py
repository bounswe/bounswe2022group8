from django.test import TestCase
from faker import Faker

from ..models.user import User, Follow
from ..models.artitem import ArtItem
from ..serializers.follow import FollowSerializer
"""
setUp() function is like a constructor for our test. It creates some mock data.
Thanks to the django.test, mock data is deleted automatically after the test, you do not have to worry about your database.
tearDown() function is like a destructor, it deletes the objects.
"""


class FollowTest(TestCase):
    # preparing to test
    def setUp(self):
        # setting up for the test
        print("TestFollow:setUp_:begin")
        self.faker = Faker()
        self.serializer = FollowSerializer()

        # do something
        print("TestFollow:setUp_:end")

    def test_follow_creation(self):
        from_user = User.objects.create(username = self.faker.unique.word(), password = self.faker.password(), email = f"{self.faker.first_name()}.{self.faker.last_name()}@{self.faker.domain_name()}")
        to_user = User.objects.create(username = self.faker.unique.word(), password = self.faker.password(), email = f"{self.faker.first_name()}.{self.faker.last_name()}@{self.faker.domain_name()}")

        follow = Follow.objects.create(from_user=from_user, to_user=to_user)


        self.assertTrue(isinstance(follow, Follow))
        self.assertEqual(follow.__str__(), str(from_user) + " follows " + str(to_user))

    def test_follow_deletion_cascaded(self):
        from_user = User.objects.create(username = self.faker.unique.word(), password = self.faker.password(), email = f"{self.faker.first_name()}.{self.faker.last_name()}@{self.faker.domain_name()}")
        to_user = User.objects.create(username = self.faker.unique.word(), password = self.faker.password(), email = f"{self.faker.first_name()}.{self.faker.last_name()}@{self.faker.domain_name()}")

        follow = Follow.objects.create(from_user=from_user, to_user=to_user)

        from_user.delete()
        
        self.assertFalse(User.objects.filter(id=from_user.id))        
        self.assertFalse(Follow.objects.filter(id=follow.id))   # empty list is False
        self.assertFalse([follow.from_user for follow in Follow.objects.filter(to_user=to_user)])
    
    def test_follow_artitems(self):
        from_user = User.objects.create(username = self.faker.unique.word(), password = self.faker.password(), email = f"{self.faker.first_name()}.{self.faker.last_name()}@{self.faker.domain_name()}")
        to_user = User.objects.create(username = self.faker.unique.word(), password = self.faker.password(), email = f"{self.faker.first_name()}.{self.faker.last_name()}@{self.faker.domain_name()}")
        artitem1= ArtItem.objects.create(title= self.faker.word(), description = self.faker.paragraph(nb_sentences=3), owner = to_user)
        artitem2 = ArtItem.objects.create(title= self.faker.word(), description = self.faker.paragraph(nb_sentences=3), owner = to_user)
        Follow.objects.create(from_user=from_user, to_user=to_user)

        followings = [follow.to_user for follow in Follow.objects.filter(from_user=from_user)]
        artitems = ArtItem.objects.filter(owner__in=followings)

        self.assertEqual(list(artitems), [artitem2, artitem1])


    def tearDown(self):
        # cleaning up after the test
        print("TestArtItem:setUp_:begin")

        # do something
        print("TestArtItem:setUp_:end")
