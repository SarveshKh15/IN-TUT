# Generated by Django 4.1.4 on 2023-08-22 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuapp', '0033_auto_20230822_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(2, 'STAFF'), (3, 'STUDENT'), (1, 'HOD')], default=1, max_length=100),
        ),
    ]
