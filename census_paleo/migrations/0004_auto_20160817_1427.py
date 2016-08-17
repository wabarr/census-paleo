# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def change_ranks(apps, schema_editor):
    taxonomy = apps.get_model("census_paleo", "taxonomy")
    for taxon in taxonomy.objects.all():
        if taxon.taxonRank == 'KINGDOM':
            taxon.taxonRank = 'kingdom'
            taxon.save()
        elif taxon.taxonRank == 'PHYLUM':
            taxon.taxonRank = 'phylum'
            taxon.save()
        elif taxon.taxonRank == 'CLASS':
            taxon.taxonRank = 'tclass'
            taxon.save()
        elif taxon.taxonRank == 'ORDER':
            taxon.taxonRank = 'order'
            taxon.save()
        elif taxon.taxonRank == 'FAMILY':
            taxon.taxonRank = 'family'
            taxon.save()
        elif taxon.taxonRank == 'SUBFAMILY':
            taxon.taxonRank = 'subfamily'
            taxon.save()
        elif taxon.taxonRank == 'TRIBE':
            taxon.taxonRank = 'tribe'
            taxon.save()
        elif taxon.taxonRank == 'GENUS':
            taxon.taxonRank = 'genus'
            taxon.save()
        elif taxon.taxonRank == 'SPECIES':
            taxon.taxonRank = 'species'
            taxon.save()
        elif taxon.taxonRank == 'SUBSPECIES':
            taxon.taxonRank = 'subspecies'
            taxon.save()
        elif taxon.taxonRank == 'INFRAORDER':
            taxon.taxonRank = 'infraorder'
            taxon.save()
        elif taxon.taxonRank == 'SUBGENUS':
            taxon.taxonRank = 'subgenus'
            taxon.save()
        elif taxon.taxonRank == 'SUBORDER':
            taxon.taxonRank = 'suborder'
            taxon.save()
        elif taxon.taxonRank == 'SUPERFAMILY':
            taxon.taxonRank = 'superfamily'
            taxon.save()

class Migration(migrations.Migration):

    dependencies = [
        ('census_paleo', '0003_auto_20160817_1350'),
    ]

    operations = [
        migrations.RunPython(change_ranks),
    ]
