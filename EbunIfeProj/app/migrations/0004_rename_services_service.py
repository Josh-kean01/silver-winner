# Generated by Django 4.1 on 2024-03-13 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_services'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Services',
            new_name='Service',
        ),
    ]
