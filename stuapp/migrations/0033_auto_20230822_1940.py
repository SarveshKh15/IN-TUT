# Generated by Django 3.2.12 on 2023-08-22 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stuapp', '0032_auto_20230822_1924'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance_date', models.DateField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('acad_year_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='stuapp.acad_year')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='stuapp.subject')),
            ],
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(2, 'STAFF'), (1, 'HOD'), (3, 'STUDENT')], default=1, max_length=100),
        ),
        migrations.CreateModel(
            name='StudentNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_At', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(default=0)),
                ('studentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stuapp.student')),
            ],
        ),
        migrations.CreateModel(
            name='StudentLeave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fromdate', models.CharField(max_length=20)),
                ('todate', models.CharField(max_length=20)),
                ('status', models.IntegerField(default=0)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('studentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stuapp.student')),
            ],
        ),
        migrations.CreateModel(
            name='StudentFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField()),
                ('feedbackreply', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('studentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stuapp.student')),
            ],
        ),
        migrations.CreateModel(
            name='StaffNotifcation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_At', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(default=0, null=True)),
                ('staffID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stuapp.staff')),
            ],
        ),
        migrations.CreateModel(
            name='StaffLeave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fromdate', models.CharField(max_length=20)),
                ('todate', models.CharField(max_length=20)),
                ('status', models.IntegerField(default=0)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('staffID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stuapp.staff')),
            ],
        ),
        migrations.CreateModel(
            name='StaffFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField()),
                ('feedbackreply', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('staffID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stuapp.staff')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance_report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('attendance_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stuapp.attendance')),
                ('studentID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='stuapp.student')),
            ],
        ),
    ]
