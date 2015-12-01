# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vendor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('Qty', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ItemModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('ItemId', models.CharField(unique=True, max_length=20)),
                ('ItemType', models.CharField(blank=True, max_length=20, null=True, choices=[(b'INS', b'En stock'), (b'OFS', b'Fuera de stock'), (b'SER', b'Servicio')])),
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
        migrations.AddField(
            model_name='inventorymodel',
            name='Item',
            field=models.OneToOneField(related_name='Item', null=True, default=None, blank=True, to='Inventory.ItemModel'),
        ),
    ]
