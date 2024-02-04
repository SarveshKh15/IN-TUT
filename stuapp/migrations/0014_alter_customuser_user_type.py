# Generated by Django 3.2.12 on 2023-08-13 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuapp', '0013_auto_20230813_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(1, 'HOD'), (3, 'STUDENT'), (2, 'STAFF')], default=1, max_length=100),
        ),
    ]
