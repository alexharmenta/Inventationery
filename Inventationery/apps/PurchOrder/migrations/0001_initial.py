# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import Inventationery.apps.PurchOrder.models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0001_initial'),
        ('Vendor', '0002_auto_20151123_1424'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchLineModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('ItemName', models.CharField(max_length=50)),
                ('PurchQty', models.PositiveIntegerField()),
                ('PurchUnit', models.CharField(max_length=10)),
                ('PurchPrice', models.FloatField()),
                ('LineDisc', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('LinePercent', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('LineAmount', models.DecimalField(max_digits=20, decimal_places=2)),
                ('PurchLineStatus', models.CharField(default=b'BAC', max_length=100, choices=[(b'BAC', b'Back order'), (b'REC', b'Recibido'), (b'INV', b'Facturado'), (b'PAI', b'Pagado'), (b'CAN', b'Cancelado')])),
                ('LineNum', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('ItemId', models.ForeignKey(to='Inventory.InventModel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PurchOrderModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('PurchId', models.CharField(default=Inventationery.apps.PurchOrder.models.Get_PurchId, unique=True, max_length=45)),
                ('PurchName', models.CharField(max_length=100)),
                ('PurchaseType', models.CharField(default=b'PO', max_length=50, choices=[(b'PO', b'Orden de compra'), (b'RO', b'Orden devuelta')])),
                ('PurchStatus', models.CharField(default=b'OPE', max_length=100, choices=[(b'OPE', b'Abierta'), (b'BAC', b'Back order'), (b'REC', b'Recibido'), (b'INV', b'Facturado'), (b'PAI', b'Pagado'), (b'CAN', b'Cancelado')])),
                ('WorkerPurchPlacer', models.CharField(max_length=100, null=True, blank=True)),
                ('LanguageCode', models.CharField(default=b'es-mx', max_length=5)),
                ('DeliveryName', models.CharField(max_length=200, null=True, blank=True)),
                ('DeliveryDate', models.DateField(null=True, blank=True)),
                ('ConfirmedDlv', models.DateField(null=True, blank=True)),
                ('DlvMode', models.CharField(default=b'HOM', max_length=20, choices=[(b'HOM', b'A domicilio'), (b'BRA', b'En sucursal')])),
                ('CurrencyCode', models.CharField(default=b'MXN', max_length=3)),
                ('Payment', models.CharField(max_length=30, null=True, blank=True)),
                ('PaymMode', models.CharField(max_length=30, null=True, blank=True)),
                ('Remarks', models.TextField(default=None, null=True, blank=True)),
                ('SubTotal', models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True)),
                ('Total', models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True)),
                ('Paid', models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True)),
                ('Balance', models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True)),
                ('Vendor', models.ForeignKey(default=None, to='Vendor.VendorModel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='purchlinemodel',
            name='PurchOrder',
            field=models.ForeignKey(blank=True, to='PurchOrder.PurchOrderModel', null=True),
        ),
    ]
