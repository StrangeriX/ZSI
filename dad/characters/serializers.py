from rest_framework import serializers
from .models import Character, Weapon, Preset


class PresetForCharacterSerializer(serializers.ModelSerializer):
    weapon = serializers.StringRelatedField(many=True)
    armor = serializers.StringRelatedField()

    class Meta:
        model = Preset
        fields = ['name', 'weapon', 'armor']


class CharacterSerializer(serializers.ModelSerializer):
    character_preset = PresetForCharacterSerializer(read_only=True)

    class Meta:
        model = Character
        fields = ['pk', 'name', 'level', 'character_preset']


class WeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = '__all__'


class PresetSerializer(serializers.ModelSerializer):
    armor = serializers.StringRelatedField()
    weapon = serializers.StringRelatedField(many=True)

    class Meta:
        model = Preset
        fields = ['name', 'armor', 'weapon', 'description']