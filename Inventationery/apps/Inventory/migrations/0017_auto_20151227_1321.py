# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0016_auto_20151227_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderhistorymodel',
            name='Price',
            field=models.DecimalField(default=0.0, max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='orderhistorymodel',
            name='SubTotal',
            field=models.DecimalField(default=0.0, max_digits=20, decimal_places=2),
        ),
    ]
