# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import Inventationery.apps.Customer.models


class Migration(migrations.Migration):

    dependencies = [
        ('DirParty', '0003_auto_20151228_1918'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('AccountNum', models.CharField(default=Inventationery.apps.Customer.models.Get_Account_Num, unique=True, max_length=45)),
                ('AccountType', models.CharField(default=b'PER', max_length=3, choices=[(b'PER', b'Persona'), (b'PAR', b'Organizaci\xc3\xb3n')])),
                ('OneTimeCustomer', models.BooleanField(default=False)),
                ('CustGroup', models.CharField(default=b'Loc', max_length=3, choices=[(b'Loc', b'Local'), (b'Nat', b'Nacional'), (b'Int', b'Internacional')])),
                ('CreditLimit', models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)),
                ('CurrencyCode', models.CharField(default=b'MXN', max_length=3)),
                ('VATNum', models.CharField(max_length=13, blank=True)),
                ('Notes', models.TextField(max_length=200, blank=True)),
                ('Party', models.OneToOneField(related_name='CustomerParty', null=True, default=None, blank=True, to='DirParty.DirPartyModel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
