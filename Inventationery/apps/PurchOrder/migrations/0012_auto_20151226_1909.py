# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PurchOrder', '0011_auto_20151226_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchordermodel',
            name='DocumentState',
            field=models.CharField(default=b'Cerrado', max_length=20, choices=[(b'Abierto', b'Abierto'), (b'Proceso', b'En proceso'), (b'Cerrado', b'Cerrado')]),
        ),
    ]
