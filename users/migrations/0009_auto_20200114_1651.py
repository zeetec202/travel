# Generated by Django 3.0.2 on 2020-01-14 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_customuser_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='token',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(default='o', max_length=1),
        ),
    ]