# Generated by Django 3.0.2 on 2020-01-15 13:24

import about.models
from django.db import migrations, models
import django.db.models.deletion
import image_cropping.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id_team', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('profile', models.ImageField(upload_to=about.models.Team.path_upload)),
                ('cropping', image_cropping.fields.ImageRatioField('profile', '700x700', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping')),
                ('description', models.TextField()),
                ('dateCreate', models.DateField(auto_now_add=True, null=True)),
                ('dateUpdate', models.DateField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SosmedTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_sosmedTeam', models.CharField(max_length=11)),
                ('name', models.CharField(max_length=15)),
                ('link', models.URLField()),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.Team')),
            ],
        ),
    ]