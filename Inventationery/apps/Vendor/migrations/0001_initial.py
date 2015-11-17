# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import Inventationery.apps.Vendor.models


class Migration(migrations.Migration):

    dependencies = [
        ('DirParty', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VendorModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('AccountNum', models.CharField(default=Inventationery.apps.Vendor.models.Get_Account_Num, unique=True, max_length=5)),
                ('AccountType', models.CharField(default=b'PAR', max_length=3, choices=[(b'PER', b'Persona'), (b'PAR', b'Organizaci\xc3\xb3n')])),
                ('OneTimeVendor', models.BooleanField(default=False)),
                ('VendGroup', models.CharField(default=b'Loc', max_length=3, choices=[(b'Loc', b'Local'), (b'Nat', b'Nacional'), (b'Int', b'Internacional')])),
                ('CreditLimit', models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)),
                ('CurrencyCode', models.CharField(default=b'MXN', max_length=3)),
                ('VATNum', models.CharField(max_length=13, blank=True)),
                ('Notes', models.TextField(max_length=200, blank=True)),
                ('Party', models.OneToOneField(related_name='VendorParty', null=True, default=None, blank=True, to='DirParty.DirPartyModel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
