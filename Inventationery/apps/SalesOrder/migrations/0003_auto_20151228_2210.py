# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SalesOrder', '0002_auto_20151228_2208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salesordermodel',
            old_name='Cashed',
            new_name='Paid',
        ),
    ]
