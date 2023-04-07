# Generated by Django 4.1.7 on 2023-04-07 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graffiti', '0008_graffiti_rotation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graffiti',
            name='font',
            field=models.CharField(choices=[('Roboto', 'Basic'), ('Creepster', 'Creepy'), ('Monoton', 'Vinyl'), ('Rye', 'Wildwest'), ('Henny Penny', 'Circus'), ('Press Start 2P', 'Gaming'), ('Emilys Candy', 'Love'), ('Bungee Shade', 'Shade3D'), ('Another', 'Graffiti'), ('Gruppo', 'Minimalistic')], max_length=30),
        ),
    ]