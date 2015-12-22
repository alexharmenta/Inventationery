# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PurchOrder', '0004_auto_20151220_2115'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymModeModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('PaymModeCode', models.CharField(max_length=5)),
                ('PaymModeName', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='purchordermodel',
            name='PaymMode',
            field=models.ForeignKey(blank=True, to='PurchOrder.PaymModeModel', null=True),
        ),
        migrations.AlterField(
            model_name='purchordermodel',
            name='Payment',
            field=models.ForeignKey(blank=True, to='PurchOrder.PaymentModel', null=True),
        ),
    ]
