from rest_framework import serializers
from ..models.user import LikeArtItem, LikeComment


class LikeArtItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeArtItem
        fields = ["id", "user", "artitem", "liked_at"] 

class LikeCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeComment
        fields = ["id", "user", "comment", "liked_at"] 