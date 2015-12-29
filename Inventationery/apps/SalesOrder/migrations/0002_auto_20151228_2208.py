# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SalesOrder', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salesordermodel',
            old_name='Paid',
            new_name='Cashed',
        ),
    ]
