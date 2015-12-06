# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0003_auto_20151206_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventorymodel',
            name='Location',
            field=models.ForeignKey(related_name='Location', blank=True, to='Inventory.LocationModel', null=True),
        ),
        migrations.AlterField(
            model_name='inventorymodel',
            name='Qty',
            field=models.IntegerField(default=0),
        ),
    ]
