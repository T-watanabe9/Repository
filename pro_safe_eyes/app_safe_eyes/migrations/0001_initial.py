# Generated by Django 5.1.6 on 2025-03-06 01:35

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('content', models.TextField(blank=True, null=True)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('physical_health', models.IntegerField(choices=[(1, '良い'), (2, '普通'), (3, '悪い')], default=2)),
                ('mental_health', models.IntegerField(choices=[(1, '良い'), (2, '普通'), (3, '悪い')], default=2)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
