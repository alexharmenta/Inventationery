# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PurchOrder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchlinemodel',
            name='ItemId',
            field=models.ForeignKey(blank=True, to='Inventory.InventModel', null=True),
        ),
        migrations.AlterField(
            model_name='purchlinemodel',
            name='ItemName',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='purchlinemodel',
            name='LineAmount',
            field=models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='purchlinemodel',
            name='PurchPrice',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='purchlinemodel',
            name='PurchQty',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='purchlinemodel',
            name='PurchUnit',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
    ]
