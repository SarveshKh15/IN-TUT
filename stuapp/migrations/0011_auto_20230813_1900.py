# Generated by Django 3.2.12 on 2023-08-13 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuapp', '0010_alter_customuser_user_type'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='course',
            new_name='branch',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(3, 'STUDENT'), (1, 'HOD'), (2, 'STAFF')], default=1, max_length=100),
        ),
    ]
