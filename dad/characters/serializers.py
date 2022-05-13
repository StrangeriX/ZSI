from rest_framework import serializers
from .models import Character, Weapon, Preset, Armor, User


class WeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = '__all__'


class PresetSerializer(serializers.HyperlinkedModelSerializer):
    armor = serializers.SlugRelatedField(queryset=Armor.objects.all(), slug_field='name')
    weapon = serializers.SlugRelatedField(many=True, queryset=Weapon.objects.all(), slug_field='name')

    class Meta:
        model = Preset
        fields = ['id', 'name', 'armor', 'weapon', 'description']


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    character_preset = PresetSerializer()
    user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    level = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Character
        fields = ['url', 'name', 'level', 'user', 'character_preset']


class CharacterDetailSerializer(serializers.HyperlinkedModelSerializer):
    character_preset = PresetSerializer()
    level = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Character
        fields = ['url', 'name', 'level', 'character_preset']
