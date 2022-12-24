
from rest_framework import serializers
from ..models.user import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from knox.auth import AuthToken
from ..models.user import Follow

class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile"""
    followers = serializers.ReadOnlyField(source='get_followers')
    followings = serializers.ReadOnlyField(source='get_followings')
    email = serializers.EmailField()

    # here, we define the parameters we expect to receive (not directly related to model)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'name', 'surname', 'about', 'location', 'profile_path', 'is_level2', 'followers', 'followings', 'new_bid_flag']

class UserUpdateProfileSerializer(serializers.ModelSerializer):
    """Update serializer for our user profile"""

    # here, we define the parameters we expect to receive (not directly related to model)
    class Meta:
        model = User
        fields = ['id', 'name', 'surname', 'about', 'location', 'profile_path', 'updated_at']
