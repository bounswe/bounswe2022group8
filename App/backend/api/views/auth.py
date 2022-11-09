from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from knox.models import AuthToken

from ..serializers.auth import RegisterSerializer, LoginSerializer
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema

from drf_yasg import openapi

from django.conf import settings
from django.core.mail import send_mail


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
                            "email": "alvin.plantsdiga@calvin.edu",
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

#Function to send Email with OTP on User Request
@api_view(['POST'])
def resetRequestView(request):
    data = request.data
    email = data['email']
    user = settings.AUTH_USER_MODEL.objects.get(email=email)
    if settings.AUTH_USER_MODEL.objects.filter(email=email).exists():
        # send email with otp
        send_mail(
        'Password Reset', #Subject
        f'We have received a request from your account to reset password. Please reset your pass word using the following OTP (one time password): {user.otp}.', #message
        'from@example.com',
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

#Function to verify OTP And reset Password
@api_view(['PUT'])
def resetPasswordView(request):
    """reset_password with email, OTP and new password"""
    data = request.data
    user = settings.AUTH_USER_MODEL.objects.get(email=data['email'])
    if user.is_active:
        # Check if otp is valid
        if data['otp'] == user.opt:
            #here use a function to check password criteria
            if data['new_password'] != '':
                # Change Password
                user.set_password(data['password'])
                user.save() # Here user otp will also be changed on save automatically 
                return Response('Password succesfully reset.')
            else:
                message = {
                    'detail': 'Password cant be empty'}
                return Response(message, status=status.HTTP_400_BAD_REQUEST)
        else:
            message = {
                'detail': 'OTP did not match'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
    else:
        message = {
            'detail': 'User is not active. Something went wrong'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
