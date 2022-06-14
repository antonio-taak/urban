from django.http import JsonResponse
from django.views import View
from django.template.loader import render_to_string

from ManagementSoftware.models import Supplier


# Create your views here.
class AllSuppliers(View):
    def get(self, request):
        data = dict()
        suppliers = Supplier.objects.all()
        data['table'] = render_to_string(
            'supplier/suppliers_table.html',
            {'suppliers': suppliers},
            request=request
        )
        return JsonResponse(data)


'''
def allsuppliers(request):
    data = dict()
    if request.method == 'GET':
        suppliers = Supplier.objects.all()
        data['table'] = render_to_string(
            'supplier/suppliers_table.html',
            {'suppliers': suppliers},
            request=request
        )
    return JsonResponse(data)
'''