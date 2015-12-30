# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0021_auto_20151228_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationmodel',
            name='LocationName',
            field=models.CharField(default=b'Default', unique=True, max_length=50),
        ),
    ]
