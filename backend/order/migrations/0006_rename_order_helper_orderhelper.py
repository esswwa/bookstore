# Generated by Django 5.0.3 on 2024-04-03 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_alter_additionalgenre_id_alter_author_id_and_more'),
        ('order', '0005_order_helper'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order_Helper',
            new_name='OrderHelper',
        ),
    ]