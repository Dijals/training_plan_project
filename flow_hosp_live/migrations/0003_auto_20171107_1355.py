# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flow_hosp_live', '0002_coreexternaltraining'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coreexternaltraining',
            options={'managed': True},
        ),
    ]
