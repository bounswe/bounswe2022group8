from rest_framework import serializers
from ..models.models import Comment


#just used for swagger
class commentsPostSerializer(serializers.Serializer):

    body = serializers.CharField(default="This is a comment.")
    parent = serializers.CharField(default="This is id of the parent comment. This is an optional parameter. You may not add this line if the comment is not a reply.")

#just used for swagger
class commentUpdateSerializer(serializers.Serializer):

    body = serializers.CharField(default="This is the updated comment.")
    