from django.urls import path
from .views import CharacterList

urlpatterns = [
    path('characters/', CharacterList.as_view())
]