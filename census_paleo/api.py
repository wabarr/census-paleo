# myapp/api.py
# ============
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie import fields
from census_paleo.models import occurrence, reference, taxonomy
from tastypie.authentication import Authentication

class OccurrenceResource(ModelResource):
    reference = fields.ToOneField("census_paleo.api.ReferenceResource", "ref",full=True)
    taxon = fields.ToOneField("census_paleo.api.TaxonomyResource", "taxon",full=True)
    class Meta:
        queryset = occurrence.objects.all()
        allowed_methods=['get']
        limit=0
        max_limit=0
        authentication = Authentication()#this means no authentication, which is OK in this case
        filtering = {
            'id' : ALL,
            "presenceAbsenceOnly" : ALL,
            "reference" : ALL_WITH_RELATIONS,
            "taxon" : ALL_WITH_RELATIONS,
        }

class TaxonomyResource(ModelResource):
    class Meta:
        queryset = taxonomy.objects.all()
        allowed_methods=['get']
        limit=0
        max_limit=0
        excludes = ["synonyms"]
        authentication = Authentication()#this means no authentication, which is OK in this case
        filtering = {
            "tribe" : ALL,
            "family" : ALL,
            "extant" : ALL,
            "subfamily" : ALL,
            "taxonRank" : ALL,

        }

class ReferenceResource(ModelResource):
    class Meta:
        queryset = reference.objects.all()
        allowed_methods=['get']
        limit=0
        max_limit=0
        authentication = Authentication()#this means no authentication, which is OK in this case