


class PrintGateway(object):

    def get_printer_list(self):
        pass

    def get_print_queue(self, printer):
        raise NotImplementedError("Subclasses must provide a way to get the job lis of the printer.")

    def get_print_job(self, printer, job_id):
        raise NotImplementedError("Subclasses must provide a way to get the job status")

    def submit_print_job(self, printer, document):
        raise NotImplementedError("Subclasses must provide a way to submit a document to the printing queue.")