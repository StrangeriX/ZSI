from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Weapon(models.Model):
    CHOICES = [
        ('1-handed', '1-handed'),
        ('2-handed', '2-handed'),
        ('dual wield', 'dual wield'),
        ('long bow', 'long bow'),
        ('short bow', 'short bow'),
        ('magic wand', 'magic wand'),
        ('magic scepter', 'magic scepter'),
        ('magic sword', 'magic sword'),
    ]
    name = models.CharField(max_length=20, choices=CHOICES)
    description = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.name}'


class Armor(models.Model):
    CHOICES = [
        ('light', 'light'),
        ('medium', 'medium'),
        ('heavy', 'heavy'),
    ]
    name = models.CharField(max_length=10, choices=CHOICES, default='light')

    def __str__(self):
        return f'{self.name}'


class Preset(models.Model):
    CHOICES = [
        ('mage', 'mage'),
        ('ranger', 'ranger'),
        ('warrior', 'warrior'),
    ]
    name = models.CharField(max_length=15, choices=CHOICES)
    weapon = models.ManyToManyField(Weapon)
    armor = models.ForeignKey(Armor, on_delete=models.CASCADE)
    description = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return f'{self.name}, {self.description}'


class Character(models.Model):
    sex_choices = [
        ('m', 'male'),
        ('f', 'female'),
    ]
    name = models.CharField(max_length=50, unique=True)
    sex = models.CharField(max_length=1, choices=sex_choices)
    level = models.IntegerField(default=1)
    character_preset = models.OneToOneField(Preset, on_delete=models.CASCADE, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, lvl:{self.level}\nclass:{self.character_preset.name}'
