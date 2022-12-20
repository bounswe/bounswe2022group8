from rest_framework import serializers
from ..models.artitem import Bid

from django.core.validators import MinValueValidator 

#just used for swagger
class bidPostSerializer(serializers.Serializer):

    #body = serializers.CharField(default="This is a comment.")
    #parent = serializers.CharField(default="This is id of the parent comment. This is an optional parameter. You may not add this line if the comment is not a reply.")
    amount = serializers.CharField(default = 568.5)
    deadline = serializers.CharField(default="2022-12-20T18:58:15.643Z")

#just used for swagger
class bidUpdateSerializer(serializers.Serializer):

    body = serializers.CharField(default="This is the updated comment.")
    accepted = serializers.BooleanField(default=False)
    