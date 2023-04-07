# Generated by Django 4.1.7 on 2023-04-07 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_project_links_link'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Link',
            new_name='TechLink',
        ),
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
