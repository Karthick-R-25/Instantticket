# Generated by Django 4.2.20 on 2025-04-04 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0010_ticketcode_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticketcode',
            name='Name',
        ),
    ]
