# Generated by Django 4.1.7 on 2023-04-08 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_techlink_project_techlink_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='techlink',
            name='project',
        ),
        migrations.AddField(
            model_name='project',
            name='tech_links',
            field=models.ManyToManyField(to='main.techlink'),
        ),
    ]