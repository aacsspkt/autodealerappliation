# Generated by Django 4.0 on 2022-01-17 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase',
            old_name='vehicle_id',
            new_name='vehicle',
        ),
    ]