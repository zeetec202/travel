# Generated by Django 3.0.2 on 2020-01-13 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_customuser_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='token',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
    ]