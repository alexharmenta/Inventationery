# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SalesOrder', '0003_auto_20151228_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesordermodel',
            name='SalesStatus',
            field=models.CharField(default=b'Abierto', max_length=100, choices=[(b'OPE', b'Abierta'), (b'RED', b'Reducido'), (b'INV', b'Facturado'), (b'CAS', b'Cobrado'), (b'CAN', b'Cancelado'), (b'RCA', b'Reducido/Cobrado')]),
        ),
    ]
