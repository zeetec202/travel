# Generated by Django 3.0.2 on 2020-01-10 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='customuser',
            name='customer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='fullname',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='customuser',
            name='number_phone',
            field=models.IntegerField(default=0),
        ),
    ]
