# Generated by Django 5.0.3 on 2024-05-27 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_rename_order_helper_orderhelper'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_order_renewal_end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
