# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0002_auto_20151224_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyinfomodel',
            name='AddressDescription',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='companyinfomodel',
            name='BuildingCompliment',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='companyinfomodel',
            name='City',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='companyinfomodel',
            name='CountryRegionId',
            field=models.CharField(default=b'MEX', max_length=3),
        ),
        migrations.AddField(
            model_name='companyinfomodel',
            name='Purpose',
            field=models.CharField(default=b'NEGOCIO', max_length=30),
        ),
        migrations.AddField(
            model_name='companyinfomodel',
            name='State',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='companyinfomodel',
            name='Street',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='companyinfomodel',
            name='StreetNumber',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='companyinfomodel',
            name='ZipCode',
            field=models.CharField(max_length=5, null=True, blank=True),
        ),
    ]
