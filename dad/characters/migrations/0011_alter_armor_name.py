# Generated by Django 3.2 on 2022-03-29 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0010_alter_armor_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='armor',
            name='name',
            field=models.CharField(choices=[('light', 'light'), ('medium', 'medium'), ('heavy', 'heavy')], default='light', max_length=10),
        ),
    ]
