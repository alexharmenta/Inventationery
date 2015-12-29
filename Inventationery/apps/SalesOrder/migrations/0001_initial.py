# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import Inventationery.apps.SalesOrder.models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0021_auto_20151228_1706'),
        ('Payments', '0001_initial'),
        ('Customer', '0002_customermodel_discount'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesLineModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('ItemName', models.CharField(max_length=50, null=True, blank=True)),
                ('SalesQty', models.PositiveIntegerField(null=True, blank=True)),
                ('SalesUnit', models.CharField(max_length=10, null=True, blank=True)),
                ('SalesPrice', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('LineDisc', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('LinePercent', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('LineAmount', models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True)),
                ('SalesLineStatus', models.CharField(default=b'BAC', max_length=100, null=True, blank=True, choices=[(b'BAC', b'Back order'), (b'RED', b'Reducido'), (b'INV', b'Facturado'), (b'CAS', b'Cobrado'), (b'CAN', b'Cancelado')])),
                ('LineNum', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('ItemId', models.ForeignKey(blank=True, to='Inventory.ItemModel', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SalesOrderModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('SalesId', models.CharField(default=Inventationery.apps.SalesOrder.models.Get_SalesId, unique=True, max_length=45)),
                ('SalesName', models.CharField(max_length=100)),
                ('SalesType', models.CharField(default=b'SO', max_length=50, choices=[(b'SO', b'Orden de venta'), (b'RO', b'Orden devuelta')])),
                ('SalesStatus', models.CharField(default=b'Abierto', max_length=100, choices=[(b'OPE', b'Abierta'), (b'RED', b'Reducido'), (b'INV', b'Facturado'), (b'CAS', b'Cobrado'), (b'CAN', b'Cancelado'), (b'RPA', b'Reducido/Cobrado')])),
                ('WorkerSalesPlacer', models.CharField(max_length=100, null=True, blank=True)),
                ('LanguageCode', models.CharField(default=b'es-mx', max_length=5)),
                ('DeliveryName', models.CharField(max_length=200, null=True, blank=True)),
                ('DeliveryDate', models.DateField(null=True, blank=True)),
                ('ConfirmedDlv', models.DateField(null=True, blank=True)),
                ('DlvMode', models.CharField(default=b'HOM', max_length=20, choices=[(b'HOM', b'A domicilio'), (b'BRA', b'En sucursal')])),
                ('CurrencyCode', models.CharField(default=b'MXN', max_length=3)),
                ('Remarks', models.TextField(default=None, null=True, blank=True)),
                ('SubTotal', models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True)),
                ('Total', models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True)),
                ('Paid', models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True)),
                ('Balance', models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True)),
                ('Enabled', models.BooleanField(default=True)),
                ('DocumentState', models.CharField(default=b'Cerrado', max_length=20, choices=[(b'Abierto', b'Abierto'), (b'Proceso', b'En proceso'), (b'Cerrado', b'Cerrado')])),
                ('Customer', models.ForeignKey(default=None, to='Customer.CustomerModel')),
                ('Location', models.ForeignKey(blank=True, to='Inventory.LocationModel', null=True)),
                ('PaymMode', models.ForeignKey(blank=True, to='Payments.PaymModeModel', null=True)),
                ('Payment', models.ForeignKey(blank=True, to='Payments.PaymentModel', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='saleslinemodel',
            name='SalesOrder',
            field=models.ForeignKey(blank=True, to='SalesOrder.SalesOrderModel', null=True),
        ),
    ]
