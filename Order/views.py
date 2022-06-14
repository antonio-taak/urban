from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.template.loader import render_to_string

from ManagementSoftware.models import (
    Site,
    Article,
    Order,
)


# Create your views here.
class AllOrders(View):
    def get(self, request):
        data = dict()
        orders = Order.objects.filter(status="installed")
        print(orders)
        data['table'] = render_to_string(
            'order/orders_table.html',
            {'orders': orders},
            request=request
        )
        return JsonResponse(data)


class LoadSites(View):
    def get(self, request):
        client_id = request.GET.get('clients')
        sites = Site.objects.filter(client_id=client_id).order_by('name')
        return render(request, 'order/order_dropdown.html', {'sites': sites})


class LoadSuppliers(View):
    def get(self, request):
        supplier_id = request.GET.get('suppliers')
        suppliers = Article.objects.filter(supplier_id=supplier_id).order_by('name')
        return render(request, 'order/supplier_dropdown.html', {'suppliers': suppliers})


class GroupOrder(View):
    is_archive = None

    def get(self, request):
        if self.is_archive:
            orders = Order.objects.filter(status='installed').order_by('id')
        else:
            orders = Order.objects.exclude(status='installed').order_by('id')

        grouped_orders = dict()
        for order in orders:
            supplier_name = order.suppliers.name
            if grouped_orders.get(supplier_name):
                grouped_orders[supplier_name].append(order.__str__())
            else:
                grouped_orders[supplier_name] = [order.__str__()]

        return JsonResponse(grouped_orders)


'''
def allorders(request):
    data = dict()
    if request.method == 'GET':
        orders = Order.objects.filter(status="installed")
        print(orders)
        data['table'] = render_to_string(
            'order/orders_table.html',
            {'orders': orders},
            request=request
        )
    return JsonResponse(data)


def load_sites(request):
    client_id = request.GET.get('clients')
    sites = Site.objects.filter(client_id=client_id).order_by('name')
    return render(request, 'order/order_dropdown.html', {'sites': sites})


def load_suppliers(request):
    supplier_id = request.GET.get('suppliers')
    suppliers = Article.objects.filter(supplier_id=supplier_id).order_by('name')
    return render(request, 'order/supplier_dropdown.html', {'suppliers': suppliers})
'''
