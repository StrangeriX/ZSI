from django.db import models


# Create your models here.
class Weapon(models.Model):
    CHOICES = [
        ('oneH', '1-handed'),
        ('twoH', '2-handed'),
        ('dual', 'dual wield'),
        ('lBow', 'long bow'),
        ('sBow', 'short bow'),
        ('wand', 'magic wand'),
        ('scepter', 'magic scepter'),
        ('mSward', 'magic sword'),
    ]
    name = models.CharField(max_length=10, choices=CHOICES)
    def __str__(self):
        return f'{self.name}'


class Armor(models.Model):
    CHOICES = [
        ('l', 'light'),
        ('m', 'medium'),
        ('h', 'heavy'),
    ]
    name = models.CharField(max_length=2, choices=CHOICES, default='l')

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

    def __str__(self):
        return f'{self.name}'

class Character(models.Model):
    sex_choices = [
        ('m', 'male'),
        ('f', 'female'),
    ]

    name = models.CharField(max_length=50, unique=True)
    sex = models.CharField(max_length=1, choices=sex_choices)
    level = models.IntegerField(default=1)
    character_preset = models.OneToOneField(Preset, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'{self.name}, lvl:{self.level}\nclass:{self.character_preset.name}'
