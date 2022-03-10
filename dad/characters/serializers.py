from rest_framework import serializers
from characters.models import Character, Weapon, Preset


class PresetSerializer(serializers.ModelSerializer):
    weapon = serializers.StringRelatedField(many=True)
    armor = serializers.StringRelatedField()

    class Meta:
        model = Preset
        fields = ['weapon', 'armor']

class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    character_preset = PresetSerializer()
    class Meta:
        model = Character
        fields = ['name', 'character_preset', 'level']
