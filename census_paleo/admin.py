from census_paleo.models import *
from django.contrib import admin
from ajax_select import make_ajax_form
from ajax_select.admin import AjaxSelectAdmin
from ajax_select.fields import autoselect_fields_check_can_add

#this is straight out of django docs

class taxonomyAdmin(admin.ModelAdmin):
    list_display = ("tclass","order","family","subFamily","tribe","genusName","specificEpithet")
    list_filter = ['tribe','taxonRank']

class OccurrenceInline(admin.TabularInline):
    model = occurrence

    def get_form(self, request, obj=None, **kwargs):
        form = make_ajax_form(occurrence, {"ref": "referenceLookup", "taxon":"taxonLookup"})
        autoselect_fields_check_can_add(form, self.model, request.user)
        return form

class censusLocationAdmin(admin.ModelAdmin):
    list_display = ("fullName","shortName","country","latitude","longitude")
    inlines = [OccurrenceInline, ]

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
