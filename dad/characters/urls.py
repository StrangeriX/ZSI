from django.urls import path
from .views import *

urlpatterns = [
    path('characters', CharacterList.as_view(), name='characters list'),
    path('characters/<int:pk>', CharacterDetails.as_view(), name='character detail'),
    path('weapon', WeaponList.as_view(), name='weapons list'),
    path('preset', PresetList.as_view(), name='presets list')
]