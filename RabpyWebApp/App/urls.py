from django.urls import path
from App import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name="home"),
    path('anime', views.animeall, name="animeall"),
    path('anime/<int:anime_id>', views.anime, name="anime"),
    path('character', views.characterall, name="characterall"),
    path('character/<int:character_id>', views.character, name="character"),
    path('contact', views.contact, name="contact")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)