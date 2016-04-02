# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-02 20:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_planetarydata_speed_of_sound'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planetarydata',
            name='atm_speed_of_light',
            field=models.FloatField(help_text='[m/s]', null=True, verbose_name='Speed of light in the atmosphere'),
        ),
        migrations.AlterField(
            model_name='planetarydata',
            name='average_density',
            field=models.FloatField(help_text='[kg/m³]', null=True),
        ),
        migrations.AlterField(
            model_name='planetarydata',
            name='avg_molecule_mass',
            field=models.FloatField(help_text='[kg]', null=True, verbose_name='Average mass of a single molecule'),
        ),
        migrations.AlterField(
            model_name='planetarydata',
            name='escape_velocity',
            field=models.FloatField(help_text='[m/s]', null=True),
        ),
        migrations.AlterField(
            model_name='planetarydata',
            name='radius',
            field=models.FloatField(help_text='[m]', null=True),
        ),
    ]