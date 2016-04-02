# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-02 21:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20160402_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planetarydata',
            name='avg_atm_molar_mass',
            field=models.FloatField(help_text='[kg/mol]', null=True, verbose_name='Average molar mass of the atmosphere'),
        ),
    ]