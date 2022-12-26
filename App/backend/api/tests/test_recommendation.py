from django.test import TestCase, RequestFactory
from faker import Faker

from ..models.user import User
from ..models.artitem import ArtItem, Tag, LikeArtItem
from ..serializers.serializers import ArtItem, ArtItemSerializer
from django.contrib.auth.models import AnonymousUser, User
from ..views.artitem import *
from ..views.auth import *
from .utils import utils
from ..views.recommendation import *
from history.models import History
from django.contrib.contenttypes.models import ContentType
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
        self.factory = RequestFactory()
        self.user = utils.register()
        self.user2 = utils.register()
        self.user11 = utils.register()
        self.user22 = utils.register()
        # do something
        print("TestArtItem:setUp_:end")

    # def test_artitem_creation(self):
    #     user = User.objects.create(username = self.faker.unique.word(), password = self.faker.password(), email = f"{self.faker.first_name()}.{self.faker.last_name()}@{self.faker.domain_name()}")
    #     artitem = ArtItem.objects.create(title= self.faker.word(), description = self.faker.paragraph(nb_sentences=3), owner = user)

    #     self.assertTrue(isinstance(artitem, ArtItem))
    #     self.assertEqual(artitem.__str__(), "Art item: " + artitem.title)
    #     self.assertEqual(artitem.artitem_image, 'artitem/defaultart.jpg')

    # def test_artitem_deletion_cascaded(self):
    #     user = User.objects.create(username = self.faker.unique.word(), password = self.faker.password(), email = f"{self.faker.first_name()}.{self.faker.last_name()}@{self.faker.domain_name()}")
    #     artitem = ArtItem.objects.create(title= self.faker.word(), description = self.faker.paragraph(nb_sentences=3), owner = user)
    #     id = artitem.id

    #     user.delete()
    #     self.assertFalse(ArtItem.objects.filter(id=id))   # empty list is False   

    # def test_artitem_deletion(self):
    #     user = User.objects.create(username = self.faker.unique.word(), password = self.faker.password(), email = f"{self.faker.first_name()}.{self.faker.last_name()}@{self.faker.domain_name()}")
    #     artitem = ArtItem.objects.create(title= self.faker.word(), description = self.faker.paragraph(nb_sentences=3), owner = user)
    #     title = artitem.title


    #     artitem.delete()
    #     self.assertFalse(ArtItem.objects.filter(title=title))   # empty list is False   
    

    # GET Test | Tests if art item recommendation function will recommend a less popular art item that is in user's interest, as it is supposed to.
    def test_recommendation_artitem(self):
        #user is self.user
        #user1 is will own all art items

        user1 = User.objects.create(username = self.faker.unique.word(), password = self.faker.password(), email = f"{self.faker.first_name()}.{self.faker.last_name()}@{self.faker.domain_name()}")
        user3 = User.objects.create(username = self.faker.unique.word(), password = self.faker.password(), email = f"{self.faker.first_name()}.{self.faker.last_name()}@{self.faker.domain_name()}")
        artitem = []
        like = []
        #0
        artitem.append(ArtItem.objects.create(title= self.faker.word(), description = self.faker.paragraph(nb_sentences=3), owner = user1, category='DR'))
        #1
        artitem.append(ArtItem.objects.create(title= self.faker.word(), description = self.faker.paragraph(nb_sentences=3), owner = user1, category='DR'))
        artitem[0].updatePopularity()
        artitem[1].updatePopularity()

        artitemliked = ArtItem.objects.create(title= self.faker.word(), description = self.faker.paragraph(nb_sentences=3), owner = user1, category='DR')
        likeliked = LikeArtItem.objects.create(user=User.objects.get(id=self.user['user']['id']), artitem=artitemliked)

        userinterest = UserInterest.objects.get(user = User.objects.get(id=self.user['user']['id']))
        userinterest.updateInterest(artitemliked.category, 2)

        # print(artitem[0].id)
        # print(artitem[1].id)

        # print("user interest")
        # print(userinterest.first)
        # print(userinterest.second)
        # print(userinterest.third)


        for i in range(2, 20):
            artitem.append(ArtItem.objects.create(title= self.faker.word(), description = self.faker.paragraph(nb_sentences=3), owner = user1, category='SC'))
            like.append(LikeArtItem.objects.create(user=user3, artitem=artitem[i]))
            artitem[i].updatePopularity()


        header = {"HTTP_AUTHORIZATION": "Token " + self.user["token"]}
        request = self.factory.get('/recommendation/artitems/', **header, content_type='application/json')
        response = RecommendArtItemView(request)
        
        actual = response.data
        # print("actual is ")
        # print(actual)

        # print('printing')
        # print(actual['artitems'][0])
        # print(actual['artitems'][0]['id'])

        self.assertEqual(response.status_code, 200)
        self.assertEqual(artitem[0].id, actual['artitems'][0]['id'])
        self.assertTrue(artitem[1].id in actual['artitems'][x]['id'] for x in actual)


# GET Test | Tests if art item recommendation function will stop recommending an art item once it has been viewed, that is in user's interest, as it is supposed to.
    def test_recommendation_artitem_viewed(self):

        user1 = User.objects.create(username = self.faker.unique.word(), password = self.faker.password(), email = f"{self.faker.first_name()}.{self.faker.last_name()}@{self.faker.domain_name()}")
        user3 = User.objects.create(username = self.faker.unique.word(), password = self.faker.password(), email = f"{self.faker.first_name()}.{self.faker.last_name()}@{self.faker.domain_name()}")
        artitem = []
        like = []
        #0
        artitem.append(ArtItem.objects.create(title= self.faker.word(), description = self.faker.paragraph(nb_sentences=3), owner = user1, category='DR'))
        #1
        artitem.append(ArtItem.objects.create(title= self.faker.word(), description = self.faker.paragraph(nb_sentences=3), owner = user1, category='DR'))
        artitem[0].updatePopularity()
        artitem[1].updatePopularity()

        artitemliked = ArtItem.objects.create(title= self.faker.word(), description = self.faker.paragraph(nb_sentences=3), owner = user1, category='DR')
        likeliked = LikeArtItem.objects.create(user=User.objects.get(id=self.user['user']['id']), artitem=artitemliked)

        userinterest = UserInterest.objects.get(user = User.objects.get(id=self.user['user']['id']))
        userinterest.updateInterest(artitemliked.category, 2)


        for i in range(2, 20):
            artitem.append(ArtItem.objects.create(title= self.faker.word(), description = self.faker.paragraph(nb_sentences=3), owner = user1, category='SC'))
            like.append(LikeArtItem.objects.create(user=user3, artitem=artitem[i]))
            artitem[i].updatePopularity()


        header = {"HTTP_AUTHORIZATION": "Token " + self.user["token"]}
        request = self.factory.get('/recommendation/artitems/', **header, content_type='application/json')
        response = RecommendArtItemView(request)
        
        actual = response.data
        # print("actual is ")
        # print(actual)

        # print('printing')
        # print(actual['artitems'][0])
        # print(actual['artitems'][0]['id'])

        self.assertEqual(response.status_code, 200)
        self.assertEqual(artitem[0].id, actual['artitems'][0]['id'])
        self.assertTrue(artitem[1].id in actual['artitems'][x]['id'] for x in actual)

        history = History.objects.create(user=User.objects.get(id=self.user['user']['id']), content_type=ContentType.objects.get_for_model(ArtItem), object_id=artitem[1].id, is_art=True, art_id=artitem[1].id)
        #print(history)

        header = {"HTTP_AUTHORIZATION": "Token " + self.user["token"]}
        request = self.factory.get('/recommendation/artitems/', **header, content_type='application/json')
        response = RecommendArtItemView(request)
        actual = response.data
        #print(actual)

        self.assertTrue(artitem[1].id not in actual['artitems'][x]['id'] for x in actual)


# GET Test | Tests if art item recommendation function will recommend popular art items even if the user is not logged in, as it is supposed to.
    def test_recommendation_artitem_anonymous(self):
        #user is self.user
        #user1 is will own all art items

        user1 = User.objects.create(username = self.faker.unique.word(), password = self.faker.password(), email = f"{self.faker.first_name()}.{self.faker.last_name()}@{self.faker.domain_name()}")
        user3 = User.objects.create(username = self.faker.unique.word(), password = self.faker.password(), email = f"{self.faker.first_name()}.{self.faker.last_name()}@{self.faker.domain_name()}")
        artitem = []
        like = []


        for i in range(0, 30):
            artitem.append(ArtItem.objects.create(title= self.faker.word(), description = self.faker.paragraph(nb_sentences=3), owner = user1, category='SC'))
            like.append(LikeArtItem.objects.create(user=user3, artitem=artitem[i]))
            artitem[i].updatePopularity()


        #1
        myart = ArtItem.objects.create(title= self.faker.word(), description = self.faker.paragraph(nb_sentences=3), owner = user1, category='DR')
        artitem.append(myart)
        for i in range(0, 100):
            newuser = User.objects.create(username = self.faker.unique.word(), password = self.faker.password(), email = f"{self.faker.first_name()}.{self.faker.last_name()}@{self.faker.domain_name()}")
        
            like.append(LikeArtItem.objects.create(user=newuser, artitem=myart))
        myart.updatePopularity()

        request = self.factory.get('/recommendation/artitems/', content_type='application/json')
        response = RecommendArtItemView(request)
        
        actual = response.data

        #print(myart.id)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(myart.id in actual['artitems'][x]['id'] for x in actual)


# GET Test | Tests if exhibition recommendation function will recommend popular art items even if the user is not logged in, as it is supposed to.
    def test_recommendation_exhibition_anonymous(self):
        #user is self.user
        #user1 is will own all art items

        exhibition = []


        for i in range(0, 20):
            exhibition.append(utils.create_offline_exhibition(self.user11, self.user22))

        print(exhibition[19])

        myexh = OfflineExhibition.objects.get(id=exhibition[19]['id'])

        myexh.popularity = 2000
        myexh.save()

        request = self.factory.get('/recommendation/exhibitions/', content_type='application/json')
        response = RecommendExhibitionView(request)
        
        actual = response.data

        #print(myart.id)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(20 in actual['exhibitions'][x]['id'] for x in actual)
        #self.assertEqual(len(actual['exhibitions']), 16)



    def tearDown(self):
        # cleaning up after the test
        print("TestArtItem:tearDown_:begin")

        # do something
        print("TestArtItem:tearDown_:end")