from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from ..models.models import Tag, Comment, ArtItem
from ..models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username',  'is_level2', 'otp', 'name', 'surname',
                  'email', 'profile_image', 'created_at', 'updated_at']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'tagname', 'description', 'created_at', 'updated_at']


class ArtItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtItem
        fields = ['id', 'title', 'description',
                  'owner', 'tags', 'artitem_image']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["tags"] = TagSerializer(instance.tags.all(), many=True).data
        return rep


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'body', 'commented_by', 'commented_on', 'created_at']


