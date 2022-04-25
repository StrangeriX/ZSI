from django.contrib import admin
from .models import Character, Preset, Weapon, Armor

# Register your models here.
admin.site.register(Character)
admin.site.register(Preset)
admin.site.register(Weapon)
admin.site.register(Armor)
