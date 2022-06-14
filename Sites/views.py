from django.http import JsonResponse
from django.views import View
from django.template.loader import render_to_string

from ManagementSoftware.models import Site


# Create your views here.
'''
def allsites(request):
    data = dict()
    if request.method == 'GET':
        sites = Site.objects.all()
        data['table'] = render_to_string(
            'site/sites_table.html',
            {'sites': sites},
            request=request
        )
    return JsonResponse(data)
'''


class AllSites(View):
    def get(self, request):
        data = dict()
        sites = Site.objects.all()
        data['table'] = render_to_string(
            'site/sites_table.html',
            {'sites': sites},
            request=request
        )
        return JsonResponse(data)
