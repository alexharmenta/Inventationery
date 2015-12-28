# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0017_auto_20151227_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderhistorymodel',
            name='DocumentStatus',
            field=models.CharField(default='pagado', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderhistorymodel',
            name='Type',
            field=models.CharField(default='po', max_length=20, choices=[(b'PO', b'Orden de compra'), (b'SO', b'Orden de venta')]),
            preserve_default=False,
        ),
    ]
