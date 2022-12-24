from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..serializers.serializers import BidSerializer
from ..serializers.bidding import bidPostSerializer, bidUpdateSerializer, artItemBidUpdateSerializer
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from ..models.user import User
from ..models.artitem import ArtItem, Bid, NewBids
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.contrib.auth.models import AnonymousUser
import datetime
from django.utils.timezone import make_aware
from dateutil import parser



@swagger_auto_schema(
    method='GET',
    operation_description="This endpoint with GET request returns all of the bids on an art item. Authentication is required. Only the owner of the art item can call this.",
    operation_summary="Get all bids on an art item.",
    tags=['bids'],
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Successfully got the art item bids.",
            examples={
                "application/json": {
                    "bids": [
                        {
                            "id": 1,
                            "artitem": {
                                "id": 21,
                                "title": "a3",
                                "category": "OT",
                                "artitem_path": "artitem/defaultart.jpg"
                            },
                            "buyer": {
                                "id": 3,
                                "username": "string2",
                                "profile_path": "avatar/default.png"
                            },
                            "amount": 10.0,
                            "created_at": "20-12-2022 17:42:34",
                            "deadline": "21-12-2022 17:42:33",
                            "accepted": "NR"
                        },
                        {
                            "id": 4,
                            "artitem": {
                                "id": 21,
                                "title": "a3",
                                "category": "OT",
                                "artitem_path": "artitem/defaultart.jpg"
                            },
                            "buyer": {
                                "id": 2,
                                "username": "string",
                                "profile_path": "avatar/default.png"
                            },
                            "amount": 3214.0,
                            "created_at": "20-12-2022 21:52:42",
                            "deadline": "22-12-2022 21:52:42",
                            "accepted": "NR"
                        }
                    ]
                }
            }
        ),
        status.HTTP_204_NO_CONTENT: openapi.Response(
            description="No bids on art item.",
            examples={
                "application/json": {
                    "detail": "The art item currently has 0 offers."
                },
            }
        ),
        status.HTTP_404_NOT_FOUND: openapi.Response(
            description="Wrong art item id.",
            examples={
                "application/json": {
                    "detail": "Art Item with given id does not exist."
                },
            }
        ),
        status.HTTP_403_FORBIDDEN: openapi.Response(
            description="User not authorized.",
            examples={
                "application/json": {
                    "detail": "Only the owner can view art item bids."
                },
            }
        ),
    }
)
@swagger_auto_schema(
    method='POST',
    request_body=bidPostSerializer,
    operation_description="This endpoint with POST request creates a bid on an art item. Authentication is required. Deadline has to be at least 10 minutes later than bidding time.",
    operation_summary="Bid on an art item.",
    tags=['bids'],
    responses={
        status.HTTP_201_CREATED: openapi.Response(
            description="Successfully bid on the art item.",
            examples={
                "application/json": {
                    "id": 6,
                    "artitem": {
                        "id": 23,
                        "title": "inspo",
                        "category": "PH",
                        "artitem_path": "artitem/defaultart.jpg"
                    },
                    "buyer": {
                        "id": 4,
                        "username": "string3",
                        "profile_path": "avatar/default.png"
                    },
                    "amount": 20.0,
                    "created_at": "20-12-2022 22:38:17",
                    "deadline": "20-12-2022 22:49:59",
                    "accepted": "NR"
                },
            }
        ),
        status.HTTP_400_BAD_REQUEST: openapi.Response(
            description="Not for sale.",
            examples={
                "application/json": {
                    "detail": "Sorry, this art item is not for sale."
                },
            }
        ),
        status.HTTP_403_FORBIDDEN: openapi.Response(
            description="Forbidden action.",
            examples={
                "application/json": {
                    "detail": "Seriously trying to bid on your own art? Sad."
                },
            }
        ),
    }
)
@swagger_auto_schema(
    method='PUT',
    request_body=artItemBidUpdateSerializer,
    operation_description="This endpoint with PUT request updates the sale_status and minimum_price of an art item. Authentication (+ownership) is required. minimum_price parameter is not required when closing the item to sale. ",
    operation_summary="Update sale status of an art item.",
    tags=['bids'],
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="The art item sale status is successfully updated.",
            examples={
                "application/json": {
                    "detail": "The art item is successfully closed to sale."
                },
            }
        ),
        status.HTTP_400_BAD_REQUEST: openapi.Response(
            description="Invalid sale status.",
            examples={
                "application/json": {
                    "detail": "The art item is already for sale."
                },
            }
        ),
        status.HTTP_403_FORBIDDEN: openapi.Response(
            description="Forbidden action.",
            examples={
                "application/json": {
                    "detail": "Only the owner can update sale status of art item."
                },
            }
        ),
    }
)
#@login_required
@api_view(['GET', 'POST', 'PUT'])
def BidArtItemView(request, artitemid):
    if request.user.is_authenticated:
        user = request.user
        data = request.data
        try:
            artitem = ArtItem.objects.get(id=artitemid)
        except ArtItem.DoesNotExist:
            message = {
                'detail': 'Art Item with given id does not exist.'}
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        if (request.method == "GET"):
            if(user == artitem.owner):
                try:

                    bids = Bid.objects.filter(artitem=artitem)
                    serializer = BidSerializer(bids, many=True)
                    resp = {"bids": serializer.data}
                    return Response(resp, status=status.HTTP_200_OK)
                except bids.count() == 0:
                    message = {
                        'detail': 'The art item currently has 0 offers.'}
                    return Response(message, status=status.HTTP_204_NO_CONTENT)
            else:
                message = {'detail': 'Only the owner can view art item bids.'}
                return Response(message, status=status.HTTP_403_FORBIDDEN)
        elif (request.method == "POST"):
            if(user == artitem.owner):
                message = {
                    'detail': 'Seriously trying to bid on your own art? Sad.'}
                return Response(message, status=status.HTTP_403_FORBIDDEN)
            else:
                if(artitem.sale_status == 'NS'):
                    message = {'detail': 'Sorry, this art item is not for sale.'}
                    return Response(message, status=status.HTTP_400_BAD_REQUEST)
                elif(artitem.sale_status == 'SO'):
                    message = {'detail': 'Sorry, this art item is already sold.'}
                    return Response(message, status=status.HTTP_400_BAD_REQUEST)
                else:
                    try:
                        previousBids = Bid.objects.filter(buyer=user, artitem=artitem, accepted='NR')
                        for bid in previousBids:
                            if(bid.deadline.replace(tzinfo=None) > datetime.datetime.now().replace(tzinfo=None)):
                                message = {
                                    'detail': 'You can not bid while you have a nonexpired bid on this art item.'}
                                return Response(message, status=status.HTTP_400_BAD_REQUEST)
                    except Bid.DoesNotExist:
                        pass
                    if(data["amount"] >= artitem.minimum_price):
                        #if(make_aware(datetime.datetime.strptime(data["deadline"], "yyyy'-'MM'-'dd'T'HH':'mm':'ss")) <= (datetime.datetime.now() + datetime.timedelta(minutes=10))):
                        if(parser.parse(data["deadline"]).replace(tzinfo=None) <= (datetime.datetime.now().replace(tzinfo=None) + datetime.timedelta(minutes=10))):
                            #print(datetime.datetime.now())
                            message = {'detail': 'Sorry, deadline has to be at least 10 minutes later than bidding time.'}
                            return Response(message, status=status.HTTP_400_BAD_REQUEST)
                        else:
                            data["buyer"] = request.user.id
                            data["artitem"] = artitemid
                            serializer = BidSerializer(data=data)
                            if serializer.is_valid():
                                serializer.save()
                                owner = artitem.owner
                                owner.new_bid_flag = True
                                newbids = NewBids.objects.get(user=owner)
                                newbids.new_bids.add(artitem)
                                newbids.save()
                                owner.save()
                                return Response(serializer.data, status=status.HTTP_201_CREATED)
                            else:
                                # catch serializer integrity error
                                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                    else:
                        message = {'detail': 'Bid has to exceed minimum price.'}
                        return Response(message, status=status.HTTP_400_BAD_REQUEST)
        elif (request.method == "PUT"):
            if(user != artitem.owner):
                message = {
                    'detail': 'Only the owner can update sale status of art item.'}
                return Response(message, status=status.HTTP_403_FORBIDDEN)
            else:
                if(artitem.sale_status == 'SO'):
                    message = {'detail': 'Sorry, this art item is already sold.'}
                    return Response(message, status=status.HTTP_400_BAD_REQUEST)
                elif(artitem.sale_status == 'FS'):
                    if(data["sale_status"] == 'FS'):
                        message = {'detail': 'The art item is already for sale.'}
                        return Response(message, status=status.HTTP_400_BAD_REQUEST)
                    if(data["sale_status"] == 'NS'):
                        artitem.sale_status = 'NS'
                        artitem.save()
                        message = {'detail': 'The art item is successfully closed to sale.'}
                        return Response(message, status=status.HTTP_200_OK)
                    else:
                        message = {'detail': 'Invalid sale status input.'}
                        return Response(message, status=status.HTTP_400_BAD_REQUEST)
                #'NS'
                else:
                    if(data["sale_status"] == 'NS'):
                        message = {'detail': 'The art item is already not for sale.'}
                        return Response(message, status=status.HTTP_400_BAD_REQUEST)
                    if(data["sale_status"] == 'FS'):
                        if(data["minimum_price"] > 0.0 ):
                            artitem.sale_status = 'FS'
                            artitem.minimum_price = data["minimum_price"]
                            artitem.save()
                            message = {'detail': 'The art item is successfully put on sale.'}
                            return Response(message, status=status.HTTP_200_OK)
                        else:
                            message = {'detail': 'Minimum price has to be a positive number.'}
                            return Response(message, status=status.HTTP_400_BAD_REQUEST)

                    else:
                        message = {'detail': 'Invalid sale status input.'}
                        return Response(message, status=status.HTTP_400_BAD_REQUEST)
            
    else:
        message = {'detail': 'Invalid token.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='GET',
    operation_description="This endpoint with GET request returns a specific bid. Authentication is required. Only the owner of the art item and the bidder can call this.",
    operation_summary="Get bid info with unique ID.",
    tags=['bids'],
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Successfully got the bid.",
            examples={
                "application/json": {
                    "bids": [
                        {
                            "id": 1,
                            "artitem": {
                                "id": 21,
                                "title": "a3",
                                "category": "OT",
                                "artitem_path": "artitem/defaultart.jpg"
                            },
                            "buyer": {
                                "id": 3,
                                "username": "string2",
                                "profile_path": "avatar/default.png"
                            },
                            "amount": 10.0,
                            "created_at": "20-12-2022 17:42:34",
                            "deadline": "21-12-2022 17:42:33",
                            "accepted": "NR"
                        },
                        {
                            "id": 4,
                            "artitem": {
                                "id": 21,
                                "title": "a3",
                                "category": "OT",
                                "artitem_path": "artitem/defaultart.jpg"
                            },
                            "buyer": {
                                "id": 2,
                                "username": "string",
                                "profile_path": "avatar/default.png"
                            },
                            "amount": 3214.0,
                            "created_at": "20-12-2022 21:52:42",
                            "deadline": "22-12-2022 21:52:42",
                            "accepted": "NR"
                        }
                    ]
                }
            }
        ),
        status.HTTP_404_NOT_FOUND: openapi.Response(
            description="Wrong bid id.",
            examples={
                "application/json": {
                    "detail": "Bid with the given id does not exist."
                },
            }
        ),
        status.HTTP_403_FORBIDDEN: openapi.Response(
            description="User not authorized.",
            examples={
                "application/json": {
                    "detail": "Only the owner and the buyer can view the bid."
                },
            }
        ),
    }
)
@swagger_auto_schema(
    operation_id="artitems_bids_response",
    method='PUT',
    request_body=bidUpdateSerializer,
    operation_description="This endpoint with PUT request is used by owner to respond to a bid. Authentication is required. Parameter response can either be AC or RE.",
    operation_summary="Respond to a bid with unique ID",
    tags=['bids'],
    responses={
        status.HTTP_201_CREATED: openapi.Response(
            description="Successfully accepted the bid.",
            examples={
                "application/json": {
                    "detail": "Successfully accepted the bid."
                },
            }
        ),
        status.HTTP_400_BAD_REQUEST: openapi.Response(
            description="Not for sale.",
            examples={
                "application/json": {
                    "detail": "Can not respond to the bid, this art item is currently not for sale."
                },
            }
        ),
        status.HTTP_403_FORBIDDEN: openapi.Response(
            description="Forbidden action.",
            examples={
                "application/json": {
                    "detail": "Only the owner can respond to the bid."
                },
            }
        ),
    }
)
@api_view(['GET', 'PUT'])
def BidView(request, id):
    if request.user.is_authenticated:
        user = request.user
        data = request.data
        try:
            bid = Bid.objects.get(id=id)
            artitem = bid.artitem
            owner = bid.artitem.owner
        except Bid.DoesNotExist:
            message = {
                'detail': 'Bid with the given id does not exist.'}
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        if (request.method == "GET"):
            if(user == bid.buyer or user == owner):
                serializer = BidSerializer(bid)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                message = {'detail': 'Only the owner and the buyer can view the bid.'}
                return Response(message, status=status.HTTP_403_FORBIDDEN)
        elif (request.method == "PUT"):
            if(user != owner):
                message = {
                    'detail': 'Only the owner can respond to the bid.'}
                return Response(message, status=status.HTTP_403_FORBIDDEN)
            else:
                if(artitem.sale_status == 'NS'):
                    message = {'detail': 'Can not respond to the bid, this art item is currently not for sale.'}
                    return Response(message, status=status.HTTP_400_BAD_REQUEST)
                elif(artitem.sale_status == 'SO'):
                    message = {'detail': 'Can not respond to the bid, this art item is already sold.'}
                    return Response(message, status=status.HTTP_400_BAD_REQUEST)
                else:
                    if(bid.deadline.replace(tzinfo=None) < datetime.datetime.now() ):
                        print(datetime.datetime.now())
                        print(bid.deadline.replace(tzinfo=None))
                        message = {'detail': 'Sorry, deadline for the bid has already passed.'}
                        return Response(message, status=status.HTTP_400_BAD_REQUEST)
                    else:
                        if(bid.accepted == 'AC'):
                            message = {'detail': 'Can not respond to the bid, the bid is already accepted.'}
                            return Response(message, status=status.HTTP_400_BAD_REQUEST)
                        elif(bid.accepted == 'RE'):
                            message = {'detail': 'Can not respond to the bid, the bid is already rejected.'}
                            return Response(message, status=status.HTTP_400_BAD_REQUEST)
                        else:
                            if(data["response"] == 'RE'):
                                bid.accepted = 'RE'
                                bid.save()
                                #serializer = BidSerializer(instance=bid)
                                #return Response(serializer.data, status=status.HTTP_200_OK)
                                message = {'detail': 'Successfully rejected the bid.'}
                                return Response(message, status=status.HTTP_200_OK)
                            elif(data["response"] == 'AC'):
                                bid.accepted = 'AC'
                                bid.save()
                                artitem.sale_status = 'SO'
                                artitem.bought_by = bid.buyer
                                artitem.save()
                                message = {'detail': 'Successfully accepted the bid.'}
                                return Response(message, status=status.HTTP_200_OK)
                                
                            else:
                                message = {'detail': 'Invalid input format for ["response"].'}
                                return Response(message, status=status.HTTP_400_BAD_REQUEST)

    else:
        message = {'detail': 'Invalid token.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
