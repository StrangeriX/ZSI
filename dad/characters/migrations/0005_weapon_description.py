# Generated by Django 3.2 on 2022-03-17 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0004_auto_20220316_0829'),
    ]

    operations = [
        migrations.AddField(
            model_name='weapon',
            name='description',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
