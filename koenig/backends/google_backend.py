from .generic import PrintBackend

class GoogleCloudPrintBackend(PrintBackend):

    name = 'Google Cloud Print'
    slug = 'google-cloud-print'

    # functions
    # ----------------
    # get all printers
    # get a print
    # submit print job