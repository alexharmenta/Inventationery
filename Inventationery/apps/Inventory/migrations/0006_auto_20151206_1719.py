# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0005_auto_20151206_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventorymodel',
            name='Item',
            field=models.ForeignKey(related_name='Item', default=None, blank=True, to='Inventory.ItemModel', null=True),
        ),
    ]
