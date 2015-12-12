# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0006_auto_20151206_1719'),
        ('PurchOrder', '0002_auto_20151206_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchordermodel',
            name='Location',
            field=models.ForeignKey(blank=True, to='Inventory.LocationModel', null=True),
        ),
    ]
