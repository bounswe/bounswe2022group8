from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.generics import ListAPIView
from knox.auth import TokenAuthentication, AuthToken
from rest_framework.filters import SearchFilter, OrderingFilter

from ..models.artitem import ArtItem
from ..models.user import User
from ..serializers.serializers import ArtItemSerializer

from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth.models import AnonymousUser

from drf_yasg import openapi
import base64

class LexSearchView(ListAPIView):
    queryset = ArtItem.objects.all()
    serializer_class = ArtItemSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', 'description', 'owner__name', 'owner__surname', 'tags__tagname')
