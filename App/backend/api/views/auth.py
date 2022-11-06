from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from knox.models import AuthToken

from ..serializers.auth import RegisterSerializer, LoginSerializer
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema

from drf_yasg import openapi


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    @swagger_auto_schema(
        operation_description="""Register to the application providing a unique username, email and password.
        This API returns a unique token for the current session, meaning that a user is automatically logged in upon a successfull registration.""",
        operation_summary="Register with username, email and password.",
        tags=['auth'],
        request_body=RegisterSerializer,
        responses={
            status.HTTP_200_OK: openapi.Response(
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
