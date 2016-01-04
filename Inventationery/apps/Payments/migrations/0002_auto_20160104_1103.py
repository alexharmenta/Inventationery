# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentmodel',
            name='PaymCode',
            field=models.CharField(max_length=5, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='paymentmodel',
            name='PaymName',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='paymmodemodel',
            name='PaymModeCode',
            field=models.CharField(max_length=5, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='paymmodemodel',
            name='PaymModeName',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
