# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flow_hosp_live', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoreExternaltraining',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('filename', models.CharField(max_length=255)),
                ('provider', models.CharField(max_length=200, null=True, blank=True)),
                ('training_type', models.CharField(max_length=200, null=True, blank=True)),
                ('training_time', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'core_externaltraining',
                'managed': False,
            },
        ),
    ]
