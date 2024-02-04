# Generated by Django 3.2.12 on 2023-08-15 16:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuapp', '0026_auto_20230815_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='altmobile',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AddField(
            model_name='staff',
            name='dob',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='staff',
            name='mobile',
            field=models.CharField(default='0', max_length=100),
        ),
    ]
