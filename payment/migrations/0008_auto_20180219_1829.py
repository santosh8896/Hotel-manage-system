# Generated by Django 2.0 on 2018-02-19 12:44

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0007_auto_20180219_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkin',
            name='check_in_date_time',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
