from django.db.models import Q
from ajax_select import LookupChannel
from census_paleo.models import taxonomy


class taxonLookup(LookupChannel):

    model = taxonomy

    def get_query(self,q,request):
        query = Q(specificEpithet__icontains=q) | Q(genusName__icontains=q) | Q(tribe__icontains=q) | Q(subFamily__icontains=q) | Q(family__icontains=q) | Q(tclass__icontains=q)
        return taxonomy.objects.filter(query).exclude(taxonRank__exact="SUBSPECIES")