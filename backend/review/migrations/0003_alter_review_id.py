# Generated by Django 5.0.3 on 2024-03-29 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_alter_review_book_alter_review_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='id',
            field=models.IntegerField(editable=False, primary_key=True, serialize=False),
        ),
    ]