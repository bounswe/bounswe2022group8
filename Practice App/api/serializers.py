from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import myUser, Tag, Comment, ArtItem, Follow

class ArtItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtItem
        fields = ['id', 'title', 'description', 'owner', 'tags', 'artitem_image']
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["tags"] = TagSerializer(instance.tags.all(), many=True).data
        rep["owner"] = SimpleUserSerializer(instance.owner).data
        return rep

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'tagname', 'description', 'created_at', 'updated_at']

    

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ["id", "from_user", "to_user", "created_at"] # add created_at


class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = myUser
        fields = ['id', 'username', 'name', 'surname']

class myUserSerializer(serializers.ModelSerializer):
    follower = serializers.SerializerMethodField()
    following = serializers.SerializerMethodField()
    class Meta:
        model = myUser
        fields = ['id', 'username', 'name', 'surname', 'follower', 'following', 'email', 'created_at', 'updated_at']

    def get_follower(self, obj):
        follower_query = Follow.objects.filter(to_user=obj.id)  # return all Follow objects with to_user = obj.id (all follow objects in which this user is being followed)
        followers =[]
        for i in range(len(follower_query)):
            followers.append(myUser.objects.get(id = follower_query[i].from_user.id))
        
        return SimpleUserSerializer(followers, many=True).data

    # myUser.objects.filter(id = Follow.objects.filter(from_user=1)[0].to_user.id)
    def get_following(self, obj):
        following_query = Follow.objects.filter(from_user=obj.id)
        followers = []
        for i in range(len(following_query)):
            followers.append(myUser.objects.get(id = following_query[i].to_user.id))

        return SimpleUserSerializer(followers, many=True).data



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'body', 'commented_by', 'commented_on', 'created_at', 'updated_at']