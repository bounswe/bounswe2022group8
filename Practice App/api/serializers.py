from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import myUser, Tag, Comment, ArtItem

class ArtItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtItem
        fields = ['id', 'title', 'description', 'owner', 'tags', 'comments']

class TagSerializer(serializers.ModelSerializer):
    model = Tag
    fields = ['id', 'tagname']

class myUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = myUser
        fields = ['id', 'username', 'name', 'surname', 'email', 'followers', 'followed_users', 'created_at', 'updated_at']
class CommentSerializer(serializers.CommentSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'body', 'commented_by', 'created_at', 'updated_at']

