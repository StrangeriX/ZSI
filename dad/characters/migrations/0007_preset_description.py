# Generated by Django 3.2 on 2022-03-17 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0006_alter_weapon_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='preset',
            name='description',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]