# Generated by Django 3.0.2 on 2020-01-20 03:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('destination', '0017_lodging_destination'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lodging',
            name='country',
        ),
    ]