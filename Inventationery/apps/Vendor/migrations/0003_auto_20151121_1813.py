# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vendor', '0002_auto_20151117_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendormodel',
            name='AccountType',
            field=models.CharField(default=b'PER', max_length=3, choices=[(b'PER', b'Persona'), (b'PAR', b'Organizaci\xc3\xb3n')]),
        ),
    ]
