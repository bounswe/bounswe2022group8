from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from ..models.models import Comment
from ..models.artitem import Tag, ArtItem
from ..models.user import User
from .serializers import TagSerializer, SimpleUserSerializer, ArtItemSerializer, SimpleArtItemSerializer
from ..models.exhibition import OfflineExhibition, VirtualExhibition, ExhibitionArtItem

class OfflineExhibitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfflineExhibition
        fields = ['id', 'owner', 'title', 'description', 'poster', 'collaborators', 'start_date', 'end_date', 'created_at', 'updated_at', 
        'city', 'country', 'address', 'latitude', 'longitude']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["poster"] = SimpleArtItemSerializer(instance.poster).data
        rep["collaborators"] = SimpleUserSerializer(instance.collaborators, many=True).data
        rep["owner"] = SimpleUserSerializer(instance.owner).data
        return rep


class ExhibitionArtItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExhibitionArtItem
        fields = ['id', 'virtualExhibition', 'owner', 'artitem_path', 'artitem_image', 'created_at']

class SimpleExhibitionArtItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExhibitionArtItem
        fields = ['id', 'virtualExhibition', 'artitem_path', 'created_at']

class VirtualExhibitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VirtualExhibition
        fields = ['id', 'owner', 'title', 'description', 'poster', 'collaborators', 'artitems_gallery', 'start_date', 'end_date', 'created_at', 'updated_at']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["poster"] = SimpleArtItemSerializer(instance.poster).data
        rep["collaborators"] = SimpleUserSerializer(instance.collaborators, many=True).data
        rep["owner"] = SimpleUserSerializer(instance.owner).data
        rep["artitems_gallery"] = SimpleArtItemSerializer(instance.artitems_gallery, many=True).data
        return rep
