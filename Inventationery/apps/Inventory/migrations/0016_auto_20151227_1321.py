# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0015_orderhistorymodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderhistorymodel',
            name='SubTotal',
            field=models.DecimalField(default=0, max_digits=20, decimal_places=2),
            preserve_default=False,
        ),
    ]
