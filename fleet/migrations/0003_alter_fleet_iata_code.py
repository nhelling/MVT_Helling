# Generated by Django 4.1.3 on 2023-01-29 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleet', '0002_alter_fleet_options_alter_fleet_aircraft_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fleet',
            name='iata_code',
            field=models.CharField(max_length=3, unique=True, verbose_name='Codigo IATA'),
        ),
    ]
