from django.urls import path
from .views import *

urlpatterns = [
    path('characters', CharacterList.as_view(), name=CharacterList.name),
    path('characters/<int:pk>', CharacterDetails.as_view(), name=CharacterDetails.name),
    path('weapon', WeaponList.as_view(), name=WeaponList.name),
    path('preset', PresetList.as_view(), name=PresetList.name),
    path('', ApiRoot.as_view(), name=ApiRoot.name)
]