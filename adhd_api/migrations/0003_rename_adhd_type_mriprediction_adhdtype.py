# Generated by Django 5.0.4 on 2024-04-24 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adhd_api', '0002_mriprediction_adhd_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mriprediction',
            old_name='adhd_type',
            new_name='adhdType',
        ),
    ]
