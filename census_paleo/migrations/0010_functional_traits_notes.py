# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('census_paleo', '0009_auto_20170919_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='functional_traits',
            name='notes',
            field=models.TextField(null=True, blank=True),
        ),
    ]
