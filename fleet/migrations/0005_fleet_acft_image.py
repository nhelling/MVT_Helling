# Generated by Django 4.1.3 on 2023-02-04 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleet', '0004_alter_fleet_iata_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='fleet',
            name='acft_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images'),
        ),
    ]