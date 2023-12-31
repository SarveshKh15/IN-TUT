# Generated by Django 3.2.12 on 2023-08-13 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Academin_year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_start', models.DateTimeField(auto_now_add=True)),
                ('session_end', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_At', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
