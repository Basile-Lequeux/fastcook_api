# Generated by Django 3.1.7 on 2021-06-13 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0012_auto_20210609_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='madeRecipe',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='recipeCreated',
            field=models.IntegerField(default=0),
        ),
    ]