
"""
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
"""

from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

from drf_yasg.utils import swagger_auto_schema
from rest_framework import status

from drf_yasg import openapi



# SWAGGER: localhost:8000/api/v1/swagger/schema
urlpatterns = [
    path('annotations/', annotate, name="annotate"),
    path('annotations/image/', get_image_annotations, name="get image annotations"),
    path('annotations/text/', get_text_annotations, name="get text annotations"),
    path('annotations/text/users/<int:userid>/artitems/<int:artitemid>', get_text_annotation_by_artitem_user_id, name="get text annotations on a specific art item by a user"),
    path('annotations/text/artitems/<int:artitemid>', get_text_annotations_by_artitem_id, name="get text annotations on an art item"),
    path('annotations/image/users/<int:userid>', get_image_annotation_by_user_id, name="get image annotations of a user"),
    path('annotations/image/artitems/<int:artitemid>', get_image_annotation_by_artitem_id, name="get image annotations on an art item by a user"),
    path('annotations/image/users/<int:userid>/artitems/<int:artitemid>', get_image_annotation_by_artitem_user_id, name="get image annotations on a specific art item by a user"),
    path('annotations/text/users/<int:userid>', get_text_annotations_by_userid, name="get text annotations of a user")
]

# added to give us the option to choose between default Response template and regular json
# extend the url with <?format=json> to get json
# if you're having any trouble with your views make sure you added format=None to the arguments
# urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
