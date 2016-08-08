from django.db.models import Q
from ajax_select import LookupChannel
from census_paleo.models import taxonomy, reference, censusLocation


class taxonLookup(LookupChannel):

    model = taxonomy

    def get_query(self,q,request):
        query = Q(taxonRank__icontains=q) | Q(specificEpithet__icontains=q) | Q(genusName__icontains=q) | Q(tribe__icontains=q) | Q(subFamily__icontains=q) | Q(family__icontains=q) | Q(tclass__icontains=q)
        return taxonomy.objects.filter(query).exclude(taxonRank__exact="SUBSPECIES")

    def can_add(self, user, argmodel):
        return True

class referenceLookup(LookupChannel):

    model = reference

    def get_query(self,q,request):
        query = Q(authorshortstring__icontains=q) | Q(year__contains=q)
        return reference.objects.filter(query)

    def can_add(self, user, argmodel):
        return True

class locationLookup(LookupChannel):

    model = censusLocation

    def get_query(self,q,request):
        query = Q(fullName__icontains=q) | Q(shortName__icontains=q)
        return censusLocation.objects.filter(query)

    def can_add(self, user, argmodel):
        return True
