# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
import csv
import os

def add_rowan(apps, schema_editor):
    traits = apps.get_model('census_paleo', 'functional_traits')
    taxonomy = apps.get_model('census_paleo', 'taxonomy')
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "../data_imports/rowan_taxa_link_to_ancient_eco.csv")

    reader = csv.DictReader(open(path))
    for row in reader:
        ob, created = traits.objects.update_or_create(
            taxon = taxonomy.objects.get(pk=row["AncientEco_TaxonID"]),
            defaults={
                'locomotor_rowan':row["SS"],
                'trophic_rowan':row["TR"]
            }
        )


class Migration(migrations.Migration):

    dependencies = [
        ('census_paleo', '0011_auto_20170927_1221'),
    ]

    operations = [
        migrations.RunPython(add_rowan),
    ]