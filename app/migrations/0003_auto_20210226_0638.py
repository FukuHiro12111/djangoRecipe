# Generated by Django 3.0 on 2021-02-25 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210225_1625'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='recipe',
            constraint=models.UniqueConstraint(fields=('link', 'userRecipe'), name='myrecipe_unique'),
        ),
    ]
