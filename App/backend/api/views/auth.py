from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from knox.models import AuthToken

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from ..serializers.auth import RegisterSerializer, LoginSerializer

from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

# Create your authentication-related views here.

class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request):
        user = request.data
    
        serializer = self.serializer_class(data = user)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        user_data = serializer.data
        return Response({"user": user_data, "token": AuthToken.objects.create(user)[1]}, status = status.HTTP_201_CREATED)

class LoginView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "token": AuthToken.objects.create(user)[1]
        })

@method_decorator(login_required, name='dispatch')  
class DummyView(generics.GenericAPIView):
    def get(self, request):
        return Response("deneme2", status=status.HTTP_202_ACCEPTED)

