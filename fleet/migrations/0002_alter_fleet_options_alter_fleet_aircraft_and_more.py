# Generated by Django 4.1.3 on 2023-01-09 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleet', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fleet',
            options={'verbose_name': 'Flota', 'verbose_name_plural': 'Aeronaves'},
        ),
        migrations.AlterField(
            model_name='fleet',
            name='aircraft',
            field=models.CharField(max_length=50, verbose_name='Aeronave'),
        ),
        migrations.AlterField(
            model_name='fleet',
            name='iata_code',
            field=models.CharField(max_length=3, verbose_name='Codigo IATA'),
        ),
        migrations.AlterField(
            model_name='fleet',
            name='seats',
            field=models.IntegerField(verbose_name='Capacidad'),
        ),
    ]
