# Generated by Django 3.0.2 on 2020-01-13 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('dateSubscribe', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
    ]
