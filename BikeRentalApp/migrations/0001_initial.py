# Generated by Django 3.2.6 on 2021-08-03 20:10

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bike_type', models.CharField(choices=[('ST', 'Standard'), ('TA', 'Tandem'), ('EL', 'Electric')], default='ST', max_length=2)),
                ('color', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Renter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('vip_num', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('price', models.FloatField(default=0.0)),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BikeRentalApp.bike')),
                ('renter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BikeRentalApp.renter')),
            ],
        ),
    ]
