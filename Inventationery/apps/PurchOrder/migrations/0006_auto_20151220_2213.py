# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PurchOrder', '0005_auto_20151220_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchordermodel',
            name='PaymMode',
            field=models.ForeignKey(blank=True, to='Payments.PaymModeModel', null=True),
        ),
        migrations.AlterField(
            model_name='purchordermodel',
            name='Payment',
            field=models.ForeignKey(blank=True, to='Payments.PaymentModel', null=True),
        ),
        migrations.DeleteModel(
            name='PaymentModel',
        ),
        migrations.DeleteModel(
            name='PaymModeModel',
        ),
    ]
