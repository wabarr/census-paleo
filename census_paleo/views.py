import json
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Context, loader,RequestContext
from django.shortcuts import render_to_response,render
from census_paleo.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.core.exceptions import MultipleObjectsReturned
from django.forms.models import modelform_factory,modelformset_factory
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required, permission_required
from census_paleo.forms import OccurrenceForm, GetTaxonInfoForm, TaxonForm, CSVUploadForm
from django_pandas.io import read_frame
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse
import csv




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


# def occurrences_ajax(request):
# #if request.is_ajax():
#     filterArgs = {}
#     for key,value in request.GET.iteritems():
#         filterArgs[key] = value
#     matchingOccurrences = occurrence.objects.filter(**filterArgs)
#     resp = []
#     for each in matchingOccurrences:
#         eachDict = {}
#         eachDict["ref"] = each.ref.__unicode__()
#         eachDict["location"] = each.location.__unicode__()
#         eachDict["locationWDPAid"] = each.location.WDPAID
#         eachDict["habitat"] = each.taxon.habitat
#         eachDict["taxon"] = each.taxon.__unicode__()
#         eachDict["abundance"] = each.abundance
#         eachDict["id"] = each.id
#         resp.append(eachDict)
#     return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def occurrence_table_json(request):
    filterArgs = {}
    for key,value in request.GET.iteritems():
        if key <> "_":
            if value <> "":
                filterArgs[key] = value
    #fieldsToGet = ["location","taxon","abundance","ref"]
    if filterArgs:
        occurrences = occurrence.objects.filter(** filterArgs)
    else:
        occurrences = occurrence.objects.all()
    #note, normally I could just use values.list with * fieldsToGet, in the above ifelse statement
    #however, I need to get the unicode methods for several fields, so I need to create the values list manually
    formattedOccs = [[eachOcc.id,
                    eachOcc.location.__unicode__(),
                    eachOcc.taxon.__unicode__(),
                    eachOcc.abundance,
                    eachOcc.ref.__unicode__()] for eachOcc in occurrences]


    response = HttpResponse(content_type='application/json')

    responsedict = {"data":[]}
    for conn in formattedOccs:
        responsedict["data"].append(conn)
    response.write(json.dumps(responsedict))
    return response

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

class ViewOccurrence(DetailView):
    model = occurrence
    template_name="occurrence_detail.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ViewOccurrence, self).dispatch(*args, **kwargs)

class ViewOccurrences(ListView):
    model = occurrence
    template_name = "occurrence_list.html"
    queryset = occurrence.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ViewOccurrences, self).get_context_data(**kwargs)
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ViewOccurrences, self).dispatch(*args, **kwargs)


def redirect2Admin(request):
    return HttpResponseRedirect("/census/admin/")

@login_required
def census_home(request):
    return render_to_response("census_home.html",
                                {},
                             RequestContext(request))

# @login_required
# def enter_multiple_occurrences(request):
#     OccurrenceFormset = inlineformset_factory(taxonomy, occurrence)
#     try:
#         taxon = taxonomy.objects.get(pk=request.GET['taxonID'])
#     except:
#         taxon = None
#
#     if request.method == 'POST':
#         formset = OccurrenceFormset(request.POST, instance=taxon)
#         if formset.is_valid():
#             formset.save()
#             messages.add_message(request, messages.INFO, "Success!")
#         else:
#             messages.add_message(request, messages.INFO, "Failure.....")
#     else:
#         formset = OccurrenceFormset(instance=taxon)
#     return render_to_response("enter_multiple_occurrences.html",
#                               {"formset": formset, 'taxon':taxon},
#                               RequestContext(request))
#
@login_required
def enter_occurrence(request):
    if request.method == 'POST':
        errorMessage = None
        successMessage = None
        form = OccurrenceForm(request.POST)
        if form.is_valid():
            form.save()
            successMessage = "Success! Occurrence has been saved."
        else:
            errorMessage = []
            for key,value in form.errors.iteritems():
                errorMessage.append(str(value))
        response = json.dumps({'successMessage': successMessage, 'errorMessage':errorMessage})
        return HttpResponse(response, content_type="application/json")
    else:
        form = OccurrenceForm()
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
                initialDict = theTaxon.values("kingdom", "phylum", "tclass", "order", "family","subfamily","tribe","genus","species")[0]
                theForm = TaxonForm(initial = initialDict)

        #if we are in POST mode, but get exception because there is no "taxon" field in post data, then we need are submitting data, and need to validate the form and save
        except:
            theForm = TaxonForm(request.POST)
            if theForm.is_valid():
                newID = theForm.save().id
                messages.add_message(request, messages.INFO, "Success! Taxon {0} has been added.".format(str(newID)))
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

def resolve_taxon(request):
    # this is pretty bare bones
    filterArgs = {}
    for key, value in request.GET.iteritems():
        if key <> "_":
            if value <> "":
                filterArgs[key] = value
    try:
        match = taxonomy.objects.get(**filterArgs).id
    except Exception as e:
        match = e.message

    return HttpResponse(json.dumps(match), content_type="application/json")

@login_required
def CSV_occurrence_upload_chooser(request):
    upload_errors=[]
    error_rownums=[]
    upload_successes=[]
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            reader = csv.DictReader(request.FILES['csvFile'])
            counter=0
            for row in reader:
                counter+=1
                try:
                    ref = reference.objects.get(pk=row['ref'])
                    taxon = taxonomy.objects.get(pk=row['taxon'])
                    location = censusLocation.objects.get(pk=row['location'])
                    newObject = occurrence(ref=ref, taxon=taxon,location=location,presenceAbsenceOnly=True)
                    newObject.save()
                    upload_successes.append('Row ' + str(counter))
                except Exception as e:
                    upload_errors.append('Row ' + str(counter) + ": " + str(e))
                    error_rownums.append(str(counter))
        else:
            messages.add_message(request, messages.WARNING,'The form is not valid')
    else:
        form = CSVUploadForm()
    return render_to_response("csv_upload_occurrences_chooser.html",
                            {"form":form,
                             "upload_errors":upload_errors,
                             "upload_successes":upload_successes,
                             "error_rownums":error_rownums},
                         RequestContext(request))

