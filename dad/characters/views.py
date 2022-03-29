from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated


class CharacterList(generics.ListCreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = [IsAuthenticated]


class CharacterDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = [IsAuthenticated]


class WeaponList(generics.ListAPIView):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class PresetList(generics.ListCreateAPIView):
    queryset = Preset.objects.all()
    serializer_class = PresetSerializer
    permission_classes = [IsAuthenticated]

