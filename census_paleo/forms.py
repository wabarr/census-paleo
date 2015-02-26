from django.forms import ModelForm, Form
from census_paleo.models import occurrence, taxonomy
from ajax_select import make_ajax_field

class OccurrenceForm(ModelForm):
    taxon = make_ajax_field(occurrence, "taxon", "taxonlookup")
    class Meta:
        model = occurrence

class TaxonForm(ModelForm):
    class Meta:
        model = taxonomy

class GetTaxonInfoForm(Form):
    taxon = make_ajax_field(occurrence, "taxon", "taxonlookup")

