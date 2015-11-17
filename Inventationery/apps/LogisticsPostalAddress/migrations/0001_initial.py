# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DirParty', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogisticsPostalAddressModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('Description', models.CharField(max_length=30, null=True, blank=True)),
                ('Purpose', models.CharField(default=b'BUS', max_length=30, choices=[(b'BUSINESS', b'Negocio'), (b'DELIVERY', b'Entrega'), (b'HOME', b'Particular'), (b'INVOICE', b'Factura'), (b'PAYMENT', b'Pago'), (b'SERVICE', b'Servicio'), (b'OTHER', b'Otro')])),
                ('CountryRegionId', models.CharField(default=b'MEX', max_length=3)),
                ('ZipCode', models.CharField(max_length=5, null=True, blank=True)),
                ('Street', models.CharField(max_length=30, null=True, blank=True)),
                ('StreetNumber', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('BuildingCompliment', models.CharField(max_length=10, null=True, blank=True)),
                ('City', models.CharField(max_length=30, null=True, blank=True)),
                ('State', models.CharField(max_length=30, null=True, blank=True)),
                ('IsPrimary', models.BooleanField(default=False)),
                ('Party', models.ForeignKey(to='DirParty.DirPartyModel')),
            ],
        ),
    ]
