from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from ..models.models import Comment
from ..models.artitem import Tag, ArtItem
from ..models.user import User
from .serializers import TagSerializer, SimpleUserSerializer, ArtItemSerializer, SimpleArtItemSerializer
from ..models.exhibition import OfflineExhibition, VirtualExhibition

class OfflineExhibitionSerializer(serializers.ModelSerializer):
    status = serializers.ReadOnlyField(source='get_status')

    class Meta:
        model = OfflineExhibition
        fields = ['id', 'owner', 'title', 'description', 'poster', 'collaborators', 'start_date', 'end_date', 'created_at', 'updated_at', 
        'city', 'country', 'address', 'latitude', 'longitude', 'status']
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["poster"] = SimpleArtItemSerializer(instance.poster).data
        rep["collaborators"] = SimpleUserSerializer(instance.collaborators, many=True).data
        rep["owner"] = SimpleUserSerializer(instance.owner).data
        return rep

class SimpleExhibitionArtItemSerializer(serializers.ModelSerializer):
    likes = serializers.ReadOnlyField(source='get_numberof_likes')
    class Meta:
        model = ArtItem
        fields = ['id', 'title', 'tags', 'description', 'type', 'artitem_path',  'likes', 'created_at']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["tags"] = TagSerializer(instance.tags.all(), many=True).data 
        return rep

class ExhibitionArtItemSerializer(serializers.ModelSerializer):
    likes = serializers.ReadOnlyField(source='get_numberof_likes')
    class Meta:
        model = ArtItem
        fields = ['id',  'owner', 'title', 'tags', 'description', 'type', 'virtualExhibition', 'artitem_path', 'artitem_image', 'likes', 'created_at']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["tags"] = TagSerializer(instance.tags.all(), many=True).data 
        rep["owner"] = SimpleUserSerializer(instance.owner).data
        return rep

class VirtualExhibitionSerializer(serializers.ModelSerializer):
    status = serializers.ReadOnlyField(source='get_status')
    artitems_upload = serializers.ReadOnlyField(source='get_uploaded_artitems')
    class Meta:
        model = VirtualExhibition
        fields = ['id', 'owner', 'title', 'description', 'poster', 'collaborators', 'artitems_gallery', 'start_date', 'end_date', 'created_at', 'updated_at', 'status', 'artitems_upload']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["poster"] = SimpleArtItemSerializer(instance.poster).data
        rep["collaborators"] = SimpleUserSerializer(instance.collaborators, many=True).data
        rep["owner"] = SimpleUserSerializer(instance.owner).data
        rep["artitems_gallery"] = SimpleArtItemSerializer(instance.artitems_gallery, many=True).data
        rep["artitems_upload"] = SimpleExhibitionArtItemSerializer(rep['artitems_upload'], many=True).data
        return rep
