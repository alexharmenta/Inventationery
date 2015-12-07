# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PurchOrder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchordermodel',
            name='PurchStatus',
            field=models.CharField(default=b'OPE', max_length=100, choices=[(b'OPE', b'Abierta'), (b'BAC', b'Back order'), (b'REC', b'Recibido'), (b'INV', b'Facturado'), (b'PAI', b'Pagado'), (b'CAN', b'Cancelado'), (b'RPA', b'Recibido/Pagado')]),
        ),
    ]
