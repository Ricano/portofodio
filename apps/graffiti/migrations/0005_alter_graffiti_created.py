# Generated by Django 4.1.7 on 2023-03-25 22:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graffiti', '0004_graffiti_created_alter_graffiti_font_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graffiti',
            name='created',
            field=models.DateField(default=datetime.datetime(2023, 3, 25, 22, 23, 28, 409240)),
        ),
    ]