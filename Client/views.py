from django.http import JsonResponse
from django.template.loader import render_to_string

from ManagementSoftware.models import Client


def allclients(request):
    data = dict()
    if request.method == 'GET':
        clients = Client.objects.all()
        data['table'] = render_to_string(
            'client/clients_table.html',
            {'clients': clients},
            request=request
        )
    return JsonResponse(data)
