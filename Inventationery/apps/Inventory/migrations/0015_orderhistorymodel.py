# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0014_auto_20151227_1250'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderHistoryModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('DocumentId', models.CharField(max_length=30)),
                ('CustVendName', models.CharField(default=None, max_length=100)),
                ('DocumentDate', models.DateField()),
                ('DocumentTotal', models.DecimalField(max_digits=20, decimal_places=2)),
                ('Qty', models.IntegerField(default=0)),
                ('Price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('SubTotal', models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True)),
                ('Item', models.ForeignKey(related_name='OrderHistory', default=None, blank=True, to='Inventory.ItemModel', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
