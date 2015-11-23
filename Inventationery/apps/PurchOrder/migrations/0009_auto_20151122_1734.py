# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PurchOrder', '0008_auto_20151122_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchordermodel',
            name='Balance',
            field=models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='purchordermodel',
            name='Paid',
            field=models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='purchordermodel',
            name='SubTotal',
            field=models.DecimalField(default=0, max_digits=20, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchordermodel',
            name='Total',
            field=models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='purchordermodel',
            name='PurchStatus',
            field=models.CharField(default=b'OPE', max_length=100, choices=[(b'OPE', b'Abierta'), (b'BAC', b'Back order'), (b'REC', b'Recibido'), (b'INV', b'Facturado'), (b'PAI', b'Pagado'), (b'CAN', b'Cancelado')]),
        ),
    ]
