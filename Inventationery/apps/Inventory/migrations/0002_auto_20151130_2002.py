# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemmodel',
            name='Description',
            field=models.TextField(max_length=100, null=True, blank=True),
        ),
    ]
