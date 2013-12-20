from django.db import model

from .fields import PrintBackendField

class Printer(model.Models):
    """
    """
    name = None

    backend = PrintBackendField()
    backend_uuid = None

    @property
    def status(self):
        """
        """
        pass

    def submit_print_job(self, document, name):
        """
            return self.backend.submit_job(printer=self, document=document, name=name)
        """
        pass

    def test_print_job(self):
        """
            document = Default test page from test.documents
        """
        document = None #
        return self.submit_print_job(document=document)


class PrintJob(object):
    """
    """
    uuid = None
    description = None
    datetime = None
    status = None