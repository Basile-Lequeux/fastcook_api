# Generated by Django 3.1.7 on 2021-05-12 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0009_user_favorites'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='createdBy',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='service.user'),
        ),
    ]
