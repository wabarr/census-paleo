# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('census_paleo', '0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='functional_traits',
            name='bodysize_brain_bunn',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[(b'1', b'I: < 23 kg'), (b'2', b'II: 23 - 113 kg'), (b'3', b'III: 113 - 340 kg'), (b'4', b'IV: 340 - 907 kg'), (b'5', b'V: 907 - 2721 kg'), (b'6', b'VI: >2721 kg')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='functional_traits',
            name='taxon',
            field=models.ForeignKey(to='census_paleo.taxonomy', unique=True),
            preserve_default=True,
        ),
    ]
