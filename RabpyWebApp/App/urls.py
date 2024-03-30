from django.urls import path
from App import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index),
    path('anime', views.animeall),
    path('anime/<int:anime_id>', views.anime),
    path('character', views.characterall),
    path('character/<int:character_id>', views.character),
    path('contact', views.contact)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)