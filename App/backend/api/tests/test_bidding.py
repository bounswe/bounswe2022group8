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
from ..views.bidding import *
from history.models import History
from django.contrib.contenttypes.models import ContentType
"""
setUp() function is like a constructor for our test. It creates some mock data.
Thanks to the django.test, mock data is deleted automatically after the test, you do not have to worry about your database.
tearDown() function is like a destructor, it deletes the objects.
"""

class BiddingTest(TestCase):
    # preparing to test
    def setUp(self):
        # setting up for the test
        print("TestBidding:setUp_:begin")
        self.faker = Faker()
        self.factory = RequestFactory()
        self.user = utils.register()
        self.user2 = utils.register()
        self.user11 = utils.register()
        self.user22 = utils.register()
        # do something
        print("TestBidding:setUp_:end")

    

    # PUT Test | Tests if art item sale status can be sucessfully changed.
    def test_open_item_for_sale(self):
        artitem = ArtItem.objects.create(title= self.faker.word(), description = self.faker.paragraph(nb_sentences=3), owner = User.objects.get(id=self.user11['user']['id']), category='DR')
        
        data = {"sale_status": ArtItem.SaleStatus.FORSALE.value, "minimum_price": 200.5}

        header = {"HTTP_AUTHORIZATION": "Token " + self.user11["token"]}
        request = self.factory.put('/artitems/1/bids/', data, **header, content_type='application/json')
        response = BidArtItemView(request, artitem.id)
        
        actual = response.data

        resp = {
                "detail": "The art item is successfully put on sale."
                }

        #print(artitem.sale_status)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(resp, actual)

    # POST Test | Tests if user can successfully bid on art item.
    def test_bid_on_art_item(self):
        artitem = ArtItem.objects.create(title= self.faker.word(), description = self.faker.paragraph(nb_sentences=3), owner = User.objects.get(id=self.user11['user']['id']), category='DR')
        
        artitem.sale_status = ArtItem.SaleStatus.FORSALE
        artitem.save()

        data = {
                "amount": 568.5,
                "deadline": "2032-12-20T18:58:15.643Z"
                }
        header = {"HTTP_AUTHORIZATION": "Token " + self.user22["token"]}
        request = self.factory.post('/artitems/1/bids/', data, **header, content_type='application/json')
        response = BidArtItemView(request, artitem.id)
        
        actual = response.data

        #print(actual)


        self.assertEqual(response.status_code, 201)
        self.assertEqual(actual['artitem']['id'], artitem.id)
        self.assertEqual(actual['amount'], 568.5)

    # POST Test | Tests if user can successfully bid on art item when item is not for sale, expected output false.
    def test_bid_on_art_item_fail(self):
        artitem = ArtItem.objects.create(title= self.faker.word(), description = self.faker.paragraph(nb_sentences=3), owner = User.objects.get(id=self.user11['user']['id']), category='DR')
        



        data = {
                "amount": 568.5,
                "deadline": "2032-12-20T18:58:15.643Z"
                }


        header = {"HTTP_AUTHORIZATION": "Token " + self.user22["token"]}
        request = self.factory.post('/artitems/1/bids/', data, **header, content_type='application/json')
        response = BidArtItemView(request, artitem.id)
        
        actual = response.data

        #print(actual)

        data = {
                "detail": "Sorry, this art item is not for sale."
                }


        self.assertEqual(response.status_code, 400)
        self.assertEqual(actual, data)


       # GET Test | Tests if user can successfully get all bids on art item.
    def test_get_all_bids_on_art_item(self):
        artitem = ArtItem.objects.create(title= self.faker.word(), description = self.faker.paragraph(nb_sentences=3), owner = User.objects.get(id=self.user11['user']['id']), category='DR')
        
        artitem.sale_status = ArtItem.SaleStatus.FORSALE
        artitem.save()

        mybid = Bid.objects.create(buyer=User.objects.get(id=self.user22['user']['id']), artitem=artitem, amount=568.5, deadline="2032-12-20T18:58:15.643Z")


        header = {"HTTP_AUTHORIZATION": "Token " + self.user11["token"]}
        request = self.factory.get('/artitems/1/bids/', **header, content_type='application/json')
        response = BidArtItemView(request, artitem.id)
        
        actual = response.data

        #print(actual)


        self.assertEqual(response.status_code, 200)
        self.assertEqual(actual['bids'][0]['artitem']['id'], artitem.id)
        self.assertEqual(actual['bids'][0]['amount'], 568.5)

    # GET Test | Tests if user can successfully get all bids on art item, fail case.
    def test_get_bids_on_art_item_fail(self):
        artitem = ArtItem.objects.create(title= self.faker.word(), description = self.faker.paragraph(nb_sentences=3), owner = User.objects.get(id=self.user11['user']['id']), category='DR')
        
        artitem.sale_status = ArtItem.SaleStatus.FORSALE
        artitem.save()

        mybid = Bid.objects.create(buyer=User.objects.get(id=self.user22['user']['id']), artitem=artitem, amount=568.5, deadline="2032-12-20T18:58:15.643Z")


        header = {"HTTP_AUTHORIZATION": "Token " + self.user22["token"]}
        request = self.factory.get('/artitems/1/bids/', **header, content_type='application/json')
        response = BidArtItemView(request, artitem.id)
        
        actual = response.data

        #print(actual)

        data = {
                "detail": "Only the owner can view art item bids."
                }


        self.assertEqual(response.status_code, 403)
        self.assertEqual(actual, data)

    # PUT Test | Tests if user can successfully reply to bid on art item.
    def test_reply_to_bid(self):
        artitem = ArtItem.objects.create(title= self.faker.word(), description = self.faker.paragraph(nb_sentences=3), owner = User.objects.get(id=self.user11['user']['id']), category='DR')
        
        artitem.sale_status = ArtItem.SaleStatus.FORSALE
        artitem.save()

        mybid = Bid.objects.create(buyer=User.objects.get(id=self.user22['user']['id']), artitem=artitem, amount=568.5, deadline="2032-12-20T18:58:15.643Z")

        mydata = {
                "response": "AC"
                }

        header = {"HTTP_AUTHORIZATION": "Token " + self.user11["token"]}
        request = self.factory.put('/artitems/bids/1/', mydata, **header, content_type='application/json')
        response = BidView(request, mybid.id)
        
        actual = response.data

        #print(actual)

        data = {
                "detail": "Successfully accepted the bid."
                }


        self.assertEqual(response.status_code, 200)
        self.assertEqual(actual, data)

        # GET Test | Tests if user can successfully get a bid on art item.
    def test_get_bid(self):
        artitem = ArtItem.objects.create(title= self.faker.word(), description = self.faker.paragraph(nb_sentences=3), owner = User.objects.get(id=self.user11['user']['id']), category='DR')
        
        artitem.sale_status = ArtItem.SaleStatus.FORSALE
        artitem.save()

        mybid = Bid.objects.create(buyer=User.objects.get(id=self.user22['user']['id']), artitem=artitem, amount=568.5, deadline="2032-12-20T18:58:15.643Z")



        header = {"HTTP_AUTHORIZATION": "Token " + self.user11["token"]}
        request = self.factory.get('/artitems/bids/1/', **header, content_type='application/json')
        response = BidView(request, mybid.id)
        
        actual = response.data

        #print(actual)


        self.assertEqual(response.status_code, 200)
        self.assertEqual(actual['id'], mybid.id)

    def tearDown(self):
        # cleaning up after the test
        print("TestBidding:tearDown_:begin")

        # do something
        print("TestBidding:tearDown_:end")