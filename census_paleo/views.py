import json
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Context, loader,RequestContext
from django.shortcuts import render_to_response,render
from census_paleo.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import modelform_factory
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required, permission_required
from census_paleo.forms import OccurrenceForm, GetTaxonInfoForm, TaxonForm
from django_pandas.io import read_frame
from django.utils.decorators import method_decorator


@login_required
def sites(request):
     return render_to_response('sites.html',
                             {},
                          context_instance=RequestContext(request))

def site_detail(request, sitename):

    if not sitename:
        HttpResponseRedirect("/census/sites")
    else:
        try: #first try to get from the fossil locations
            site = fossilLocation.objects.get(shortName = sitename)
        except: #if it aint a fossil site try the census locations
            try:
                site = censusLocation.objects.get(shortName = sitename)
            except:#if neither fossil nor census location then just return the map
                return HttpResponseRedirect("/census/sites/")

        site_occurrences = occurrence.objects.filter(location__shortName = sitename)
        if isinstance(site, fossilLocation):
            relatedSites = fossilLocation.objects.filter(projectArea = site.projectArea)
        else:
            relatedSites = None

        return render_to_response('site_detail.html',
                              {"site_occurrences":site_occurrences, "site":site, "relatedSites":relatedSites},
                              context_instance=RequestContext(request))



def sites_json(request):
    resp = []
    for each in censusLocation.objects.all():
        eachDict = {}
        eachDict["fullName"] = each.fullName
        eachDict["shortName"] = str(each.shortName)
        eachDict["lat"] = str(each.latitude)
        eachDict["long"] = str(each.longitude)
        resp.append(eachDict)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def occurrences_ajax(request):
#if request.is_ajax():
    filterArgs = {}
    for key,value in request.GET.iteritems():
        filterArgs[key] = value
    matchingOccurrences = occurrence.objects.filter(**filterArgs)
    resp = []
    for each in matchingOccurrences:
        eachDict = {}
        eachDict["ref"] = each.ref.__unicode__()
        eachDict["location"] = each.location.__unicode__()
        eachDict["locationWDPAid"] = each.location.WDPAID
        eachDict["habitat"] = each.taxon.habitat
        eachDict["taxon"] = each.taxon.__unicode__()
        eachDict["abundance"] = each.abundance
        eachDict["id"] = each.id
        resp.append(eachDict)
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def occurrences(request):


    refs = reference.objects.all()
    locations = censusLocation.objects.all()

    ####this appears necessary because sqlite does not support 'select distinct on' a particular field
    uniqueTaxaIDs = []
    for each in occurrence.objects.all():
        if each.taxon.id not in uniqueTaxaIDs:
            uniqueTaxaIDs.append(each.taxon.id)
    taxa = taxonomy.objects.filter(id__in=uniqueTaxaIDs)
    ####



    return render_to_response('occurrences.html',
                         {"refs":refs,"locations":locations,"taxa":taxa},
                      context_instance=RequestContext(request))



class ViewTaxon(DetailView):
    model = taxonomy
    template_name="taxonomy_detail.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ViewTaxon, self).dispatch(*args, **kwargs)

class ViewTaxa(ListView):
    model = taxonomy
    template_name = "taxonomy_list.html"
    queryset = taxonomy.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ViewTaxa, self).get_context_data(**kwargs)
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ViewTaxa, self).dispatch(*args, **kwargs)



def redirect2Admin(request):
    return HttpResponseRedirect("/census/admin/")

@login_required
def census_home(request):
    return render_to_response("census_home.html",
                                {},
                             RequestContext(request))

@permission_required("census_paleo.occurrence_add")
def enter_occurrence(request):
    if request.method == 'POST': # If the form has been submitted...
        form = OccurrenceForm(request.POST)# A form bound to the POST data
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "Occurrence added successfully.")
            returnDict = {'ref': request.POST["ref"],'location':request.POST["location"],'taxon':request.POST["taxon"]}

            #test if presenseAbsenceOnly was checked, and add to return dict if so.
            #this check is necessary because an unchecked box on the form will not be in post data, and will return MultiValueDictKeyError
            try:
                returnDict["presenceAbsenceOnly"] = request.POST["presenceAbsenceOnly"]
            except:
                pass

            returnedForm = OccurrenceForm(initial=returnDict)
            #returnedForm.fields["taxon"].queryset = taxaQS
            return render_to_response("enter_data.html",# Redirect after POST
                            {"form":returnedForm},
                         RequestContext(request))
    else:
        form = OccurrenceForm() # An unbound form
        #form.fields["taxon"].queryset = taxaQS
    return render_to_response("enter_data.html",
                            {"form":form},
                         RequestContext(request))

@login_required
def occurrence_pivot_json(request):
    kwarg_dict = {}
    try:
        kwarg_dict["ref"] = request.GET["ref"]
    except:
        kwarg_dict["ref"] = 1 #for now give a default ref, should probably change this in future

    occurrences = occurrence.objects.filter(**kwarg_dict)
    occ_frame = read_frame(occurrences, fieldnames=["location", "taxon","presenceAbsenceOnly","abundance"])
    pres_abs_vals = [value[0] for value in occurrences.values_list("presenceAbsenceOnly")]
    if all(pres_abs_vals):#if all of the occurrences are presenceAbsence only
        returnjson = occ_frame.pivot_table(index="location", columns="taxon", values="presenceAbsenceOnly",fill_value=0).to_json()
    elif all([element == False for element in pres_abs_vals]):
        returnjson = occ_frame.pivot_table(index="location", columns="taxon", values="abundance").to_json()
    else:
        returnjson = json.dumps({"error":"This reference mixes presence/absence data with abundance data. Please fix this in the database."})

    return HttpResponse(returnjson, content_type="application/json")

@login_required
def occurrence_pivot(request):
    try:
        refID = request.GET["ref"]
    except:
        refID = 1 #for now give a default ref, should probably change this in future

    try:
        ref = reference.objects.get(pk=refID)
    except:
        ref=None

    return render_to_response("occurrence_pivot.html",
                                {'reference':ref},
                                RequestContext(request))

@login_required
def add_taxon(request):
    # this control flow is more complicated than usual, because we will be coming here by POST both when we get refered here by
    # census_paleo.views.get_taxon_info_before_adding AND when we are submitting data to the db

    if request.method == "POST":

        try:
            #it has to be filter, not get, because filter returns QS, which allows me to use values()
            theTaxon = taxonomy.objects.filter(id = request.POST["taxon"])

            if theTaxon.count() <> 1:
                messages.add_message(request, messages.INFO, "Couldn't autopopulate taxonomy data. You will have to do it by hand.")
                theForm = TaxonForm()
            else:
                initialDict = theTaxon.values("kingdom", "phylum", "tclass", "order", "family","subFamily","tribe","genusName","specificEpithet")[0]
                theForm = TaxonForm(initial = initialDict)

        #if we are in POST mode, but get exception because there is no "taxon" field in post data, then we need are submitting data, and need to validate the form and save
        except:
            theForm = TaxonForm(request.POST)
            if theForm.is_valid():
                theForm.save()
                messages.add_message(request, messages.INFO, "Taxon added successfully.")
            else:
                messages.add_message(request, messages.INFO, "There are one are more errors. Please correct them below.")


    else: #return blank form if we didn't get here by post
        theForm = TaxonForm()

    return render_to_response("addTaxon.html",
        {"form":theForm},
        RequestContext(request)
    )

@login_required
def get_taxon_info_before_adding(request):
    theForm = GetTaxonInfoForm()

    return render_to_response("get_taxon_info_before_adding.html",
        {"form":theForm},
        RequestContext(request)
    )
