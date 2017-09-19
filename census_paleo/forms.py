from django import forms
from django.forms import ModelForm, Form
from census_paleo.models import occurrence, taxonomy
from ajax_select import make_ajax_field



class OccurrenceForm(ModelForm):
    taxon = make_ajax_field(occurrence, "taxon", "taxonLookup")
    ref = make_ajax_field(occurrence, "ref", "referenceLookup")
    location = make_ajax_field(occurrence, "location", "locationLookup")
    notes = forms.CharField(widget=forms.Textarea, required=False)
    issue = forms.BooleanField(required=False, initial=False)
    class Meta:
        model = occurrence
        fields = "__all__"


class TaxonForm(ModelForm):
    class Meta:
        model = taxonomy
        fields = "__all__"

class GetTaxonInfoForm(Form):
    taxon = make_ajax_field(occurrence, "taxon", "taxonLookup")

class CSVUploadForm(Form):
    csvFile=forms.FileField(required=True, label="CSV file")
    #taxonomyColumnName = forms.CharField(required=True,label="Taxonomy Column Name", initial='taxon')
    #referenceColumnName = forms.CharField(required=True, label="Reference Column Name", initial='ref')
    #locationColumnName = forms.CharField(required=True, label='Location Column Name', initial='location')
    #presenceAbsenceData = forms.BooleanField(required=False, label="Presence Absence Data")

