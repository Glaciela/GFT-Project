# Generated by Django 5.1.7 on 2025-03-26 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permission', '0003_rename_is_public_permission_is_publihed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='date_end',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='permission',
            name='date_start',
            field=models.DateTimeField(),
        ),
    ]
