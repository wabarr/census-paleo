# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('census_paleo', '0002_auto_20160817_1334'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taxonomy',
            old_name='genusName',
            new_name='genus',
        ),
        migrations.RenameField(
            model_name='taxonomy',
            old_name='specificEpithet',
            new_name='species',
        ),
        migrations.RenameField(
            model_name='taxonomy',
            old_name='subFamily',
            new_name='subfamily',
        ),
        migrations.AlterField(
            model_name='taxonomy',
            name='taxonRank',
            field=models.CharField(max_length=100, null=True, choices=[(b'tclass', b'class'), (b'order', b'order'), (b'family', b'family'), (b'subfamily', b'subfamily'), (b'tribe', b'tribe'), (b'genus', b'genus'), (b'species', b'species'), (b'subspecies', b'subspecies'), (b'infraorder', b'infraorder'), (b'subgenus', b'subgenus'), (b'suborder', b'suborder'), (b'superfamily', b'superfamily')]),
            preserve_default=True,
        ),
    ]
