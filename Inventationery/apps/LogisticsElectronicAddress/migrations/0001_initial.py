# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DirParty', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogisticsElectronicAddressModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('Description', models.CharField(max_length=30, null=True, blank=True)),
                ('Type', models.CharField(default=b'TEL', max_length=30, choices=[(b'TEL', b'Tel\xc3\xa9fono'), (b'CEL', b'Celular'), (b'EMA', b'Email'), (b'URL', b'P\xc3\xa1gina web'), (b'FAX', b'Fax')])),
                ('Contact', models.CharField(max_length=200, null=True, blank=True)),
                ('IsPrimary', models.BooleanField(default=False)),
                ('Party', models.ForeignKey(to='DirParty.DirPartyModel')),
            ],
        ),
    ]
