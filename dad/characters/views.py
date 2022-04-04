from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from .custompermission import IsOwnerOrReadOnly


class CharacterList(generics.ListCreateAPIView):
    name = 'character-list'
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = [IsAuthenticated]


class CharacterDetails(generics.RetrieveUpdateDestroyAPIView):
    name = 'character-detail'
    queryset = Character.objects.all()
    serializer_class = CharacterDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class WeaponList(generics.ListAPIView):
    name = 'weapon-list'
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]


class PresetList(generics.ListCreateAPIView):
    name = 'preset-list'
    queryset = Preset.objects.all()
    serializer_class = PresetSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({'character-list': reverse(CharacterList.name, request=request),
                         'weapon-list': reverse(WeaponList.name, request=request),
                         'preset_list': reverse(PresetList.name, request=request),
                         })
