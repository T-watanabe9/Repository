# Generated by Django 5.2.3 on 2025-07-01 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_byzer_game', '0011_card_race1_card_race2_card_race3'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='race',
        ),
    ]
