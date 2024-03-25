from rest_framework import serializers, viewsets, routers
from .models import Character
from .serializer import CharacterSerializer

class CharacterApiView(viewsets.ModelViewSet):
    queryset = Character.objects.filter(gender='female')
    serializer_class = CharacterSerializer

router = routers.DefaultRouter()
router.register(r'character/list', CharacterApiView)