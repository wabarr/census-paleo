# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('census_paleo', '0007_auto_20170321_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='functional_traits',
            name='trophic_reed',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[(b'B', b'leaves'), (b'C', b'meat'), (b'C/B', b'meat/bone'), (b'C/I', b'meat/invertebrates'), (b'FG', b'fresh grass'), (b'FL', b'fruit plus'), (b'G', b'grass'), (b'I', b'insects'), (b'MF', b'leaves and grass'), (b'OM', b'omnivorous'), (b'R', b'roots/bulbs')]),
            preserve_default=True,
        ),
    ]
