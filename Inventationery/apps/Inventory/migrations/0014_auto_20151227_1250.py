# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0013_auto_20151227_1230'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ecoresproductmodel',
            old_name='DefaulLocation',
            new_name='DefaultLocation',
        ),
    ]
