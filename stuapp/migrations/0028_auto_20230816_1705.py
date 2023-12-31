# Generated by Django 3.2.12 on 2023-08-16 17:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stuapp', '0027_auto_20230815_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acad_year',
            name='end',
            field=models.CharField(blank=True, default=datetime.date(2023, 8, 16), max_length=100),
        ),
        migrations.AlterField(
            model_name='acad_year',
            name='start',
            field=models.CharField(blank=True, default=datetime.date(2023, 8, 16), max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(1, 'HOD'), (2, 'STAFF'), (3, 'STUDENT')], default=1, max_length=100),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stuapp.branch')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stuapp.staff')),
            ],
        ),
    ]
