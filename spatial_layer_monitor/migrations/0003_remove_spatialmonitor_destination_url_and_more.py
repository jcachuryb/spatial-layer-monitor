# Generated by Django 5.0.11 on 2025-01-31 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spatial_layer_monitor', '0002_alter_requestauthentication_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spatialmonitor',
            name='destination_url',
        ),
        migrations.AddField(
            model_name='spatialmonitor',
            name='kmi_layer_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
