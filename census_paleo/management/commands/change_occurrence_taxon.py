from django.core.management.base import BaseCommand, CommandError
from census_paleo.models import *
from django.core.exceptions import ObjectDoesNotExist
from optparse import make_option

class Command(BaseCommand):
    help = 'changes taxon for all matching occurrences'
    option_list = BaseCommand.option_list + (
            make_option('--oldtaxon',default=None),
            make_option('--newtaxon', default=None),
    )

    def handle(self, *args, **options):
        try:
            old = options["oldtaxon"]
            new = options["newtaxon"]

            oldTaxon = taxonomy.objects.get(pk=old)
            newTaxon = taxonomy.objects.get(pk=new)

            matches = occurrence.objects.filter(taxon=oldTaxon)
            for match in matches:
                match.taxon = newTaxon
                match.save()
            self.stdout.write("success")
        except KeyError:
            raise CommandError("you must provide and old and a new taxon for changing occurrences")
        except ObjectDoesNotExist:
            raise CommandError("no matching taxon")


