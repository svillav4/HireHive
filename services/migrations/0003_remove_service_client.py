# Generated by Django 5.1.6 on 2025-03-11 03:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_rename_clientinterests_clientinterest_service_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='client',
        ),
    ]
