# Generated by Django 4.2.6 on 2023-11-08 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('san', '0002_foodball_player_delete_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodball_player',
            name='p_salary',
            field=models.IntegerField(default=0),
        ),
    ]
