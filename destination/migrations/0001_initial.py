# Generated by Django 3.0.2 on 2020-01-20 01:35

import destination.models
from django.db import migrations, models
import django.db.models.deletion
import image_cropping.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id_country', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Lodging',
            fields=[
                ('id_lodging', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to=destination.models.Lodging.path_upload)),
                ('cropping', image_cropping.fields.ImageRatioField('image', '700x800', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping')),
                ('price', models.IntegerField()),
                ('address', models.TextField()),
                ('website', models.URLField(blank=True, null=True)),
                ('postalCode', models.IntegerField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='destination.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id_destination', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('cover', models.ImageField(upload_to=destination.models.Destination.path_upload1)),
                ('profile', models.ImageField(upload_to=destination.models.Destination.path_upload2)),
                ('croppingProfile', image_cropping.fields.ImageRatioField('profile', '700x800', adapt_rotation=False, allow_fullsize=False, free_crop=True, help_text=None, hide_image_field=False, size_warning=False, verbose_name='croppingProfile')),
                ('price', models.IntegerField()),
                ('slug', models.SlugField(blank=True, null=True)),
                ('dateCreate', models.DateField(auto_now_add=True, null=True)),
                ('dateUpdate', models.DateField(auto_now=True, null=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='destination.Country')),
            ],
        ),
    ]