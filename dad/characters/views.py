from .models import Character
from .serializers import CharacterSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class CharacterList(generics.ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
