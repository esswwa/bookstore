# Generated by Django 5.0.3 on 2024-04-08 12:31

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_alter_review_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='date_review',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
