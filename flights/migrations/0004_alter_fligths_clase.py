# Generated by Django 4.1.3 on 2023-01-29 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_alter_fligths_options_alter_fligths_acft_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fligths',
            name='clase',
            field=models.CharField(choices=[('P - PAX', 'P - PAX'), ('F - FERRY', 'F - FERRY'), ('ALT', 'ALT'), ('CAN', 'CAN'), ('EZE', 'EZE')], max_length=10, verbose_name='Clase'),
        ),
    ]