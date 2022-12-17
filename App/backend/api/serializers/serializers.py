from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from ..models.models import Comment
from ..models.artitem import Tag, ArtItem
from ..models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username',  'is_level2', 'name', 'surname',
                  'email', 'profile_path', 'created_at', 'updated_at']

class CommentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'profile_path']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'tagname', 'description', 'created_at', 'updated_at']


class ArtItemSerializer(serializers.ModelSerializer):
    likes = serializers.ReadOnlyField(source='get_numberof_likes')

    class Meta:
        model = ArtItem
        fields = ['id', 'owner', 'title', 'description', 'category', 'tags', 'artitem_path', 'likes', 'created_at']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["tags"] = TagSerializer(instance.tags.all(), many=True).data 
        rep["owner"] = SimpleUserSerializer(instance.owner).data
        return rep


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'body', 'parent', 'commented_by', 'commented_on', 'created_at', 'lft', 'rght', 'tree_id', 'level']
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["commented_by"] = CommentUserSerializer(instance.commented_by).data 
        return rep


class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'name', 'surname',  'profile_path']