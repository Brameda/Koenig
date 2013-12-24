from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Register a new CloudPrinter'

    def handle(self, *args, **options):
        # step one  : get list of all printers from backend
        # step two  : select printer to install
        # step three: copy printer settings to from backend to model
        # these functions can only be controlled by the commandline

        self.stdout.write('Successfully add a CloudPrinter')