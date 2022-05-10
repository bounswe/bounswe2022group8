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