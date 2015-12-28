# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('Vendor', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Inventory', '0007_remove_itemmodel_vendorprice'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemVendorModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('VendorPrice', models.DecimalField(max_digits=10, decimal_places=2)),
                ('Item', models.ForeignKey(default=None, blank=True, to='Inventory.ItemModel', null=True)),
                ('Vendor', models.ForeignKey(default=None, blank=True, to='Vendor.VendorModel', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MovementHistoryModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('TransactionType', models.CharField(max_length=30, choices=[(b'REC', b'Recepci\xc3\xb3n de producto'), (b'AJD', b'Ajuste de stock'), (b'PIC', b'Selecci\xc3\xb3n'), (b'SAL', b'Venta')])),
                ('Note', models.TextField(max_length=100, null=True, blank=True)),
                ('Qty', models.IntegerField(default=0, null=True)),
                ('Qty_prev', models.IntegerField(default=0, null=True)),
                ('Qty_after', models.IntegerField(default=0, null=True)),
                ('Location', models.ForeignKey(related_name='LocationHistory', blank=True, to='Inventory.LocationModel', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
