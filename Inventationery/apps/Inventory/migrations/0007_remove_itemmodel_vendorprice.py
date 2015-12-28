# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0006_auto_20151206_1719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemmodel',
            name='VendorPrice',
        ),
    ]
