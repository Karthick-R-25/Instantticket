# Generated by Django 4.2.20 on 2025-03-24 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0002_passenger_alter_bus_bus_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='username',
            field=models.CharField(max_length=150),
        ),
    ]
