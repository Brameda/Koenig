from .generic import PrintBackend

class GoogleCloudPrintBackend(PrintBackend):
    """
        Google Cloud Backend

        Notes on Google Backend
        -----------------------
        * authentication with oauth2 keys
        * please make all http calls with the requests lib http://docs.python-requests.org/en/latest/
    """
    name = 'Google Cloud Print'
    slug = 'google-cloud-print'

    # functions
    # ----------------
    # get all printers
    # get a print
    # submit print job