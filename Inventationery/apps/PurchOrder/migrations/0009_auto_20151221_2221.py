# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PurchOrder', '0008_auto_20151221_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchordermodel',
            name='PurchStatus',
            field=models.CharField(default=b'Abierta', max_length=100),
        ),
    ]
