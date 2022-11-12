
from rest_framework import serializers
from ..models.user import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate


class RegisterSerializer(serializers.ModelSerializer):
    START_ERROR = "The username must start with a letter."
    END_ERROR = "The username cannot end with an underscore."
    ALPHANUM_ERROR = "The username can consist of letters, numbers or underscore."
    MIN_LENGTH_ERROR = "Username must have at least 6 characters."
    SUCCESS = ""

    password = serializers.CharField(min_length = 10, write_only=True,  error_messages={
        'blank':  'This field is required.',
        'min_length':  'Password must have at least 10 characters.'
    })
    #username = serializers.CharField(min_length = 6, unique = True)
    password_confirm = serializers.CharField(write_only=True, error_messages={
        'blank':  'This field is required.'
    })

    # here, we define the parameters we expect to receive (not directly related to model)
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password_confirm']
        extra_kwargs = {'email': {'error_messages': {'blank': 'This field is required.'}},
        'username': {'error_messages': {'blank': 'This field is required.'}}}


    def validate(self, data):
        username = data.get('username', '')
        password = data.get('password', '')
        try:
            validate_password(password)
        except ValidationError as e:
            raise serializers.ValidationError({"password": e.messages}) 


        is_valid_username, error = self.is_valid_username(username)
        if not is_valid_username:
            raise serializers.ValidationError({"username": error})
        if not data.get('password') or not data.get('password_confirm'):
            raise serializers.ValidationError({"password": "Please enter a password and confirm it."})
        if data.get('password') != data.get('password_confirm'):
            raise serializers.ValidationError({"password_confirm": "Passwords do not match."})

        return data

    def create(self, validated_data):
        
        del validated_data['password_confirm']
        validated_data['password'] = make_password(validated_data['password'])
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
        if(not username[0].isalpha()): return (False, self.START_ERROR)
        elif(username[-1] == '_'): return (False, self.END_ERROR)
        elif(not username.replace('_','').isalnum()): return (False, self.ALPHANUM_ERROR)
        elif(len(username) < 6): return (False, self.MIN_LENGTH_ERROR)
        # elif(User.objects.filter(username=username) is not None): return (False, "The username must be unique.")
        else: return (True, self.SUCCESS)

        # Why did I comment out the last elif? Well, because we defined 'username' field to be unique in the models.user file.
        # Therefore it's not necessary to check it again.


class LoginSerializer(serializers.Serializer):
    credential = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        credentials = {
            'username': '',
            'password': data.get("password")
        }

        # This is answering the original question, but do whatever you need here. 
        # For example in my case I had to check a different model that stores more user info
        # But in the end, you should obtain the username to continue.
        usr = User.objects.filter(email=data.get("credential")).first() or User.objects.filter(username=data.get("credential")).first()
        if usr:
            credentials['username'] = usr.username
        else:
            raise serializers.ValidationError({"credentials": 'Incorrect username or email.'})
        user = authenticate(**credentials)

        if user and user.is_active:
            return user
        raise serializers.ValidationError({"credentials": 'Incorrect password.'})
#just used for swagger
class resetRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = User 
        fields = ["email"]
#just used for swagger
class resetPasswordSerializer(serializers.Serializer):

    email = serializers.EmailField(default="user_email@artopia.com")
    otp = serializers.CharField(default="six_digit_otp_from_email")
    new_password = serializers.CharField(default="new_user_password")

#just used for swagger
class passwordSerializer(serializers.Serializer):
    new_password = serializers.CharField(default="new_user_password")
