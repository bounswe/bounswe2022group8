from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from ..models.models import Tag, Comment, ArtItem
from ..models.user import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length = 8, write_only=True)
    class Meta:
        model = User
        fields = ['email', 'username', 'name', 'surname', 'password']

    def validate(self, attrs):
        username = attrs.get('username', '')

        is_valid_username, error = self.is_valid_username(username)
        if not is_valid_username:
            raise serializers.ValidationError({"username": error})

        return attrs

    def create(self, validated_data):
        return User.objects.create(**validated_data)
    
    def is_valid_username(self, username):
        """
        Check the following rules for a username:
        1) First character must be a letter
        2) Last character cannot be an underscore
        3) It can consist of letters, numbers and underscore (alphanum + underscore)
        4) Username must be unique. Don't accept it if it is already present in the database.
        5) It must have at least 6 characters (because reasons)
        """
        if(not username[0].isalpha()): return (False, "The username must start with a letter.")
        elif(username[-1] == '_'): return (False, "The username cannot end with an underscore.")
        elif(not username.replace('_','').isalnum()): return (False, "The username can consist of letters, numbers or underscore.")
        elif(len(username) < 6): return (False, "The username must have at least 6 characters")
        # elif(User.objects.filter(username=username) is not None): return (False, "The username must be unique.")
        else: return (True, "")

        # Why did I comment out the last elif? Well, because we defined 'username' field to be unique in the models.user file.
        # Therefore it's not necessary to check it again.


