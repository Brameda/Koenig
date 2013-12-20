from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Register a new CloudPrinter'

    def handle(self, *args, **options):

        self.stdout.write('Successfully add a CloudPrinter')