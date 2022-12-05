from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from knox.models import AuthToken

from ..serializers.auth import RegisterSerializer, LoginSerializer, resetRequestSerializer, resetPasswordSerializer, passwordSerializer
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema

from drf_yasg import openapi

from django.conf import settings
from django.core.mail import send_mail
from ..models.user import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
import hashlib


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    @swagger_auto_schema(
        operation_description="""Register to the application providing a unique username, email and password.
        This API returns a unique token for the current session, meaning that a user is automatically logged in upon a successfull registration.""",
        operation_summary="Register with username, email and password.",
        tags=['auth'],
        request_body=RegisterSerializer,
        responses={
            status.HTTP_201_CREATED: openapi.Response(
                description="Successfully logged in.",
                examples={
                    "application/json": {
                        "user": {
                            "email": "alvin.plantiga@calvin.edu",
                            "username": "on_existentialism"
                        },
                        "token": "d3e90cabeb3c3476eba98c5b4fc3750e81efd9c72fd623c8c6bae1bfbcc7b435"
                    }
                }
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description="Invalid credentials.",
                examples={
                    "application/json": {
                            "email": [
                                "user with this email already exists."
                            ],
                        "username": [
                                "user with this username already exists."
                            ]
                    },
                }
            ),
        }
    )
    def post(self, request):
        user = request.data

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        user_data = serializer.data
        return Response({"user": user_data, "token": AuthToken.objects.create(user)[1]}, status=status.HTTP_201_CREATED)


class LoginView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer

    @ swagger_auto_schema(
        operation_description="Login to the application with your username or email. This API returns a unique token for the current session.",
        operation_summary="Login with username or email.",
        tags=['auth'],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Successfully logged in.",
                examples={
                    "application/json": {
                        "token": "70c4706e8c8de50a3267f2393ff38753418be4454df383d50cf4f6265e1d9368"}
                }
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description="Invalid credentials.",
                examples={
                    "application/json": {
                        "credentials": ["Incorrect username or email."],
                        "credentials": ["Incorrect password"]
                    },
                }
            ),
        }
    )
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "token": AuthToken.objects.create(user)[1]
        })

# {
#   "email": "user_email@artopia.com"
# }
#Function to send Email with OTP on User Request
@swagger_auto_schema(
        method='POST',
        request_body=resetRequestSerializer,
        operation_description="Password reset request API. This API takes the user email as a parameter and sends an email with OTP (one time password) to user.",
        operation_summary="Send password reset request with email (Part1).",
        tags=['password_reset'],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Successfully sent the password reset email.",
                examples={
                    "application/json": {
                        "detail": ["Successfully sent the password reset email."]
                    }
                }
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description="Invalid credentials.",
                examples={
                    "application/json": {
                        "credentials": ["Incorrect username or email."],
                        "credentials": ["Incorrect password"]
                    },
                }
            ),
        }
    )
@api_view(['POST'])
def resetRequestView(request):
    data = request.data
    email = data['email']
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        message = {
            'detail': 'User with given email does not exist.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    if User.objects.filter(email=email).exists():
        #create an otp
        myotp = user.changeOTP()
        #print(settings.EMAIL_HOST_USER)
        # send email with otp
        send_mail(
        'Password Reset', #Subject
        f'We have received a request from your account to reset password. Please reset your password using the following OTP (one time password): {myotp}.', #message
        settings.EMAIL_HOST_USER,
        [user.email],
        fail_silently=False,
        )
        message = {
            'detail': 'Successfully sent the password reset email.'}
        return Response(message, status=status.HTTP_200_OK)
    else:
        message = {
            'detail': 'User with given email does not exist. Error occured while sending password reset email.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

# {
#   "email": "user_email@artopia.com",
#   "otp": "six_digit_otp_from_email",
#   "new_password": "new_user_password"
# }
#Function to verify OTP And reset Password
@swagger_auto_schema(
        method='PUT',
        request_body=resetPasswordSerializer,
        operation_description="Password reset API. After user has received otp via request-reset API, this API takes the user email, otp and new_password as a parameters and changes the user password if everything checks out.",
        operation_summary="Password reset API (Part2).",
        tags=['password_reset'],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Password succesfully reset.",
                examples={
                    "application/json": {
                        "detail": ["Password succesfully reset."]
                    }
                }
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description="Invalid credentials.",
                examples={
                    "application/json": {
                        "detail": ["User with given email does not exist."],
                        "detail": ["Password cant be empty"],
                        "detail": ["User is not active. Something went wrong"],
                        "detail": ["OTP did not match"]
                    },
                    
                }
            ),
        }
    )
@api_view(['PUT'])
def resetPasswordView(request):
    """reset_password with email, OTP and new password"""
    data = request.data
    try:
        user = User.objects.get(email=data['email'])
    except User.DoesNotExist:
        message = {
            'detail': 'User with given email does not exist.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    if user.is_active:
        # Check if otp is valid
        if hashlib.sha256(data['otp'].encode('utf-8')).hexdigest() == user.otp:
            #here use a function to check password criteria
            if data['new_password'] != '':
                #validate that new password fits criteria
                try:
                    validate_password(data['new_password'])
                except ValidationError as e:
                    message = {
                    'detail': e.messages}
                    return Response(message, status=status.HTTP_400_BAD_REQUEST)
                # Change Password
                user.set_password(data['new_password'])
                user.save() 
                user.changeOTP()
                message = {
                    'detail': 'Password succesfully reset.'}
                return Response(message, status=status.HTTP_200_OK)
            else:
                message = {
                    'detail': 'Password cant be empty'}
                user.changeOTP()
                return Response(message, status=status.HTTP_400_BAD_REQUEST)
        else:
            message = {
                'detail': 'OTP did not match'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
    else:
        message = {
            'detail': 'User is not active. Something went wrong'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

# {
#   "new_password": "new_user_password"
# }
@swagger_auto_schema(
        method='PUT',
        request_body=passwordSerializer,
        operation_description="Password update API. This API takes the new password as a parameter and updates the user password. Login is required",
        operation_summary="Password update API.",
        tags=['password_reset'],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Password succesfully updated.",
                examples={
                    "application/json": {
                        "detail": ["Password succesfully updated."]
                    }
                }
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description="Invalid credentials.",
                examples={
                    "application/json": {
                        "detail": ["Invalid token."],
                        "detail": ["Password cant be empty"]
                    },
                }
            ),
        }
    )
@api_view(['PUT'])
@login_required
def resetPasswordLoggedView(request):
    data = request.data
    currentusername = request.user.username
    u = User.objects.get(username = currentusername)
    if data['new_password'] != '':
        #validate that new password fits criteria
        try:
            validate_password(data['new_password'])
        except ValidationError as e:
            message = {
            'detail': e.messages}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        # Change Password
        u.set_password(data['new_password'])
        u.save() 
        message = {
            'detail': 'Password succesfully updated.'}
        return Response(message, status=status.HTTP_200_OK)
    else:
        message = {
            'detail': 'Password cant be empty'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
        method='DELETE',
        request_body=passwordSerializer,
        operation_description="Account deletion API. This API takes the password as a parameter and deletes the user account. Login is required",
        operation_summary="Account deletion API.",
        tags=['auth'],
        responses={
            status.HTTP_204_NO_CONTENT: openapi.Response(
                description="The user account has been successfully deleted.",
                examples={
                    "application/json": {
                        "Success": ["The user account has successfully been deleted!"]
                    }
                }
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description="The password did not match or the user account could not be deleted.",
                examples={
                    "application/json": {
                        "Failure": ["The user account could not be deleted!"],
                        "Failure": ["The password did not match!"]
                    },
                }
            ),
        }
    )
@api_view(['DELETE'])
@login_required
def delete_account(request):
    data = request.data
    user = request.user
    if(user.check_password(data['password'])):
        try:
            user.delete()
            return Response({'Success': 'The user account has successfully been deleted!'}, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({'Failure': 'The user account could not be deleted!'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'Failure': 'The password did not match!'}, status=status.HTTP_400_BAD_REQUEST)
