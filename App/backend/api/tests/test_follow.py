from django.test import TestCase, RequestFactory
from faker import Faker

from ..views.follow import *
from ..models.user import User, Follow
from ..models.artitem import ArtItem
from ..serializers.follow import FollowSerializer
from .utils import utils
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
        self.factory = RequestFactory()

        self.user1 = utils.register()
        self.user2 = utils.register()

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

    # POST test
    def test_follow(self):
        header = {"HTTP_AUTHORIZATION": "Token " + self.user1["token"]}
        request = self.factory.post('/users/follow/', **header, content_type='application/json')
        response = follow_user(request, self.user2['user']['id']) # user1 follows user2
 
        expected = {
            "from_user": self.user1['user']['id'],
            "to_user": self.user2['user']['id'],
        }
        actual = {
            "from_user": response.data['from_user'],
            "to_user": response.data['to_user'], 
        }

        self.assertEqual(response.status_code, 201)
        self.assertEqual(actual, expected)

    # POST + GET my followings test
    def test_get_my_followings(self):
        utils.create_follow(self.user1, self.user2)

        header = {"HTTP_AUTHORIZATION": "Token " + self.user1["token"]}
        request = self.factory.get('/users/me/followings/', **header, content_type='application/json')
        self.helper_test(self.user1, self.user2, get_my_followings, request) # user1 follows user2

    # POST + GET my followers test
    def test_get_my_followers(self):
        utils.create_follow(self.user2, self.user1)  # user2 follows user1

        header = {"HTTP_AUTHORIZATION": "Token " + self.user1["token"]}
        request = self.factory.get('/users/me/followers/', **header, content_type='application/json')
        self.helper_test(self.user1, self.user2, get_my_followers, request) # user1 follows user2
        

    # POST + GET user followers test
    def test_get_user_followers(self):
        utils.create_follow(self.user2, self.user1)  # user2 follows user1

        request = self.factory.get('/users/followers/', content_type='application/json')
        self.helper_test(self.user1, self.user2, get_followers, request, self.user1['user']['id'],) # user1 follows user2

    # POST + GET user followers test
    def test_get_user_followings(self):
        utils.create_follow(self.user1, self.user2)  # user2 follows user1

        request = self.factory.get('/users/followings/', content_type='application/json')
        self.helper_test(self.user1, self.user2, get_followings, request, self.user1['user']['id'],) # user1 follows user2
    
    
    def helper_test(self, _, user2, f, request, qid = None):  # user1 follows user2
        response = f(request) if not qid else f(request, qid)
        actual_data = response.data[0]
 
        expected = {
            "id": user2['user']['id'],
            "username": user2['user']['username'],
            "is_level2": False,
            "name": "",
            "surname": "",
            "email": user2['user']['email'],
            "profile_path": "avatar/default.png"
        }
        actual = {
            "id": actual_data['id'],
            "username": actual_data['username'],
            "is_level2": actual_data['is_level2'],
            "name": actual_data['name'],
            "surname": actual_data['surname'],
            "email": actual_data['email'],
            "profile_path": actual_data["profile_path"]
        }

        self.assertEqual(response.status_code, 200)
        self.assertEqual(actual, expected)


    def test_unfollow(self):
        utils.create_follow(self.user1, self.user2)  # user1 follows user2
        user3 = utils.register()

        header = {"HTTP_AUTHORIZATION": "Token " + self.user1["token"]}
        request = self.factory.delete('/users/unfollow/', **header, content_type='application/json')
        response = unfollow_user(request, self.user2['user']['id']) # user1 follows user2

        self.assertEqual(response.status_code, 204)
        response = unfollow_user(request, user3['user']['id']) # attempt to unfollow user3
        self.assertEqual(response.status_code, 400)
        response = unfollow_user(request, -1) # attempt to unfollow user3
        self.assertEqual(response.status_code, 404)

    def tearDown(self):
        # cleaning up after the test
        print("TestArtItem:setUp_:begin")

        # do something
        print("TestArtItem:setUp_:end")
