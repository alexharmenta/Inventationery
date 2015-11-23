# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DirPartyModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('Name', models.CharField(max_length=60)),
                ('NameAlias', models.CharField(max_length=50, null=True, blank=True)),
                ('LanguageCode', models.CharField(default=b'es-mx', max_length=5)),
                ('SecondName', models.CharField(max_length=30, null=True, blank=True)),
                ('FirstLastName', models.CharField(max_length=30)),
                ('SecondLastName', models.CharField(max_length=30, null=True, blank=True)),
                ('Gender', models.CharField(default=b'N', max_length=1, choices=[(b'M', b'Masculino'), (b'F', b'Femenino'), (b'N', b'No definido')])),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
