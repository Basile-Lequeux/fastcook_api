# Generated by Django 3.1.7 on 2021-06-18 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0016_auto_20210617_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='moderate',
            field=models.BooleanField(default=False),
        ),
    ]
