# Generated by Django 3.1.7 on 2021-03-03 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_auto_20210302_1926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='recipes',
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(related_name='recipes', to='service.Ingredient'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='imageUrl',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='imageUrl',
            field=models.URLField(null=True),
        ),
    ]
