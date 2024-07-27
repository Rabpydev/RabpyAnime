from django.urls import path
from App import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_swagger.views import get_swagger_view
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="API Documentation",
      default_version='v1',
      description="API documentation using Swagger",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', views.index, name="home"),
    path('anime', views.animeall, name="animeall"),
    path('anime/<int:anime_id>', views.anime, name="anime"),
    path('character', views.characterall, name="characterall"),
    path('character/<int:character_id>', views.character, name="character"),
    path('contact', views.contact, name="contact"),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)