# Generated by Django 4.1.3 on 2023-02-05 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0004_alter_fligths_clase'),
    ]

    operations = [
        migrations.AddField(
            model_name='fligths',
            name='apto_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images'),
        ),
    ]
