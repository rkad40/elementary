from django.conf import settings
from cronos import Time, epoch

def general(request):
    data = {
        'resource': {
            'query': {
                # In debug mode, force selected resources to reload for each request by appending
                # a query string of the form f'?reload_this_resource={epoch}' for all occurrences of
                # {{ resource.query.string }}.
                'string': '?reload_this_resource=' + str(int(epoch())) if settings.DEBUG else ''
            },
        },
        'debug': {
            'mode': {
                # Is debug mode enables?
                'enabled': settings.DEBUG,
            },
        },
    }
    return data