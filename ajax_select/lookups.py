from django.db.models import Q
from ajax_select import LookupChannel
from census_paleo.models import taxonomy, reference, censusLocation, specimen, fossilLocation


class taxonLookup(LookupChannel):

    model = taxonomy

    def get_query(self,q,request):
        query = Q(taxonRank__icontains=q) | Q(species__icontains=q) | Q(genus__icontains=q) | Q(tribe__icontains=q) | Q(subfamily__icontains=q) | Q(family__icontains=q) | Q(tclass__icontains=q)
        return taxonomy.objects.filter(query).exclude(taxonRank__exact="subspecies")

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

class specimenLookup(LookupChannel):

    model = specimen

    def get_query(self, q, request):
        query = Q(collection_code__icontains=q) | Q(specimen_number__icontains=q)
        return specimens.objects.filter(query)

    def can_add(self, user, argmodel):
        return True

class assemblageLookup(LookupChannel):
    model = fossilLocation

    def get_query(self, q, request):
        query = Q(projectArea__icontains=q) | Q(formation__icontains=q) | Q(member__icontains=q) | Q(locality__icontains=q)
        return fossilLocation.objects.filter(query)

    def can_add(self, user, argmodel):
        return True