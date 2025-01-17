# Generated by Django 5.0.6 on 2024-05-24 14:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addisRideApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DriverProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_number', models.CharField(max_length=50)),
                ('vehicle_type', models.CharField(max_length=50)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='addisRideApp.profile')),
            ],
        ),
        migrations.CreateModel(
            name='PassengerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite_destination', models.CharField(max_length=100)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='addisRideApp.profile')),
            ],
        ),
    ]
