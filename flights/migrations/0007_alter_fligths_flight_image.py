# Generated by Django 4.1.3 on 2023-02-05 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0006_rename_apto_image_fligths_flight_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fligths',
            name='flight_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images', verbose_name='Imagen'),
        ),
    ]