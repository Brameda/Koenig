from django.db import models

from .backends.generic import PrintBackend
from .backends.google_backend import GoogleCloudPrintBackend

implementations = {
    'google': GoogleCloudPrintBackend(),
}

class PrintBackendField(models.Field):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 50)
        kwargs.setdefault('choices', [(v, v.name) for k, v in implementations.items()])
        super(PrintBackendField, self).__init__(*args, **kwargs)

    __metaclass__ = models.SubfieldBase

    def get_internal_type(self):
        return 'CharField'

    def to_python(self, value):
        if isinstance(value, PrintBackend):
            return value
        elif value == '':
            return None
        else:
            return implementations[value]

    def get_prep_value(self, value):
        if value is None:
            return ''
        elif isinstance(value, basestring):
            return value
        elif isinstance(value, PrintBackend):
            return value.slug
        else:
            assert False, 'Unknown type %s: %s' % (type(value), value)