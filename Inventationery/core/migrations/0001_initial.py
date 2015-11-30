# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id_countries', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200, null=True, blank=True)),
                ('iso_alpha2', models.CharField(max_length=2, null=True, blank=True)),
                ('iso_alpha3', models.CharField(max_length=3, null=True, blank=True)),
                ('iso_numeric', models.IntegerField(null=True, blank=True)),
                ('currency_code', models.CharField(max_length=3, null=True, blank=True)),
                ('currency_name', models.CharField(max_length=32, null=True, blank=True)),
                ('currrency_symbol', models.CharField(max_length=3, null=True, blank=True)),
                ('flag', models.CharField(max_length=6, null=True, blank=True)),
            ],
            options={
                'db_table': 'countries',
                'managed': False,
            },
        ),
    ]
