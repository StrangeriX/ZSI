from rest_framework import serializers
from .models import Character, Weapon, Preset, Armor


class PresetForCharacterSerializer(serializers.HyperlinkedModelSerializer):
    weapon = serializers.StringRelatedField(many=True)
    armor = serializers.StringRelatedField()

    class Meta:
        model = Preset
        fields = ['name', 'weapon', 'armor']


class WeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = '__all__'


class PresetSerializer(serializers.HyperlinkedModelSerializer):
    armor = serializers.SlugRelatedField(queryset=Armor.objects.all(), slug_field='name')
    weapon = serializers.SlugRelatedField(many=True, queryset=Weapon.objects.all(), slug_field='name')

    class Meta:
        model = Preset
        fields = ['name', 'armor', 'weapon', 'description']


class CharacterSerializer(serializers.ModelSerializer):
    character_preset = PresetSerializer()

    class Meta:
        model = Character
        fields = ['url', 'name', 'level', 'character_preset']


class CharacterDetailSerializer(serializers.HyperlinkedModelSerializer):
    character_preset = PresetForCharacterSerializer()

    class Meta:
        model = Character
        fields = ['url', 'name', 'level', 'character_preset']
