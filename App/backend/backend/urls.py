"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view

from . import views

schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Artopia API Documentation",
        default_version='v1.0',
        description="Artopia API Endpoints",
    ),
    public=True,
)

# You can open the Swagger documentation from here on local: localhost:8000/api/v1/swagger/schema
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="index"),
        path('api/v1/', 
        include([
            path('', include('api.urls')),
            path('swagger/schema/', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-schema"),
        ])
    ),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
