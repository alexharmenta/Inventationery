# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PurchOrder', '0010_auto_20151221_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchordermodel',
            name='DocumentState',
            field=models.CharField(default=b'Cerrado', max_length=20, choices=[(b'Abierto', b'Abierto'), (b'Cerrado', b'Cerrado')]),
        ),
        migrations.AlterField(
            model_name='purchordermodel',
            name='PurchStatus',
            field=models.CharField(default=b'Abierto', max_length=100, choices=[(b'OPE', b'Abierta'), (b'REC', b'Recibido'), (b'INV', b'Facturado'), (b'PAI', b'Pagado'), (b'CAN', b'Cancelado'), (b'RPA', b'Recibido/Pagado')]),
        ),
    ]
