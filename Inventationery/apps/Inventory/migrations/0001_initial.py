# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vendor', '0002_auto_20151123_1424'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('ItemId', models.CharField(unique=True, max_length=20)),
                ('ItemName', models.CharField(max_length=50)),
                ('Description', models.CharField(max_length=100, null=True, blank=True)),
                ('UnitId', models.CharField(max_length=20)),
                ('Price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('VendorPrice', models.DecimalField(max_digits=10, decimal_places=2)),
                ('ItemImage', models.ImageField(default=None, null=True, upload_to=b'ItemTable/', blank=True)),
                ('PrimaryVendor', models.ForeignKey(default=None, blank=True, to='Vendor.VendorModel', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
