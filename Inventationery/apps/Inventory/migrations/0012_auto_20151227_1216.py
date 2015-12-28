# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vendor', '0001_initial'),
        ('Inventory', '0011_auto_20151226_2308'),
    ]

    operations = [
        migrations.CreateModel(
            name='EcoResProductModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('BarCode', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('StdUnit', models.CharField(default=b'pza.', max_length=20, null=True, blank=True)),
                ('SalesUnit', models.CharField(default=b'pza.', max_length=20, null=True, blank=True)),
                ('PurchUnit', models.CharField(default=b'pza.', max_length=20, null=True, blank=True)),
                ('Notes', models.TextField(max_length=100, null=True, blank=True)),
                ('DefaulLocation', models.ForeignKey(related_name='DefaultLocation', blank=True, to='Inventory.LocationModel', null=True)),
                ('Item', models.ForeignKey(default=None, blank=True, to='Inventory.ItemModel', null=True)),
                ('LastVendor', models.ForeignKey(default=None, blank=True, to='Vendor.VendorModel', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameField(
            model_name='movementhistorymodel',
            old_name='Note',
            new_name='Notes',
        ),
    ]
