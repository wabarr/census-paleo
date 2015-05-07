from census_paleo.models import *
from django.contrib import admin
from ajax_select import make_ajax_form
from ajax_select.admin import AjaxSelectAdmin


#this is straight out of django docs

class taxonomyAdmin(admin.ModelAdmin):
    list_display = ("tclass","order","family","subFamily","tribe","genusName","specificEpithet")
    list_filter = ['tribe','taxonRank']

class censusLocationAdmin(admin.ModelAdmin):
    list_display = ("fullName","shortName","country","latitude","longitude")

class occurrenceAdmin(AjaxSelectAdmin):
    list_filter = ["ref","location"]
    list_display = ["ref","location","taxon","abundance","presenceAbsenceOnly"]
    list_editable = ["abundance","presenceAbsenceOnly"]
    form = make_ajax_form(occurrence, {'ref': 'referenceLookup', 'location':'locationLookup', 'taxon':'taxonLookup'})




admin.site.register(reference)
admin.site.register(taxonomy,taxonomyAdmin)
admin.site.register(censusLocation,censusLocationAdmin)
admin.site.register(occurrence, occurrenceAdmin)
admin.site.register(fossilLocation)
