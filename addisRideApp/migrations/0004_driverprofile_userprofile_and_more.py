# Generated by Django 5.0.6 on 2024-05-25 14:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addisRideApp', '0003_remove_passengerprofile_profile_remove_profile_user_and_more'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='DriverProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('plate_number', models.CharField(max_length=20)),
                ('fullname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone_number', models.CharField(max_length=15)),
                ('fullname', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='plate_number',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='role',
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_driver',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='customuser_set', to='auth.group'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='customuser_set', to='auth.permission'),
        ),
    ]
