from census_paleo.models import *
from django.contrib import admin
from ajax_select import make_ajax_form
from ajax_select.admin import AjaxSelectAdmin, AjaxSelectAdminTabularInline

#this is straight out of django docs

class OccurrenceInline(AjaxSelectAdminTabularInline):
    model = occurrence
    form = make_ajax_form(occurrence, {"ref": "referenceLookup", "taxon":"taxonLookup", "location":"locationLookup"})

class occurrenceAdmin(AjaxSelectAdmin):
    list_filter = ["ref","location"]
    list_display = ["ref","location","taxon","abundance","presenceAbsenceOnly"]
    list_editable = ["abundance","presenceAbsenceOnly"]
    form = make_ajax_form(occurrence, {'ref': 'referenceLookup', 'location':'locationLookup', 'taxon':'taxonLookup'})

class taxonomyAdmin(admin.ModelAdmin):
    list_display = ("tclass","order","family","subFamily","tribe","genusName","specificEpithet")
    list_filter = ['tribe','taxonRank', "family"]
    search_fields = ["genusName", "specificEpithet"]
    inlines = [OccurrenceInline, ]


class censusLocationAdmin(AjaxSelectAdmin):
    list_display = ("fullName","shortName","country","latitude","longitude", "WDPAID")
    inlines = [OccurrenceInline, ]
    search_fields = ["fullName", "shortName"]




class fossilLocationAdmin(admin.ModelAdmin):
    inlines = [OccurrenceInline, ]
    search_fields = ["fullName", "shortName"]


class referenceAdmin(admin.ModelAdmin):
    list_display = ["authorshortstring", "year","dataEntryComplete"]
    list_editable = ["year","dataEntryComplete"]
    inlines = [OccurrenceInline,]

admin.site.register(reference, referenceAdmin)
admin.site.register(taxonomy,taxonomyAdmin)
admin.site.register(censusLocation,censusLocationAdmin)
admin.site.register(occurrence, occurrenceAdmin)
admin.site.register(fossilLocation, fossilLocationAdmin)
