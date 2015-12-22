# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PurchOrder', '0007_auto_20151221_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchordermodel',
            name='PurchStatus',
            field=models.CharField(default=b'OPE', max_length=100, choices=[(b'OPE', b'Abierta'), (b'REC', b'Recibido'), (b'INV', b'Facturado'), (b'PAI', b'Pagado'), (b'CAN', b'Cancelado'), (b'RPA', b'Recibido/Pagado')]),
        ),
    ]
