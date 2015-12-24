# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DirParty', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyInfoModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('CompanyType', models.CharField(max_length=20, choices=[(b'LEGE', b'Entidad jur\xc3\xaddica'), (b'FORE', b'Compan\xc3\xada extranjera'), (b'LEGP', b'Persona jur\xc3\xaddica')])),
                ('CoRegNum', models.CharField(max_length=13, blank=True)),
                ('VATNum', models.CharField(max_length=13, blank=True)),
                ('DataArea', models.CharField(max_length=4)),
                ('Party', models.OneToOneField(related_name='CompanyParty', null=True, default=None, blank=True, to='DirParty.DirPartyModel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
